# main.py
from asyncpg import Pool, Record
from asyncpg.pool import PoolAcquireContext
from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2AuthorizationCodeBearer
import jwt
from jwt.exceptions import PyJWTError
from typing import Optional, Any, Coroutine, Dict
from datetime import datetime, timedelta
from pydantic import BaseModel

from environment import *


async def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl="authorization",
    tokenUrl="token",
)


class TokenData(BaseModel):
    sub: str
    name: str
    is_gamemaster: Optional[bool] = False


async def get_current_user(request: Request = None) -> TokenData:
    token = request.session.get("access_token")
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
            )
        token_data = TokenData(**payload)
    except PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    return token_data


async def get_round_replays_for_user(user: TokenData, db_pool: Pool) -> Optional[Dict[int, str]]:
    """Returns the replays available to the user, as a dictionary of round_id -> replay file path."""

    replays = await get_replays_available()

    if not user.is_gamemaster:
        # Query the database for the rounds the user has played.
        rounds_played = await get_user_rounds_played(user.sub, db_pool, min(replays.keys()))

        # Filter replays to only those the user has played.
        replays = {round_id: replays[round_id] for round_id in rounds_played if round_id in replays.keys()}

    return replays


async def get_user_rounds_played(user_id: str, db_pool: Pool, starting_round: int = 0) -> Optional[list[int]]:
    """Query database to get user roles and properties"""
    rounds: list[int] = []
    async with db_pool.acquire() as conn:

        rows: list[Record] = await conn.fetch(
            'SELECT round_id FROM player_roundsjoined_view WHERE round_id > $1 AND user_id = $2;',
            starting_round, user_id
        )

    if rows:
        rounds = [int(row['round_id']) for row in rows]

    return rounds


async def did_user_play_round(user_id: str, round_id: int, db_pool: Pool) -> bool:
    """Check if a user has played a specific round"""
    async with db_pool.acquire() as conn:
        row: Optional[Record] = await conn.fetchrow(
            'SELECT 1 FROM player_roundsjoined_view WHERE user_id = $1 AND round_id = $2;',
            user_id, round_id
        )

    return row is not None


async def get_replays_available() -> Optional[Dict[int, str]]:
    """Query the local filesystem for replay files that exist, then map as round id -> file location relative to the base path."""
    replays: Dict[int, str] = dict()
    for root, dirs, files in os.walk(FILESYSTEM_REPLAYS_BASE_PATH):
        for file in files:
            if file.endswith(".zip"):
                # Extract round ID: YYYY-MM-DD-round_ROUNDID.zip
                # Example: 2023-10-01-round_123456.zip
                round_id = file.split("-")[3][6:][:-4]

                # File is just the name, not the full path. Join to the full path, then snip the base path off the front.
                file = os.path.join(root, file)  # Full path to the file
                file = str(file)
                file = file.replace(FILESYSTEM_REPLAYS_BASE_PATH, "")  # Snip base path
                file = file[1:]  # Snip leading slash

                replays[int(round_id)] = file

    return replays
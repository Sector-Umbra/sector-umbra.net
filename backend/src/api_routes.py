from fastapi import APIRouter, Depends, HTTPException, status
from starlette.requests import Request

from utils import TokenData, get_current_user, get_replays_available, did_user_play_round, \
    get_round_replays_for_user

router = APIRouter(prefix="/api", tags=["api"])

@router.get("/me")
async def read_users_me(
        current_user: TokenData = Depends(get_current_user),
        request: Request = None
):
    """Protected endpoint that requires authentication"""
    replays = await get_round_replays_for_user(current_user, request.app.state.db_pool)

    response_data = {
        "user_id": current_user.sub,
        "name": current_user.name,
        "gm_access": current_user.is_gamemaster,
        "replays": replays
    }

    return response_data

@router.get("/query-replay")
async def query_replays(
        current_user: TokenData = Depends(get_current_user),
        request: Request = None
):
    # Caddy forward-auth endpoint. Original URI, which should correspond to a file we have on the filesystem,
    # is passed as the X-Original-Uri header. Extract the round number, check if the user has access, if they do,
    # return 200 OK, if not, return 401 Unauthorized.

    header_value = request.headers.get("X-Original-Uri")
    if not header_value:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing replay file")

    # header_value should look like /yyyy/mm/YYYY-MM-DD-round_ROUNDID.zip . Only the last file name part is mandatory.
    # If file name part does not match YYYY-MM-DD-round_ROUNDID.zip, reject with 400 Bad Request.
    parts = header_value.split("/")
    file_name = parts[-1]
    if not file_name.endswith(".zip"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid replay file")

    # Extract round ID from file name
    try:
        round_id = int(file_name.split("_")[-1].split(".")[0])
    except ValueError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid replay file")

    replays_available = await get_replays_available()
    if round_id not in replays_available:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Replay not found")

    # Check if the user has played this round
    if not current_user.is_gamemaster and not await did_user_play_round(current_user.sub, round_id, request.app.state.db_pool):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You have not played this round")

    return {"message": "You have access to this replay"}
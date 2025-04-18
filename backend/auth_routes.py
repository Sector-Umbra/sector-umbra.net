from datetime import timedelta
from fastapi import APIRouter, Request, Response
from fastapi.exceptions import HTTPException
from starlette.responses import RedirectResponse

from environment import *
from utils import create_access_token

# OIDC Provider Configuration


router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/login")
async def login(request: Request):
    redirect_uri = OIDC_REDIRECT_URL
    return await OAUTH.oidc.authorize_redirect(request, redirect_uri)


@router.get("/callback")
async def auth_callback(request: Request):
    token = await OAUTH.oidc.authorize_access_token(request)
    user_info = token.get('userinfo')

    if not user_info:
        raise HTTPException(status_code=400, detail="Failed to get user info from OIDC provider")

    # Get user's ID from userinfo
    user_id = user_info.get('ss14-id')
    groups = user_info.get('groups')
    if not groups:
        groups = []

    # Create token payload with OIDC claims and roles
    token_payload = {
        "sub": user_id,
        "name": user_info.get("preferred_username"),
        "is_gamemaster": ("Game Master" in groups),
    }

    # Generate access token
    access_token = await create_access_token(
        data=token_payload,
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    print(access_token)

    # Store token in session
    request.session["access_token"] = access_token

    # Redirect to home page or a welcome page
    return RedirectResponse(url="/replays")

@router.get("/logout")
async def logout(request: Request, response: Response):
    request.session.pop("access_token", None)
    return RedirectResponse(url="/replays")
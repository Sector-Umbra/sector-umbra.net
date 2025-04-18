
from asyncpg import Pool
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
import asyncpg
from contextlib import asynccontextmanager

from environment import *
import auth_routes
import api_routes

# Database connection pool
async def create_db_pool() -> Pool:
    return await asyncpg.create_pool(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )


# Lifespan context manager for FastAPI
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create DB connection pool
    app.state.db_pool: Pool = await create_db_pool()

    # Register OIDC provider
    OAUTH.register(
        name="oidc",
        client_id=OIDC_CLIENT_ID,
        client_secret=OIDC_CLIENT_SECRET,
        server_metadata_url=OIDC_DISCOVERY_URL,
        client_kwargs={
            "scope": "openid"
        }
    )

    yield

    # Shutdown: Close DB connection pool
    await app.state.db_pool.close()


app = FastAPI(lifespan=lifespan)

# Add session middleware
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
app.include_router(auth_routes.router)
app.include_router(api_routes.router)

# Run with: uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
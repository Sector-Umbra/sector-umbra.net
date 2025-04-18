import os
from dotenv import load_dotenv
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config

load_dotenv()

# Configuration
SECRET_KEY = os.environ.get("SECRET_KEY", "this-should-be-changed-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
DB_DSN = os.environ.get("DATABASE_URL", "postgresql://127.0.0.1:5433/su-server")

DB_HOST = os.environ.get("DATABASE_HOST", "localhost")
DB_PORT = os.environ.get("DATABASE_PORT", 5432)
DB_USER = os.environ.get("DATABASE_USER", "postgres")
DB_PASSWORD = os.environ.get("DATABASE_PASSWORD", "a-password-that-does-not-belong-on-github")
DB_NAME = os.environ.get("DATABASE_NAME", "postgres")

OIDC_CLIENT_ID = os.environ.get("OIDC_CLIENT_ID", "your-client-id")
OIDC_CLIENT_SECRET = os.environ.get("OIDC_CLIENT_SECRET", "your-client-secret")
OIDC_DISCOVERY_URL = os.environ.get("OIDC_DISCOVERY_URL", "https://your-oidc-provider/.well-known/openid-configuration")
OIDC_REDIRECT_URL = os.environ.get("OIDC_REDIRECT_URL", "http://127.0.0.1:8000/auth/callback")

FILESYSTEM_REPLAYS_BASE_PATH = os.environ.get("FILESYSTEM_REPLAYS_BASE_PATH", "/path/to/replays")

# Create Config for OAuth
OAUTH_CONFIG = Config(environ=os.environ)
OAUTH = OAuth(OAUTH_CONFIG)
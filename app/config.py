import os

GITHUB_URL = os.environ.get("GITHUB_URL", "https://api.github.com")

POSTGRES_USER = os.environ.get("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "postgres")
POSTGRES_ADDRESS = os.environ.get("POSTGRES_ADDRESS", "localhost")
POSTGRES_DB = os.environ.get("POSTGRES_DB", "github_challenge")

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_ADDRESS}:5432/{POSTGRES_DB}"

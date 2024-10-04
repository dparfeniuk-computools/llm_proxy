import os
from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_PATH = Path(__file__).parent.parent.parent


class APIUrlsSettings(BaseModel):
    """API public urls settings."""

    docs: str = "/docs"
    redoc: str = "/redoc"


class PublicApiSettings(BaseModel):
    """Configure public API service settings."""

    domain: str = "http://backend.com"
    name: str = "LLM Proxy"
    version: str = "0.1.0"
    urls: APIUrlsSettings = APIUrlsSettings()


class DatabaseSettings(BaseModel):
    driver: str = "postgresql+asyncpg"
    host: str = os.getenv("LLM_PROXY__DATABASE__HOST", "database")
    port: str = os.getenv("LLM_PROXY__DATABASE__PORT", "5432")
    user: str = os.getenv("LLM_PROXY__DATABASE__USER", "postgres")
    password: str = os.getenv("LLM_PROXY__DATABASE__PASSWORD", "postgres")
    name: str = os.getenv("LLM_PROXY__DATABASE__NAME", "postgres")

    @property
    def url(self) -> str:
        # NOTE: SQLite is used as a database for testing purposes only.
        #       When pytest is in the runtime it automatically overrides
        #       the database driver
        if "sqlite" in self.driver:
            return f"{self.driver}:///{ROOT_PATH}/{self.name}.db"

        return (
            f"{self.driver}://"
            f"{self.user}:{self.password}@"
            f"{self.host}:{self.port}/"
            f"{self.name}"
        )


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        env_file=".env",
        extra="ignore",
    )

    # Application settings
    root_dir: Path
    src_dir: Path
    llama_endpoint: str = os.getenv("LLM_PROXY__LLAMA__ENDPOINT", "invalid")

    debug: bool = True
    public_api: PublicApiSettings = PublicApiSettings()
    database: DatabaseSettings = DatabaseSettings()


settings = Settings(
    root_dir=ROOT_PATH,
    src_dir=ROOT_PATH / "src",
)

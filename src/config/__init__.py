from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

from . import core
from . import cors as _cors
from . import database as _database
from . import public_api as _public_api


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_nested_delimiter="__",
        env_file=".env",
        extra="ignore",
    )

    # Application settings
    root_dir: Path
    src_dir: Path

    debug: bool = True
    public_api: _public_api.Settings = _public_api.Settings()
    cors: _cors.CorsSettings = _cors.CorsSettings()
    database: _database.DatabaseSettings = _database.DatabaseSettings()


settings = Settings(
    root_dir=core.ROOT_PATH,
    src_dir=core.ROOT_PATH / "src",
)

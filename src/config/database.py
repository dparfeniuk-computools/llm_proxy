from pydantic import BaseModel

from .core import ROOT_PATH


class DatabaseSettings(BaseModel):
    driver: str = "postgresql+asyncpg"
    host: str = "database"
    port: int = 5432
    user: str = "postgres"
    password: str = "postgres"
    name: str = "postgres"

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

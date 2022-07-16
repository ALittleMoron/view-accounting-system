import sys
from pathlib import Path


from pydantic import BaseSettings


class Settings(BaseSettings):
    BASE_DIR: Path = Path(__file__).parent.parent
    BACKEND_DIR: Path = Path(__file__).parent.parent.parent

    class Config:
        case_sensitive = True


settings = Settings()
sys.path.insert(0, str(settings.BACKEND_DIR))

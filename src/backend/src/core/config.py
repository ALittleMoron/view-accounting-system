import sys
from pathlib import Path


from pydantic import BaseSettings


class Settings(BaseSettings):
    BASE_DIR: Path = Path(__file__).parent.parent
    ROOT_DIR: Path = BASE_DIR.parent

    class Config:
        case_sensitive = True


settings = Settings()
sys.path.insert(0, str(settings.ROOT_DIR))

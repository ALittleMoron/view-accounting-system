from typing import Optional
import uvicorn

from src.main import app
from .base import BaseCommand


class Runserver(BaseCommand):
    def action(self, host: Optional[str] = 'localhost', port: Optional[int] = 8000):
        """Команда запуска локального тестового сервера.

        По умолчанию, использует --host localhost --port 8000.
        """
        uvicorn.run('src.main:app', host=host, port=port, reload=True, workers=2)  # type: ignore


command = Runserver()

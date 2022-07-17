from typing import Any

from .base import BaseCommand


class Echo(BaseCommand):
    def action(self, echo: str):
        """Обычная эхо-команда. Ничего не делает, кроме как повторять введенную строку."""
        print(echo)


command = Echo()

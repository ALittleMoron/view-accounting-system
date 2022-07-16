from src.management.commands.base import BaseCommand
from src.utils.exceptions import ExecuteError

class Executor:
    def __init__(self, commands: dict[str, BaseCommand]) -> None:
        self.commands = commands

    def execute(self, *args, **kwargs) -> None:
        command = self.commands.get(args[0])


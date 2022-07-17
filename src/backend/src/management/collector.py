import os
from importlib import import_module
from pathlib import Path

from src.utils.exceptions import ExecuteError

from .commands.base import BaseCommand


class Collector:
    def __init__(self) -> None:
        self.exclude_files = {'__init__.py', 'base.py', '__pycache__'}

    def collect(self) -> dict[str, BaseCommand]:
        result = {}
        postfix = 'commands'
        path = Path(__file__).parent / postfix
        dir_list = os.listdir(path)

        for _file in filter(lambda x: x not in self.exclude_files, dir_list):
            _file_name = _file.split('.')[0]
            try:
                package = import_module(f'src.management.{postfix}.{_file_name}')
                result[_file_name] = package.command
            except ImportError:
                raise ExecuteError(f"COllector have failed to open file {_file}.")
        return result

import os
from importlib import import_module
from pathlib import Path
from .commands.base import BaseCommand


class Collector:
    def __init__(self) -> None:
        self.exclude_files = {'__init__.py', 'base.py', '__pycache__'}
        self.collected_commands = self.collect()

    def collect(self) -> dict[str, BaseCommand]:
        result = {}
        postfix = 'commands'
        path = Path(__file__).parent / postfix
        dir_list = os.listdir(path)
        print(dir_list)
        for _file in filter(lambda x: x not in self.exclude_files, dir_list):
            _file_name = _file.split('.')[0]
            try:
                package = import_module(f'src.management.{postfix}.{_file_name}')
                result[_file_name] = package.command
            except ImportError:
                print(f"Can't open file {_file_name}...")
        return result


"""
Django-like manage.py script for some administration utils.
"""
import os
import sys

from core.config import settings
from src.management import execute_from_command_line
from src.utils.exceptions import ExecuteError


def main():
    """
    entrypoint in manage.py script
    """
    try:
        execute_from_command_line(sys.argv)
    except ExecuteError as e:
        print(e)
        sys.exit(87)


if __name__ == '__main__':
    main()

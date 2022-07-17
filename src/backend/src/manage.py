"""
Django-like manage.py script for some administration utils.
"""
import sys


from core import settings
from src.management import application
from src.utils.exceptions import ExecuteError


def main():
    """
    entrypoint in manage.py script
    """
    try:
        application()
    except ExecuteError as e:
        print(e)
        sys.exit(87)


if __name__ == '__main__':
    main()

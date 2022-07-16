from .executor import Executor
from .collector import Collector


def execute_from_command_line(args: list[str]) -> None:
    collector = Collector()
    executor = Executor(collector.collected_commands)


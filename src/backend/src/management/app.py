from typer import Typer
from .collector import Collector


def build_app():
    app = Typer()
    collector = Collector()

    for command_name, callback in collector.collect().items():
        app.command(command_name)(callback.action)  # type: ignore

    return app

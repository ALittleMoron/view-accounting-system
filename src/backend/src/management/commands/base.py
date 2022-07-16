from abc import ABC, abstractmethod

class BaseCommand(ABC):
    def __call__(self, *args, **kwargs) -> None:
        self.action(*args, **kwargs)

    @abstractmethod
    def action(self, *args, **kwargs) -> None:
        raise NotImplemented


from abc import ABC, abstractmethod

class LoggerClass(ABC):
    @abstractmethod
    def send(self, msg: str) -> None:
        pass
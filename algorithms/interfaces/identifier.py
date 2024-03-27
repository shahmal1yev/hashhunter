from abc import ABC, abstractmethod


class Identifier(ABC):
    @abstractmethod
    def validate(self) -> bool:
        pass

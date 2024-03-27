from abc import ABC, abstractmethod


class Identifier(ABC):
    @property
    @abstractmethod
    def algorithm_name(self) -> str:
        pass

    @abstractmethod
    def validate(self) -> bool:
        pass

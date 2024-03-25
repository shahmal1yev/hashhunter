from abc import ABC, abstractmethod


class Identifier(ABC):

    @abstractmethod
    def get_fix_length(self) -> int:
        pass

    @abstractmethod
    def validate(self) -> bool:
        pass

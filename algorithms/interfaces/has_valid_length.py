from abc import ABC, abstractmethod


class HasValidLength(ABC):
    @property
    @abstractmethod
    def byte_size(self) -> int:
        pass

    def get_valid_length(self) -> int:
        return int(self.byte_size * 2)

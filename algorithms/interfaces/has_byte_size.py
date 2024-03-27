from abc import ABC, abstractmethod


class HasByteSize(ABC):
    @property
    @abstractmethod
    def byte_size(self) -> int:
        pass

    def get_valid_character_length(self) -> int:
        return int(self.byte_size * 2)

    def get_valid_bit_length(self) -> int:
        return int(self.byte_size * 8)

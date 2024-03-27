from abc import ABC, abstractmethod

from helpers import is_hex_str


class HasByteSize(ABC):
    @property
    @abstractmethod
    def byte_size(self) -> int:
        pass

    def get_valid_character_length(self) -> int:
        return int(self.byte_size * 2)

    def get_valid_bit_length(self) -> int:
        return int(self.byte_size * 8)


class Identifier(HasByteSize):
    hash_value: str = None

    def __init__(self, hash_value: str):
        self.hash_value = hash_value

    @property
    @abstractmethod
    def algorithm_name(self) -> str:
        pass

    def validate_character_length(self) -> bool:
        return len(self.hash_value) == self.get_valid_character_length()

    def validate_bit_length(self) -> bool:
        return ((len(self.hash_value) / 2) * 8) == self.get_valid_bit_length()

    def validate_is_hex(self) -> bool:
        return is_hex_str(self.hash_value)

    def validate(self):
        is_hex = self.validate_is_hex()
        is_valid_character_length = self.validate_character_length()
        is_valid_bit_length = self.validate_bit_length()

        return is_hex and is_valid_character_length and is_valid_bit_length

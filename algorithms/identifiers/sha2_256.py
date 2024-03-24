from abc import ABC, abstractmethod
from algorithms.interfaces.identifier import Identifier


class SHA2256(Identifier):
    def __init__(self, hash_value: str):
        self.hash_value = hash_value
        self.length = self.get_fix_length()

    def get_name(self) -> str:
        return 'SHA2-256'

    def get_fix_length(self) -> int:
        return 64

    def validate(self):
        is_valid_length = len(self.hash_value) == self.length
        is_digit = self.hash_value.isdigit()
        is_alpha = self.hash_value.isalpha()
        is_alphanum = self.hash_value.isalnum()

        return is_valid_length and is_alphanum and not is_digit and not is_alpha

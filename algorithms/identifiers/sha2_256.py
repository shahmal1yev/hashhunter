from algorithms.interfaces.identifier import Identifier
from algorithms.interfaces.has_valid_length import HasValidLength
from helpers import is_hex_str


class SHA2256(Identifier, HasValidLength):
    algorithm_name: str = "SHA2256"
    byte_size: int = 32

    def __init__(self, hash_value: str):
        self.hash_value = hash_value

    def validate(self):
        is_hex = is_hex_str(self.hash_value)
        is_valid_length = len(self.hash_value) == self.get_valid_length()
        is_digit = self.hash_value.isdigit()
        is_alpha = self.hash_value.isalpha()
        is_alphanum = self.hash_value.isalnum()

        return is_hex and is_valid_length and is_alphanum and not is_digit and not is_alpha

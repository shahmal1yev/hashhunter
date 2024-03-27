from algorithms.interfaces.identifier import Identifier
from algorithms.interfaces.has_valid_length import HasValidLength
from helpers import is_hex_str


class SHA1(Identifier, HasValidLength):
    algorithm_name: str = "SHA1"
    byte_size: int = 20

    def __init__(self, hash_value):
        self.hash_value = hash_value

    def validate(self):
        is_hex = is_hex_str(self.hash_value)
        is_valid_length = len(self.hash_value) == self.get_valid_length()

        return is_hex and is_valid_length

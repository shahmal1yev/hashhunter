from algorithms.interfaces.identifier import Identifier
from helpers import is_hex_str


class NTLM(Identifier):
    algorithm_name: str = "NTLM"
    BYTE_LENGTH = 32

    def __init__(self, hash_value: str):
        self.hash_value = hash_value

    def validate(self) -> bool:
        is_hex = is_hex_str(self.hash_value)
        is_valid_length = len(self.hash_value) == self.BYTE_LENGTH
        is_digit = self.hash_value.isdigit()
        is_alpha = self.hash_value.isalpha()
        is_alphanum = self.hash_value.isalnum()

        return is_hex and is_valid_length and is_alphanum and not is_digit and not is_alpha

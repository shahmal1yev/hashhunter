from algorithms.interfaces.identifier import Identifier


class MD5(Identifier):
    ALGORITHM_NAME = "MD5"

    def __init__(self, hash_value: str):
        self.hash_value = hash_value
        self.length = self.get_fix_length()

    def get_fix_length(self) -> int:
        return 32

    def validate(self) -> bool:
        is_valid_length = len(self.hash_value) == self.length
        is_digit = self.hash_value.isdigit()
        is_alpha = self.hash_value.isalpha()
        is_alphanum = self.hash_value.isalnum()

        return is_valid_length and is_alphanum and not is_digit and not is_alpha

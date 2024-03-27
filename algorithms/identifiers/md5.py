from algorithms.interfaces.identifier import Identifier


class MD5(Identifier):
    algorithm_name: str = "MD5"
    byte_size: int = 16
    hash_value: str = None

    def __init__(self, hash_value: str):
        self.hash_value = hash_value

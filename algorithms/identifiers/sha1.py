from algorithms.interfaces.identifier import Identifier


class SHA1(Identifier):
    algorithm_name: str = "SHA1"
    byte_size: int = 20
    hash_value: str = None

    def __init__(self, hash_value):
        self.hash_value = hash_value

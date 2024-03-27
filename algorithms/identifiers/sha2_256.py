from algorithms.interfaces.identifier import Identifier


class SHA2256(Identifier):
    algorithm_name: str = "SHA2256"
    byte_size: int = 32
    hash_value: str = None

    def __init__(self, hash_value: str):
        self.hash_value = hash_value

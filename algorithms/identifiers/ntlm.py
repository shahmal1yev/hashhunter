from algorithms.interfaces.identifier import Identifier


class NTLM(Identifier):
    algorithm_name: str = "NTLM"
    byte_size: int = 16
    hash_value: str = None

    def __init__(self, hash_value: str):
        self.hash_value = hash_value

from algorithms.interfaces.identifier import Identifier


class SHA2256(Identifier):
    algorithm_name: str = "SHA2256"
    byte_size: int = 32

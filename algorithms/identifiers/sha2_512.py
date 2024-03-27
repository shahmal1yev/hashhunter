from algorithms.interfaces.identifier import Identifier


class SHA2512(Identifier):
    algorithm_name: str = "SHA2-512"
    byte_size: int = 64

from algorithms.interfaces.identifier import Identifier


class SHA1(Identifier):
    algorithm_name: str = "SHA1"
    byte_size: int = 20

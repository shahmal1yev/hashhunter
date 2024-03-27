from algorithms.interfaces.identifier import Identifier


class MD4(Identifier):
    algorithm_name: str = "MD4"
    byte_size: int = 16

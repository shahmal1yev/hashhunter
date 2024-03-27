from algorithms.interfaces.identifier import Identifier


class MD5(Identifier):
    algorithm_name: str = "MD5"
    byte_size: int = 16

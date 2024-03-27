from algorithms.interfaces.identifier import Identifier


class NTLM(Identifier):
    algorithm_name: str = "NTLM"
    byte_size: int = 16

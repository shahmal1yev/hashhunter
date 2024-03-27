from algorithms.interfaces import Identifier


class MD4(Identifier):
    algorithm_name: str = "MD4"
    byte_size: int = 16


class MD5(Identifier):
    algorithm_name: str = "MD5"
    byte_size: int = 16


class NTLM(Identifier):
    algorithm_name: str = "NTLM"
    byte_size: int = 16


class SHA1(Identifier):
    algorithm_name: str = "SHA1"
    byte_size: int = 20


class SHA2256(Identifier):
    algorithm_name: str = "SHA2-256"
    byte_size: int = 32


class SHA2512(Identifier):
    algorithm_name: str = "SHA2-512"
    byte_size: int = 64

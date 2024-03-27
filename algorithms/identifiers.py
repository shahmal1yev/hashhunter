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


class SHA2224(Identifier):
    algorithm_name: str = "SHA2-224"
    byte_size: int = 28


class SHA2384(Identifier):
    algorithm_name: str = "SHA2-384"
    byte_size: int = 48


class SHA3224(Identifier):
    algorithm_name: str = "SHA3-324"
    byte_size: int = 28


class SHA3256(Identifier):
    algorithm_name: str = "SHA3-256"
    byte_size: int = 32


class SHA3384(Identifier):
    algorithm_name: str = "SHA3-384"
    byte_size: int = 48


class SHA3512(Identifier):
    algorithm_name: str = "SHA3-512"
    byte_size: int = 64


class RIPEMD160(Identifier):
    algorithm_name: str = "RIPEMD160"
    byte_size: int = 20


class BLAKE2b512(Identifier):
    algorithm_name: str = "BLAKE2b-512"
    byte_size: int = 64


class GOSTR34112012256(Identifier):
    algorithm_name: str = "GOST R 34.11-2012 (Streebog) 256-bit, big-endian"
    byte_size: int = 32


class GOSTR34112012512(Identifier):
    algorithm_name: str = "GOST R 34.11-2012 (Streebog) 512-bit, big-endian"
    byte_size: int = 64


class HalfMD5(Identifier):
    algorithm_name: str = "Half MD5"
    byte_size: int = 8


class Keccak224(Identifier):
    algorithm_name: str = "Keccak-224"
    byte_size: int = 28


class Keccak256(Identifier):
    algorithm_name: str = "Keccak-224"
    byte_size: int = 32


class Keccak384(Identifier):
    algorithm_name: str = "Keccak-224"
    byte_size: int = 48


class Keccak512(Identifier):
    algorithm_name: str = "Keccak-224"
    byte_size: int = 64


class Whirlpool(Identifier):
    algorithm_name = "Whirlpool"
    byte_size: int = 64

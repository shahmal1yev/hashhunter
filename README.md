# Hash Hunter (hash-identifier)

Hash Hunter is a Python tool that identifies hashes from a wordlist, integrating with HashCat.

![img_1.png](build/hashhunter/img.png)

### Who is it for?

- Ideal for cybersecurity professionals who want to analyze hash types.
- Suitable for anyone who wants to analyze hash lists quickly and easily.
- Anyone looking to better understand and analyze hash types can benefit from this tool.

### New Feature: Hash List Upload

HashHunter's newest feature allows users to directly upload a hash list to the tool. This feature groups hash lists into different files, making them suitable for use with hashcat.

### Usage

- Identify hash values from a specified file and save only the most possible hash groups:

```shell
hashhunter -H path/to/hash_list.txt --group
```

- Identify hash values from a specified file and save both the most and least possible hash groups:

```shell
hashhunter -H path/to/hash_list.txt --group -a
```

- Identify hash values from a specified file and save all output to a file:

```shell
hashhunter -H path/to/hash_list.txt -pO path/to/output.txt
```

### Parameters

| Parameter          | Shortcut | Description                                                                       |
|--------------------|----------|-----------------------------------------------------------------------------------|
|                    | **-H**   | Path to the file containing hashes to identify. Required parameter.               |
| **--plain-output** | **-pO**  | Used to save all output to a file.                                                |
| **--group**        | **-g**   | Used to group hash values and save them with names based on HashCat's hash modes. |
| **--all**          | **-a**   | Used to save both most and least hash groups.                                     |

### Supported Algorithms

- MD4
- MD5
- Half MD5
- NTLM
- SHA1
- SHA2-224
- SHA2-256
- SHA2-384
- SHA2-512
- SHA3-224
- SHA3-256
- SHA3-384
- SHA3-512
- Keccak-224
- Keccak-256
- Keccak-384
- Keccak-512
- RIPEMD160,
- BLAKE2b512
- GOST R 34.11-2012 (Streebog) 256-bit
- GOST R 34.11-2012 (Streebog) 512-bit
- Whirlpool

### Authors

- [@shahmal1yev](https://www.github.com/shahmal1yev)
- [@blackploit](https://www.github.com/blackploit)


import argparse
import constants
from tabulate import tabulate
from algorithms.identifiers.md5 import MD5

parser = argparse.ArgumentParser(description="Identify hashes from a wordlist that integrates with HashCat")
parser.add_argument('hash_list_file', help='path to the file containing hashes to identify')


def hash_list_parser(hash_list_file_path: str):
    with open(hash_list_file_path, 'r') as f:
        hash_list = f.read().splitlines()

    return hash_list


if __name__ == '__main__':
    args = parser.parse_args()

    print(constants.WELCOME)
    print(constants.SOCIAL_INFO, '\n')

    algorithms = [
        MD5
    ]

    for hash_value in hash_list_parser(args.hash_list_file):
        possible_hashes = []

        for algorithm in algorithms:
            algorithm_instance = algorithm(hash_value)
            if (algorithm_instance.validate()):
                possible_hashes.append([f"[+] {algorithm.__name__}"])

        if possible_hashes:
            print("\n\n", tabulate(possible_hashes, headers=[f"[+] Possible algorithms for {hash_value}"]))

    print(constants.GOOD_LUCK)
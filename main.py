import argparse
import os
from tabulate import tabulate

import constants
from algorithms.identifiers.md5 import MD5
from helpers import parse_hash_list, make_hash_groups_dir

parser = argparse.ArgumentParser(description="Identify hashes from a wordlist that integrates with HashCat")
parser.add_argument('-H', dest="hash_list_file", help='path to the file containing hashes to identify')


if __name__ == '__main__':
    args = parser.parse_args()

    print(constants.WELCOME)
    print(constants.SOCIAL_INFO, '\n')

    algorithms = [MD5]

    possible_hashes = {}

    for hash_value in parse_hash_list(args.hash_list_file):
        validated_algorithms = []

        for algorithm in algorithms:
            instance = algorithm(hash_value)
            if instance.validate():
                possible_hashes.setdefault(algorithm.__name__, []).append(hash_value)
                validated_algorithms.append(algorithm.__name__)

        if validated_algorithms:
            print("\n\n", tabulate([
                [f"[+] {algorithm_name}"] for algorithm_name in validated_algorithms
            ], headers=[f"Possible algorithms for {hash_value}"]))

    if possible_hashes:
        hash_group_dir_name = make_hash_groups_dir()

        for hash_group, hashes in possible_hashes.items():
            with open(os.path.join(hash_group_dir_name, f"{hash_group.lower()}.txt"), "a") as hash_group_file:
                hash_group_file.writelines(f"{hash}\n" for hash in hashes)

    print(constants.GOOD_LUCK)

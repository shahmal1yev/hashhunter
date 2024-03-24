import argparse
from tabulate import tabulate

import constants
from helpers import parse_hash_list, make_hash_groups_dir, write_hash_group_file

parser = argparse.ArgumentParser(description="Identify hashes from a wordlist that integrates with HashCat")
parser.add_argument('-H', dest="hash_list_file", help='path to the file containing hashes to identify')


if __name__ == '__main__':
    args = parser.parse_args()

    print(constants.WELCOME)
    print(constants.SOCIAL_INFO, '\n')

    possible_hashes = {}

    for hash_value in parse_hash_list(args.hash_list_file):
        validated_algorithms = []

        for algorithm, hashcat_code in constants.ACTIVE_ALGORITHMS.items():
            instance = algorithm(hash_value)
            if instance.validate():
                possible_hashes.setdefault(hashcat_code, []).append(hash_value)
                validated_algorithms.append(algorithm.__name__)

        if validated_algorithms:
            print("\n\n", tabulate([
                [f"[+] {algorithm_name}"] for algorithm_name in validated_algorithms
            ], headers=[f"Possible algorithms for {hash_value}"]))

    if possible_hashes:
        hash_group_dirname = make_hash_groups_dir()

        for hash_group, hash_values in possible_hashes.items():
            write_hash_group_file(
                hash_group_dirname=hash_group_dirname,
                algorithm_hashcat_code=hash_group,
                hash_values=hash_values
            )

    print(constants.GOOD_LUCK)

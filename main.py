import argparse
from tabulate import tabulate

import constants
from helpers import (parse_hash_list,
                     make_hash_groups_dir,
                     write_hash_group_file,
                     print_to_file)

parser = argparse.ArgumentParser(prog='hashhunter',
                                 description="Identify hashes from a wordlist that integrates with HashCat")
parser.add_argument('-H', dest="hash_list_file", help='path to the file containing hashes to identify')
parser.add_argument('-pO', '--plain-output', dest="output_file", help='save all output to a file')
parser.add_argument('-g', '--group', dest="group",
                    help='group hash values and save them with names based on hashcat\'s hash modes',
                    action="store_true")

if __name__ == '__main__':
    args = parser.parse_args()

    output = None
    if args.output_file:
        output = open(args.output_file, 'w+')

    print(constants.WELCOME)
    print(constants.SOCIAL_INFO)
    print_to_file(constants.WELCOME, output)
    print_to_file(constants.SOCIAL_INFO, output)

    possible_hashes = {}

    for hash_value in parse_hash_list(args.hash_list_file):
        validated_algorithms = []

        for algorithm, hashcat_code in constants.ACTIVE_ALGORITHMS.items():
            instance = algorithm(hash_value)
            if instance.validate():
                possible_hashes.setdefault(hashcat_code, []).append(hash_value)
                validated_algorithms.append(algorithm.__name__)

        if validated_algorithms:
            info = "\n\n" + tabulate([
                [f"[+] {algorithm_name}"] for algorithm_name in validated_algorithms
            ], headers=[f"Possible algorithms for {hash_value}"])

            print(info)
            print_to_file(info, output)

    if possible_hashes:
        if args.group:
            hash_group_dirname = make_hash_groups_dir()

            for hash_group, hash_values in possible_hashes.items():
                write_hash_group_file(
                    hash_group_dirname=hash_group_dirname,
                    algorithm_hashcat_code=hash_group,
                    hash_values=hash_values
                )
    else:
        info = "\n\n[-] Sorry! No suitable match detected."
        print(info)
        print_to_file(info, output)

    info = "\n" + constants.GOOD_LUCK
    print(info)
    print()
    print_to_file(info, output)
    print_to_file("", output)

    if args.output_file:
        output.close()

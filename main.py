import argparse
from tabulate import tabulate

import constants
from helpers import parse_hash_list, make_hash_groups_dir, write_hash_group_file, print_to_file

parser = argparse.ArgumentParser(prog='hashhunter',
                                 description="Identify hashes from a wordlist that integrates with HashCat")
parser.add_argument('-H', dest="hash_list_file", help='path to the file containing hashes to identify')
parser.add_argument('-pO', '--plain-output', dest="output_file", help='save all output to a file')
parser.add_argument('-g', '--group', dest="group",
                    help='group hash values and save them with names based on hashcat\'s hash modes',
                    action="store_true")

if __name__ == '__main__':
    args = parser.parse_args()

    output = open(args.output_file, 'w+') if args.output_file else None

    print(constants.WELCOME)
    print(constants.SOCIAL_INFO)
    print_to_file(constants.WELCOME, output)
    print_to_file(constants.SOCIAL_INFO, output)

    for hash_value in parse_hash_list(args.hash_list_file):
        possible_hashes = {}

        for hashcat_code, algorithm in constants.ACTIVE_ALGORITHMS.items():
            instance = algorithm(hash_value)
            if instance.validate():
                possible_hashes.setdefault(hashcat_code, []).append(hash_value)

        if possible_hashes:
            sorted_algorithms = sorted(possible_hashes.keys())

            priority_algorithms = sorted_algorithms[:2]
            other_algorithms = sorted_algorithms[2:]

            info1 = "\n\n" + tabulate(
                [[f"[+] {constants.ACTIVE_ALGORITHMS[algorithm_code].ALGORITHM_NAME}"] for algorithm_code in
                 priority_algorithms], headers=[f"Possible algorithms for {hash_value}"])

            print(info1)
            print_to_file(info1, output)

            if other_algorithms:
                info2 = "\n\n" + tabulate(
                    [[f"[+] {constants.ACTIVE_ALGORITHMS[algorithm_code].ALGORITHM_NAME}"] for algorithm_code in
                     other_algorithms], headers=[f"Least possible algorithms for {hash_value}"])

                print(info2)
                print_to_file(info2, output)
        else:
            info = f"\n\n[-] Sorry! No suitable match detected for {hash_value}."
            print(info)
            print_to_file(info, output)

    if args.group:
        hash_group_dirname = make_hash_groups_dir()

        for hash_group, hash_values in possible_hashes.items():
            write_hash_group_file(
                hash_group_dirname=hash_group_dirname,
                algorithm_hashcat_code=hash_group,
                hash_values=hash_values
            )

    info = "\n" + constants.GOOD_LUCK
    print(info)
    print()
    print_to_file(info, output)
    print_to_file("", output)

    if output:
        output.close()

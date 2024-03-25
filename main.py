import argparse
from tabulate import tabulate

import constants
from helpers import parse_hash_list, make_hash_groups_dir, write_hash_group_file, print_to_file, colored_output

parser = argparse.ArgumentParser(prog='hashhunter',
                                 description="Identify hashes from a wordlist that integrates with HashCat")
parser.add_argument('-H', dest="hash_list_file", help='Path to the file containing hashes to identify', required=True)
parser.add_argument('-pO', '--plain-output', dest="output_file", help='Save all output to a file')
parser.add_argument('-g', '--group', dest="group",
                    help='Group hash values and save them with names based on HashCat\'s hash modes',
                    action="store_true")
parser.add_argument('-a', '--all', dest="all", help='Save both most and least hash groups', action="store_true")

if __name__ == '__main__':
    args = parser.parse_args()

    output = open(args.output_file, 'w+') if args.output_file else None

    print(colored_output(constants.WELCOME, 'green'))
    print(colored_output(constants.SOCIAL_INFO, 'yellow'))
    print_to_file(constants.WELCOME, output)
    print_to_file(constants.SOCIAL_INFO, output)

    possible_hashes = {}

    for hash_value in parse_hash_list(args.hash_list_file):
        for hashcat_code, algorithm in constants.ACTIVE_ALGORITHMS.items():
            instance = algorithm(hash_value)
            if instance.validate():
                possible_hashes.setdefault(hash_value, []).append(hashcat_code)
            else:
                possible_hashes.setdefault(hash_value, [])

    if possible_hashes:
        sorted_algorithms = sorted(possible_hashes.values())

        table = {}

        for hash_value, hashcat_codes in possible_hashes.items():
            sorted_hashcat_codes = sorted(hashcat_codes)

            table.setdefault('Hash Value', []).append(hash_value)
            table.setdefault('Most Possible', []).append(
                ", ".join(map(lambda code: constants.ACTIVE_ALGORITHMS[code].ALGORITHM_NAME,
                              sorted_hashcat_codes[:constants.MOST_POSSIBLE_LENGTH])))
            table.setdefault('Least Possible', []).append(
                ", ".join(map(lambda code: constants.ACTIVE_ALGORITHMS[code].ALGORITHM_NAME,
                              sorted_hashcat_codes[constants.MOST_POSSIBLE_LENGTH:])))

        info = "\n\n" + tabulate(table, headers="keys", tablefmt="fancy_grid")

        print(colored_output(info, 'green'))
        print_to_file(info, output)

    else:
        info = f"\n\n[-] Sorry! No suitable match detected."
        print(colored_output(info, 'red'))
        print_to_file(info, output)

    if args.group:
        hash_group_dirname = make_hash_groups_dir()

        for hash_value in parse_hash_list(args.hash_list_file):
            hashcat_codes = possible_hashes.get(hash_value, [])
            hashcat_codes_to_save = hashcat_codes[:len(hashcat_codes) if args.all else constants.MOST_POSSIBLE_LENGTH]

            for hashcat_code in hashcat_codes_to_save:
                write_hash_group_file(
                    hash_group_dirname=hash_group_dirname,
                    algorithm_hashcat_code=hashcat_code,
                    hash_values=[hash_value]
                )

    info = "\n" + constants.GOOD_LUCK
    print(colored_output(info, 'green'))
    print()
    print_to_file(info, output)
    print_to_file("", output)

    if output:
        output.close()

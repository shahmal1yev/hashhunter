import os
from datetime import datetime


def parse_hash_list(hash_list_file_path: str):
    with open(hash_list_file_path, 'r') as f:
        hash_list = f.read().splitlines()
    return hash_list


def make_hash_groups_dir():
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    hash_groups_dirname = f"hashes-{now}"
    os.makedirs(hash_groups_dirname, exist_ok=True)
    return hash_groups_dirname

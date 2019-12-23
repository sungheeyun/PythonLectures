from typing import Dict
import json
import os


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
DATA_DIR = os.path.join(ROOT_DIR, "data")


def get_square_dict(n: int, m: int) -> Dict[str, int]:
    res: Dict[str, int] = dict()
    for number in range(n, m + 1):
        res[str(number)] = number ** 2

    return res


if __name__ == "__main__":
    file_name_1: str = "number_square_pair_1.json"
    file_name_path_1: str = os.path.join(DATA_DIR, file_name_1)

    file_name_2: str = "number_square_pair_2.json"
    file_name_path_2: str = os.path.join(DATA_DIR, file_name_2)

    with open(file_name_path_1, "w") as fid:
        json.dump(get_square_dict(1, 100), fid, indent=2)

    with open(file_name_path_2, "w") as fid:
        json.dump(get_square_dict(101, 1000), fid, indent=2)

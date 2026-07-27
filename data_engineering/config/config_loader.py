from pathlib import Path

import yaml


BASE_PATH = Path(__file__).parent


def load_yaml(file_name: str):

    with open(
        BASE_PATH / file_name,
        "r",
        encoding="utf-8",
    ) as file:

        return yaml.safe_load(file)
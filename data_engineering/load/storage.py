from pathlib import Path


BASE_PATH = Path(__file__).parent.parent

OUTPUT = BASE_PATH / "storage"

BRONZE = OUTPUT / "bronze"

SILVER = OUTPUT / "silver"

GOLD = OUTPUT / "gold"


for folder in (

    OUTPUT,

    BRONZE,

    SILVER,

    GOLD,

):

    folder.mkdir(
        parents=True,
        exist_ok=True,
    )
from pathlib import Path

BASE = Path(__file__).parent

WAREHOUSE = BASE / "warehouse_data"

DIMENSION = WAREHOUSE / "dimensions"

FACT = WAREHOUSE / "facts"

for folder in (
    WAREHOUSE,
    DIMENSION,
    FACT,
):

    folder.mkdir(
        parents=True,
        exist_ok=True,
    )
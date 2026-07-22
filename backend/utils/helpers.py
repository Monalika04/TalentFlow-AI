from math import ceil


def calculate_total_pages(
    total_records: int,
    page_size: int,
) -> int:

    if total_records == 0:
        return 0

    return ceil(
        total_records / page_size
    )
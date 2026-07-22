import math


class Pagination:

    @staticmethod
    def build(
        page,
        page_size,
        total,
        data
    ):

        return {
            "page": page,
            "page_size": page_size,
            "total_records": total,
            "total_pages": (
                math.ceil(total / page_size)
                if total
                else 0
            ),
            "data": data
        }
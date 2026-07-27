import duckdb
import pandas as pd

from analytics.config import GOLD_PATH


class AnalyticsDatabase:

    def __init__(self):

        self.connection = duckdb.connect(
            database=":memory:"
        )

    def dataframe(
        self,
        query: str,
    ) -> pd.DataFrame:

        return self.connection.execute(
            query
        ).df()

    def execute(
        self,
        query: str,
    ):

        return self.connection.execute(
            query
        )

    @staticmethod
    def gold_table(
        table_name: str,
    ) -> str:

        return (
            f"read_parquet("
            f"'{GOLD_PATH}/{table_name}.parquet'"
            f")"
        )


db = AnalyticsDatabase()
import pandas as pd

from data_engineering.config.config_loader import (
    load_yaml,
)

from .warehouse_storage import (
    DIMENSION,
    FACT,
)


class WarehouseBuilder:

    def __init__(self):

        self.config = load_yaml(
            "warehouse_config.yaml"
        )

    def build_dimensions(
        self,
        datasets: dict,
    ):

        dimensions = {}

        for table, info in self.config[
            "dimensions"
        ].items():

            source = info["source"]

            columns = info["columns"]

            df = datasets[source][columns].copy()

            dimensions[table] = df

            df.to_parquet(
                DIMENSION / f"{table}.parquet",
                index=False,
            )

        return dimensions

    def build_facts(
        self,
        datasets: dict,
    ):

        facts = {}

        for table, info in self.config[
            "facts"
        ].items():

            source = info["source"]

            columns = info["columns"]

            df = datasets[source][columns].copy()

            facts[table] = df

            df.to_parquet(
                FACT / f"{table}.parquet",
                index=False,
            )

        return facts
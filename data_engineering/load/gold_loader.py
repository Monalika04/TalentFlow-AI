from .storage import GOLD


class GoldLoader:

    def load(
        self,
        tables,
    ):

        for name, dataframe in tables.items():

            path = GOLD / f"{name}.parquet"

            dataframe.to_parquet(

                path,

                index=False,

                engine="pyarrow",

            )

        print("Gold Layer Loaded")
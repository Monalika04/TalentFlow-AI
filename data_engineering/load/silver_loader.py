from .storage import SILVER


class SilverLoader:

    def load(
        self,
        tables,
    ):

        for name, dataframe in tables.items():

            path = SILVER / f"{name}.parquet"

            dataframe.to_parquet(

                path,

                index=False,

                engine="pyarrow",

            )

        print("Silver Layer Loaded")
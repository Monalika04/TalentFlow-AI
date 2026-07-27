from .storage import BRONZE


class BronzeLoader:

    def load(
        self,
        tables,
    ):

        for name, dataframe in tables.items():

            path = BRONZE / f"{name}.parquet"

            dataframe.to_parquet(

                path,

                index=False,

                engine="pyarrow",

            )

        print("Bronze Layer Loaded")
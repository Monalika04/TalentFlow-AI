from pathlib import Path

from .storage import GOLD

from data_engineering.gold.analytics_dashboard import (
    AnalyticsDashboardBuilder,
)


class GoldLoader:

    def load(
        self,
        tables,
    ):

        # -----------------------------------
        # Save Gold Parquet Files
        # -----------------------------------

        for name, dataframe in tables.items():

            path = GOLD / f"{name}.parquet"

            dataframe.to_parquet(

                path,

                index=False,

                engine="pyarrow",

            )

        print("Gold Layer Loaded")

        # -----------------------------------
        # Build Analytics Dashboard Dataset
        # -----------------------------------

        dashboard = AnalyticsDashboardBuilder().build(
            tables
        )

        dashboard_path = GOLD / "analytics_dashboard.parquet"

        dashboard.to_parquet(

            dashboard_path,

            index=False,

            engine="pyarrow",

        )

        print("Analytics Dashboard Dataset Created")
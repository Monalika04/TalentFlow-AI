import pandas as pd

from .base_transformer import BaseTransformer


class ApplicationTransformer(BaseTransformer):

    def transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        df = dataframe.copy()

        df["application_year"] = (
            df["application_date"].dt.year
        )

        df["application_month"] = (
            df["application_date"]
            .dt.month_name()
        )

        df["application_quarter"] = (
            "Q"
            + df["application_date"]
            .dt.quarter.astype(str)
        )

        df["application_age_days"] = (
            pd.Timestamp.now()
            - df["application_date"]
        ).dt.days

        return df
import pandas as pd

from .base_feature import BaseFeature


class CandidateFeatures(BaseFeature):

    def engineer(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        df = dataframe.copy()

        # Salary Difference

        df["salary_difference"] = (
            df["expected_ctc"]
            - df["current_ctc"]
        )

        # Salary Increase %

        df["salary_growth_percent"] = (
            (
                df["salary_difference"]
                /
                df["current_ctc"]
            )
            * 100
        ).round(2)

        return df
import pandas as pd

from data_engineering.config.config_loader import (
    load_yaml,
)

from .base_transformer import BaseTransformer


class CandidateTransformer(BaseTransformer):

    def __init__(self):

        self.rules = load_yaml(
            "candidate_rules.yaml"
        )

    def transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        df = dataframe.copy()

        # -----------------------------
        # Candidate Name
        # -----------------------------

        df["candidate_name"] = (
            df["first_name"].fillna("")
            + " "
            + df["last_name"].fillna("")
        ).str.strip()

        # -----------------------------
        # Experience Level
        # -----------------------------

        junior = self.rules["experience"]["junior_max"]

        mid = self.rules["experience"]["mid_max"]

        df["experience_level"] = "Senior"

        df.loc[
            df["total_experience"] < junior,
            "experience_level",
        ] = "Junior"

        df.loc[
            (
                df["total_experience"] >= junior
            )
            &
            (
                df["total_experience"] < mid
            ),
            "experience_level",
        ] = "Mid"

        # -----------------------------
        # Notice Period
        # -----------------------------

        immediate = self.rules[
            "notice_period"
        ]["immediate_max"]

        short = self.rules[
            "notice_period"
        ]["short_max"]

        df["notice_category"] = "Long"

        df.loc[
            df["notice_period_days"] <= immediate,
            "notice_category",
        ] = "Immediate"

        df.loc[
            (
                df["notice_period_days"] > immediate
            )
            &
            (
                df["notice_period_days"] <= short
            ),
            "notice_category",
        ] = "Short"

        # -----------------------------
        # Salary Band
        # -----------------------------

        low = self.rules[
            "salary_band"
        ]["low_max"]

        medium = self.rules[
            "salary_band"
        ]["medium_max"]

        df["salary_band"] = "High"

        df.loc[
            df["expected_ctc"] <= low,
            "salary_band",
        ] = "Low"

        df.loc[
            (
                df["expected_ctc"] > low
            )
            &
            (
                df["expected_ctc"] <= medium
            ),
            "salary_band",
        ] = "Medium"

        return df
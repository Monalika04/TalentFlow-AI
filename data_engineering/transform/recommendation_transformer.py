import pandas as pd

from data_engineering.config.config_loader import (
    load_yaml,
)

from .base_transformer import BaseTransformer


class RecommendationTransformer(
    BaseTransformer
):

    def __init__(self):

        self.rules = load_yaml(
            "recommendation_rules.yaml"
        )

    def transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        df = dataframe.copy()

        grades = self.rules["match_grade"]

        confidence = self.rules["confidence"]

        df["match_grade"] = "D"

        df.loc[
            df["overall_score"] >= grades["A"],
            "match_grade",
        ] = "A"

        df.loc[
            (
                df["overall_score"] >= grades["B"]
            )
            &
            (
                df["overall_score"] < grades["A"]
            ),
            "match_grade",
        ] = "B"

        df.loc[
            (
                df["overall_score"] >= grades["C"]
            )
            &
            (
                df["overall_score"] < grades["B"]
            ),
            "match_grade",
        ] = "C"

        df["confidence_level"] = "Low"

        df.loc[
            df["confidence_score"]
            >= confidence["High"],
            "confidence_level",
        ] = "High"

        df.loc[
            (
                df["confidence_score"]
                >= confidence["Medium"]
            )
            &
            (
                df["confidence_score"]
                < confidence["High"]
            ),
            "confidence_level",
        ] = "Medium"

        return df
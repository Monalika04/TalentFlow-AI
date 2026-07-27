import pandas as pd

from data_engineering.config.config_loader import (
    load_yaml,
)

from .base_feature import BaseFeature


class RecommendationFeatures(BaseFeature):

    def __init__(self):

        self.rules = load_yaml(
            "feature_rules.yaml"
        )

    def engineer(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        df = dataframe.copy()

        grade = self.rules["overall_grade"]

        priority = self.rules["hiring_priority"]

        df["overall_grade"] = "Needs Improvement"

        df.loc[
            df["overall_score"] >= grade["average"],
            "overall_grade",
        ] = "Average"

        df.loc[
            df["overall_score"] >= grade["good"],
            "overall_grade",
        ] = "Good"

        df.loc[
            df["overall_score"] >= grade["excellent"],
            "overall_grade",
        ] = "Excellent"

        df["hiring_priority"] = "Low"

        df.loc[
            df["overall_score"] >= priority["medium"],
            "hiring_priority",
        ] = "Medium"

        df.loc[
            df["overall_score"] >= priority["high"],
            "hiring_priority",
        ] = "High"

        return df
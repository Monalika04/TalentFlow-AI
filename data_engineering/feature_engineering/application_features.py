import pandas as pd

from data_engineering.config.config_loader import (
    load_yaml,
)

from .base_feature import BaseFeature


class ApplicationFeatures(BaseFeature):

    def __init__(self):

        self.rules = load_yaml(
            "feature_rules.yaml"
        )

    def engineer(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:

        df = dataframe.copy()

        fresh = self.rules[
            "application_age"
        ]["fresh"]

        recent = self.rules[
            "application_age"
        ]["recent"]

        df["application_bucket"] = "Old"

        df.loc[
            df["application_age_days"] <= fresh,
            "application_bucket",
        ] = "Fresh"

        df.loc[
            (
                df["application_age_days"] > fresh
            )
            &
            (
                df["application_age_days"] <= recent
            ),
            "application_bucket",
        ] = "Recent"

        return df
from .bronze_loader import BronzeLoader
from .silver_loader import SilverLoader
from .gold_loader import GoldLoader


class LoadPipeline:

    def __init__(self):

        self.bronze = BronzeLoader()

        self.silver = SilverLoader()

        self.gold = GoldLoader()

    def run(

        self,

        raw_data,

        transformed_data,

        feature_data,

    ):

        self.bronze.load(raw_data)

        self.silver.load(transformed_data)

        self.gold.load(feature_data)

        print()

        print("=" * 60)

        print("LOAD PIPELINE COMPLETED")

        print("=" * 60)
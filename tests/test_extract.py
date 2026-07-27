from data_engineering.extract.extract_pipeline import (
    ExtractPipeline,
)

pipeline = ExtractPipeline()

data = pipeline.run()

for name, dataframe in data.items():

    print("=" * 60)

    print(name.upper())

    print("=" * 60)

    print(dataframe.head())

    print()

    print(dataframe.info())
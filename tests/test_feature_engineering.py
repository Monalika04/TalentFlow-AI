from data_engineering.extract.extract_pipeline import (
    ExtractPipeline,
)

from data_engineering.transform.transform_pipeline import (
    TransformPipeline,
)

from data_engineering.feature_engineering.feature_pipeline import (
    FeaturePipeline,
)

raw = ExtractPipeline().run()

transformed = TransformPipeline().run(raw)

features = FeaturePipeline().run(
    transformed
)

for table, df in features.items():

    print("=" * 70)

    print(table.upper())

    print("=" * 70)

    print(df.head())

    print(df.columns.tolist())

    print()
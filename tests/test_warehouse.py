from data_engineering.extract.extract_pipeline import ExtractPipeline
from data_engineering.transform.transform_pipeline import TransformPipeline
from data_engineering.feature_engineering.feature_pipeline import FeaturePipeline
from data_engineering.warehouse.warehouse_pipeline import WarehousePipeline

raw = ExtractPipeline().run()

transformed = TransformPipeline().run(raw)

features = FeaturePipeline().run(
    transformed
)

warehouse = WarehousePipeline().run(
    features
)

print()

print("=" * 70)

print("DIMENSIONS")

print("=" * 70)

for name, df in warehouse["dimensions"].items():

    print(name)

    print(df.head())

    print()

print("=" * 70)

print("FACTS")

print("=" * 70)

for name, df in warehouse["facts"].items():

    print(name)

    print(df.head())

    print()
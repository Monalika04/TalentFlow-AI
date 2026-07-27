from data_engineering.extract.extract_pipeline import (
    ExtractPipeline,
)

from data_engineering.transform.transform_pipeline import (
    TransformPipeline,
)


extract = ExtractPipeline()

raw_data = extract.run()

transform = TransformPipeline()

transformed = transform.run(raw_data)

for table_name, dataframe in transformed.items():

    print("=" * 60)

    print(table_name.upper())

    print("=" * 60)

    print(dataframe.head())

    print()

    print(dataframe.columns.tolist())

    print()
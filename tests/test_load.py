from data_engineering.extract.extract_pipeline import ExtractPipeline
from data_engineering.transform.transform_pipeline import TransformPipeline
from data_engineering.feature_engineering.feature_pipeline import FeaturePipeline
from data_engineering.load.load_pipeline import LoadPipeline


raw = ExtractPipeline().run()

transformed = TransformPipeline().run(raw)

features = FeaturePipeline().run(transformed)

LoadPipeline().run(

    raw,

    transformed,

    features,

)
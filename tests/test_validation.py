from data_engineering.extract.extract_pipeline import (
    ExtractPipeline,
)

from data_engineering.validate.pipeline_validator import (
    PipelineValidator,
)

data = ExtractPipeline().run()

results = PipelineValidator().validate_candidates(
    data["candidates"]
)

for result in results:

    print(result)
import time

from data_engineering.extract.extract_pipeline import (
    ExtractPipeline,
)

from data_engineering.validate.pipeline_validator import (
    PipelineValidator,
)

from data_engineering.transform.transform_pipeline import (
    TransformPipeline,
)

from data_engineering.feature_engineering.feature_pipeline import (
    FeaturePipeline,
)

from data_engineering.load.load_pipeline import (
    LoadPipeline,
)

from data_engineering.warehouse.warehouse_pipeline import (
    WarehousePipeline,
)

from .base_stage import BaseStage
from .stage_result import StageResult


class ExtractStage(BaseStage):

    def execute(
        self,
        context,
    ):

        start = time.time()

        raw = ExtractPipeline().run()

        context["raw"] = raw

        return StageResult(

            name="Extract",

            status="SUCCESS",

            rows=len(raw["candidates"]),

            execution_time=round(
                time.time() - start,
                2,
            ),

            data=context,
        )
        
class ValidationStage(BaseStage):

    def execute(
        self,
        context,
    ):

        start = time.time()

        validator = PipelineValidator()

        validator.validate_candidates(

            context["raw"]["candidates"]

        )

        return StageResult(

            name="Validation",

            status="SUCCESS",

            rows=len(
                context["raw"]["candidates"]
            ),

            execution_time=round(
                time.time() - start,
                2,
            ),

            data=context,
        )
        
class TransformStage(BaseStage):

    def execute(
        self,
        context,
    ):

        start = time.time()

        transformed = (

            TransformPipeline()

            .run(

                context["raw"]

            )

        )

        context["transformed"] = transformed

        return StageResult(

            name="Transformation",

            status="SUCCESS",

            rows=len(
                transformed["candidates"]
            ),

            execution_time=round(
                time.time() - start,
                2,
            ),

            data=context,
        )
        
class FeatureStage(BaseStage):

    def execute(
        self,
        context,
    ):

        start = time.time()

        features = (

            FeaturePipeline()

            .run(

                context["transformed"]

            )

        )

        context["features"] = features

        return StageResult(

            name="Feature Engineering",

            status="SUCCESS",

            rows=len(
                features["candidates"]
            ),

            execution_time=round(
                time.time() - start,
                2,
            ),

            data=context,
        )

class LoadStage(BaseStage):

    def execute(
        self,
        context,
    ):

        start = time.time()

        LoadPipeline().run(

            context["raw"],

            context["transformed"],

            context["features"],

        )

        return StageResult(

            name="Load",

            status="SUCCESS",

            rows=len(
                context["features"]["candidates"]
            ),

            execution_time=round(
                time.time() - start,
                2,
            ),

            data=context,
        )

class WarehouseStage(BaseStage):

    def execute(
        self,
        context,
    ):

        start = time.time()

        warehouse = (

            WarehousePipeline()

            .run(

                context["features"]

            )

        )

        context["warehouse"] = warehouse

        return StageResult(

            name="Warehouse",

            status="SUCCESS",

            rows=len(
                context["features"]["candidates"]
            ),

            execution_time=round(
                time.time() - start,
                2,
            ),

            data=context,
        )


from .pipeline_steps import (
    ExtractStage,
    ValidationStage,
    TransformStage,
    FeatureStage,
    LoadStage,
    WarehouseStage,
)

from .logger import logger
from .report import PipelineReport


class TalentFlowPipeline:

    def __init__(self):

        self.report = PipelineReport()

        self.context = {}

        self.stages = [

            ExtractStage(),

            ValidationStage(),

            TransformStage(),

            FeatureStage(),

            LoadStage(),

            WarehouseStage(),

        ]

    def execute(self):

        print()

        print("=" * 70)

        print("TalentFlow AI Pipeline")

        print("=" * 70)

        for stage in self.stages:

            result = stage.execute(
                self.context
            )

            logger.info(
                f"{result.name} completed."
            )

            self.report.add_step(

                result.name,

                result.rows,

                result.status,

                result.execution_time,

            )

        self.report.save()

        print()

        print("=" * 70)

        print("PIPELINE COMPLETED")

        print("=" * 70)
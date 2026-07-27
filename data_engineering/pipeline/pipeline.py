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

from .logger import logger

from .report import PipelineReport


class TalentFlowPipeline:

    def __init__(self):

        self.report = PipelineReport()

    def execute(self):

        print()

        print("=" * 70)

        print("TalentFlow AI ETL Pipeline")

        print("=" * 70)

        # -------------------------
        # Extract
        # -------------------------

        start = time.time()

        raw = ExtractPipeline().run()

        elapsed = round(
            time.time() - start,
            2,
        )

        logger.info("Extract Completed")

        self.report.add_step(

            "Extract",

            len(raw["candidates"]),

            "SUCCESS",

            elapsed,

        )

        # -------------------------
        # Validation
        # -------------------------

        start = time.time()

        results = (

            PipelineValidator()

            .validate_candidates(

                raw["candidates"]

            )

        )

        elapsed = round(
            time.time() - start,
            2,
        )

        logger.info("Validation Completed")

        self.report.add_step(

            "Validation",

            len(raw["candidates"]),

            "SUCCESS",

            elapsed,

        )

        # -------------------------
        # Transform
        # -------------------------

        start = time.time()

        transformed = (

            TransformPipeline()

            .run(raw)

        )

        elapsed = round(
            time.time() - start,
            2,
        )

        logger.info("Transformation Completed")

        self.report.add_step(

            "Transformation",

            len(transformed["candidates"]),

            "SUCCESS",

            elapsed,

        )

        # -------------------------
        # Feature Engineering
        # -------------------------

        start = time.time()

        features = (

            FeaturePipeline()

            .run(

                transformed

            )

        )

        elapsed = round(
            time.time() - start,
            2,
        )

        logger.info("Feature Engineering Completed")

        self.report.add_step(

            "Feature Engineering",

            len(features["candidates"]),

            "SUCCESS",

            elapsed,

        )

        # -------------------------
        # Load
        # -------------------------

        start = time.time()

        LoadPipeline().run(

            raw,

            transformed,

            features,

        )

        elapsed = round(
            time.time() - start,
            2,
        )

        logger.info("Load Completed")

        self.report.add_step(

            "Load",

            len(features["candidates"]),

            "SUCCESS",

            elapsed,

        )

        # -------------------------
        # Warehouse
        # -------------------------

        start = time.time()

        WarehousePipeline().run(

            features

        )

        elapsed = round(
            time.time() - start,
            2,
        )

        logger.info("Warehouse Completed")

        self.report.add_step(

            "Warehouse",

            len(features["candidates"]),

            "SUCCESS",

            elapsed,

        )

        self.report.save()

        print()

        print("=" * 70)

        print("PIPELINE FINISHED SUCCESSFULLY")

        print("=" * 70)
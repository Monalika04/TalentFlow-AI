from .warehouse_builder import (
    WarehouseBuilder,
)


class WarehousePipeline:

    def __init__(self):

        self.builder = WarehouseBuilder()

    def run(
        self,
        feature_data,
    ):

        dimensions = (
            self.builder.build_dimensions(
                feature_data
            )
        )

        facts = (
            self.builder.build_facts(
                feature_data
            )
        )

        return {

            "dimensions": dimensions,

            "facts": facts,
        }
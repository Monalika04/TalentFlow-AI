from .candidate_transformer import (
    CandidateTransformer,
)

from .application_transformer import (
    ApplicationTransformer,
)

from .recommendation_transformer import (
    RecommendationTransformer,
)


class TransformPipeline:

    def __init__(self):

        self.candidate = CandidateTransformer()

        self.application = (
            ApplicationTransformer()
        )

        self.recommendation = (
            RecommendationTransformer()
        )

    def run(
        self,
        extracted_data: dict,
    ):

        return {

            "candidates":
                self.candidate.transform(
                    extracted_data["candidates"]
                ),
                
                "companies":
        extracted_data["companies"],

            "applications":
                self.application.transform(
                    extracted_data["applications"]
                ),

            "recommendations":
                self.recommendation.transform(
                    extracted_data["recommendations"]
                ),

            "jobs":
                extracted_data["jobs"],
        }
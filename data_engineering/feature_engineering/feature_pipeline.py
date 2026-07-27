from .candidate_features import CandidateFeatures
from .application_features import ApplicationFeatures
from .recommendation_features import RecommendationFeatures


class FeaturePipeline:

    def __init__(self):

        self.candidate = CandidateFeatures()

        self.application = ApplicationFeatures()

        self.recommendation = RecommendationFeatures()

    def run(
        self,
        transformed_data: dict,
    ):

        return {

            "candidates":
                self.candidate.engineer(
                    transformed_data["candidates"]
                ),
                
                "companies":
        transformed_data["companies"],

            "applications":
                self.application.engineer(
                    transformed_data["applications"]
                ),

            "recommendations":
                self.recommendation.engineer(
                    transformed_data["recommendations"]
                ),

            "jobs":
                transformed_data["jobs"],
        }
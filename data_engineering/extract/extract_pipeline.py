from backend.models.ai_recommendation import (
    AIRecommendation,
)
from backend.models.application import Application
from backend.models.candidate import Candidate
from backend.models.company import Company
from backend.models.job import Job

from .generic_extractor import GenericExtractor


class ExtractPipeline:

    def __init__(self):

        self.extractor = GenericExtractor()

    def run(self):

        return {

            "candidates":
                self.extractor.extract(Candidate),

            "companies":
                self.extractor.extract(Company),

            "jobs":
                self.extractor.extract(Job),

            "applications":
                self.extractor.extract(Application),

            "recommendations":
                self.extractor.extract(
                    AIRecommendation
                ),
        }
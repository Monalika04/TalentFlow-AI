from fastapi import HTTPException

from backend.repositories.application_repository import (
    ApplicationRepository,
)
from backend.schemas.candidate_ranking_schema import (
    CandidateRankingItem,
    CandidateRankingResponse,
)


class CandidateRankingService:

    def __init__(self, db):

        self.repository = ApplicationRepository(db)

    def get_job_ranking(
        self,
        job_id: int,
    ) -> CandidateRankingResponse:

        records = self.repository.get_ranking_by_job(
            job_id
        )

        if not records:

            raise HTTPException(
                status_code=404,
                detail="No ranked candidates found for this job.",
            )

        ranking = []

        rank = 1

        for (
            application,
            candidate,
            recommendation,
        ) in records:

            ranking.append(

                CandidateRankingItem(

                    rank=rank,

                    application_id=application.application_id,

                    candidate_id=candidate.candidate_id,

                    candidate_name=(
                        f"{candidate.first_name} "
                        f"{candidate.last_name}"
                    ).strip(),

                    overall_score=float(
                        recommendation.overall_score
                    ),

                    recommendation=(
                        recommendation.recommendation
                    ),
                )

            )

            rank += 1

        return CandidateRankingResponse(

            job_id=job_id,

            total_candidates=len(ranking),

            ranking=ranking,
        )
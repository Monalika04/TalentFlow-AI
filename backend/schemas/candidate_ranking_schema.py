from pydantic import BaseModel


class CandidateRankingItem(BaseModel):

    rank: int

    application_id: int

    candidate_id: int

    candidate_name: str

    overall_score: float

    recommendation: str


class CandidateRankingResponse(BaseModel):

    job_id: int

    total_candidates: int

    ranking: list[CandidateRankingItem]
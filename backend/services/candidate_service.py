import math

from fastapi import HTTPException

from backend.models.candidate import Candidate
from backend.repositories.candidate_repository import CandidateRepository
from backend.schemas.candidate_schema import CandidateListResponse


class CandidateService:

    def __init__(self, db):

        self.repository = CandidateRepository(db)

    def create_candidate(self, data):

        if self.repository.get_by_email(data.email):
            raise HTTPException(
                status_code=409,
                detail="Email already exists."
            )

        if self.repository.get_by_phone(data.phone):
            raise HTTPException(
                status_code=409,
                detail="Phone number already exists."
            )

        candidate = Candidate(**data.model_dump())

        return self.repository.create(candidate)

    def search_candidates(
        self,
        page,
        page_size,
        city,
        status,
        search
    ):

        total, candidates = self.repository.search(
            page,
            page_size,
            city,
            status,
            search
        )

        return CandidateListResponse(
            page=page,
            page_size=page_size,
            total_records=total,
            total_pages=math.ceil(total / page_size)
            if total else 0,
            data=candidates
        )
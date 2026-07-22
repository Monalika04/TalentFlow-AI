import math

from fastapi import HTTPException

from backend.models.candidate import Candidate
from backend.repositories.candidate_repository import CandidateRepository
from backend.schemas.candidate_schema import (
    CandidateListResponse,
    CandidateUpdate,
)


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

    def get_candidate_by_id(self, candidate_id: int):

        candidate = self.repository.get_by_id(candidate_id)

        if not candidate:
            raise HTTPException(
                status_code=404,
                detail="Candidate not found."
            )

        return candidate

    def update_candidate(
        self,
        candidate_id: int,
        data: CandidateUpdate
    ):

        candidate = self.repository.get_by_id(candidate_id)

        if not candidate:
            raise HTTPException(
                status_code=404,
                detail="Candidate not found."
            )

        email = self.repository.get_by_email(data.email)

        if (
            email
            and email.candidate_id != candidate_id
        ):
            raise HTTPException(
                status_code=409,
                detail="Email already exists."
            )

        phone = self.repository.get_by_phone(data.phone)

        if (
            phone
            and phone.candidate_id != candidate_id
        ):
            raise HTTPException(
                status_code=409,
                detail="Phone number already exists."
            )

        candidate.first_name = data.first_name
        candidate.last_name = data.last_name
        candidate.email = data.email
        candidate.phone = data.phone
        candidate.city = data.city
        candidate.state = data.state
        candidate.country = data.country
        candidate.total_experience = data.total_experience
        candidate.current_ctc = data.current_ctc
        candidate.expected_ctc = data.expected_ctc
        candidate.notice_period_days = data.notice_period_days
        candidate.highest_education = data.highest_education
        candidate.linkedin_url = data.linkedin_url
        candidate.github_url = data.github_url
        candidate.portfolio_url = data.portfolio_url
        candidate.status = data.status

        self.repository.update()

        return candidate

    def delete_candidate(self, candidate_id: int):

        candidate = self.repository.get_by_id(candidate_id)

        if not candidate:
            raise HTTPException(
                status_code=404,
                detail="Candidate not found."
            )

        candidate.status = "INACTIVE"

        self.repository.delete()

        return {
            "message": "Candidate deleted successfully."
        }
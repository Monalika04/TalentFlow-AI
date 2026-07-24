from sqlalchemy.orm import Session

from backend.models.education import Education
from backend.repositories.base_repository import BaseRepository


class EducationRepository(BaseRepository[Education]):
    def __init__(self, db: Session):
        super().__init__(db, Education)

    def get_by_candidate(self, candidate_id: int) -> list[Education]:
        return (
            self.db.query(Education)
            .filter(Education.candidate_id == candidate_id)
            .all()
        )

    def delete_by_candidate(self, candidate_id: int) -> None:

        (
            self.db.query(Education)
            .filter(Education.candidate_id == candidate_id)
            .delete(synchronize_session=False)
        )

        self.db.flush()
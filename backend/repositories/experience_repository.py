from sqlalchemy.orm import Session

from backend.models.experience import Experience
from backend.repositories.base_repository import BaseRepository


class ExperienceRepository(BaseRepository[Experience]):

    def __init__(self, db: Session):
        super().__init__(db, Experience)

    def get_by_candidate(self, candidate_id: int) -> list[Experience]:

        return (
            self.db.query(Experience)
            .filter(
                Experience.candidate_id == candidate_id
            )
            .all()
        )

    def delete_by_candidate(self, candidate_id: int) -> None:

        (
            self.db.query(Experience)
            .filter(
                Experience.candidate_id == candidate_id
            )
            .delete(synchronize_session=False)
        )

        self.db.flush()
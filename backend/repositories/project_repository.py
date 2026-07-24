from sqlalchemy.orm import Session

from backend.models.project import Project
from backend.repositories.base_repository import BaseRepository


class ProjectRepository(BaseRepository[Project]):
    def __init__(self, db: Session):
        super().__init__(db, Project)

    def get_by_candidate(self, candidate_id: int) -> list[Project]:
        return (
            self.db.query(Project)
            .filter(Project.candidate_id == candidate_id)
            .all()
        )

    def delete_by_candidate(self, candidate_id: int) -> None:

        (
            self.db.query(Project)
            .filter(Project.candidate_id == candidate_id)
            .delete(synchronize_session=False)
        )

        self.db.flush()
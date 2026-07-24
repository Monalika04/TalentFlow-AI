from sqlalchemy.orm import Session

from backend.models.certification import Certification
from backend.repositories.base_repository import BaseRepository


class CertificationRepository(BaseRepository[Certification]):

    def __init__(self, db: Session):
        super().__init__(db, Certification)

    def get_by_candidate(
        self,
        candidate_id: int,
    ) -> list[Certification]:

        return (
            self.db.query(Certification)
            .filter(
                Certification.candidate_id == candidate_id
            )
            .all()
        )

    def delete_by_candidate(
        self,
        candidate_id: int,
    ) -> None:

        (
            self.db.query(Certification)
            .filter(
                Certification.candidate_id == candidate_id
            )
            .delete(synchronize_session=False)
        )

        self.db.flush()
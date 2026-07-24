from sqlalchemy.orm import Session

from backend.models.language import Language
from backend.repositories.base_repository import BaseRepository


class LanguageRepository(BaseRepository[Language]):

    def __init__(self, db: Session):
        super().__init__(db, Language)

    def get_by_candidate(
        self,
        candidate_id: int,
    ) -> list[Language]:

        return (
            self.db.query(Language)
            .filter(
                Language.candidate_id == candidate_id
            )
            .all()
        )

    def delete_by_candidate(
        self,
        candidate_id: int,
    ) -> None:

        (
            self.db.query(Language)
            .filter(
                Language.candidate_id == candidate_id
            )
            .delete(synchronize_session=False)
        )

        self.db.flush()
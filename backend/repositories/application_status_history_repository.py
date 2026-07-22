from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.models.application_status_history import (
    ApplicationStatusHistory,
)


class ApplicationStatusHistoryRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        history: ApplicationStatusHistory,
    ):
        self.db.add(history)
        self.db.commit()
        self.db.refresh(history)

        return history

    def get_by_id(
        self,
        history_id: int,
    ):
        return (
            self.db.query(ApplicationStatusHistory)
            .filter(
                ApplicationStatusHistory.history_id == history_id
            )
            .first()
        )

    def search(
        self,
        page: int,
        page_size: int,
        application_id: int | None,
        new_status: str | None,
        changed_by: str | None,
    ):

        query = self.db.query(ApplicationStatusHistory)

        if application_id:
            query = query.filter(
                ApplicationStatusHistory.application_id == application_id
            )

        if new_status:
            query = query.filter(
                ApplicationStatusHistory.new_status == new_status
            )

        if changed_by:
            query = query.filter(
                ApplicationStatusHistory.changed_by == changed_by
            )

        total = query.with_entities(
            func.count(ApplicationStatusHistory.history_id)
        ).scalar()

        history = (
            query
            .order_by(
                ApplicationStatusHistory.changed_at.desc()
            )
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

        return total, history

    def update(self):
        self.db.commit()

    def delete(
        self,
        history: ApplicationStatusHistory,
    ):
        self.db.delete(history)
        self.db.commit()
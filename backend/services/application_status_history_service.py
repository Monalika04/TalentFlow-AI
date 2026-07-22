from math import ceil

from backend.models.application import Application
from backend.models.application_status_history import (
    ApplicationStatusHistory,
)
from backend.repositories.application_repository import (
    ApplicationRepository,
)
from backend.repositories.application_status_history_repository import (
    ApplicationStatusHistoryRepository,
)
from backend.schemas.application_status_history_schema import (
    ApplicationStatusHistoryCreate,
    ApplicationStatusHistoryUpdate,
    ApplicationStatusHistoryListResponse,
)


class ApplicationStatusHistoryService:

    def __init__(self, db):
        self.repository = ApplicationStatusHistoryRepository(db)
        self.application_repository = ApplicationRepository(db)

    def create(
        self,
        request: ApplicationStatusHistoryCreate,
    ):
        application = self.application_repository.get_by_id(
            request.application_id
        )

        if not application:
            raise ValueError("Application not found.")

        history = ApplicationStatusHistory(
            application_id=request.application_id,
            previous_status=request.previous_status,
            new_status=request.new_status,
            changed_by=request.changed_by,
            remarks=request.remarks,
        )

        return self.repository.create(history)

    def get_by_id(
        self,
        history_id: int,
    ):
        history = self.repository.get_by_id(history_id)

        if not history:
            raise ValueError("History record not found.")

        return history

    def search(
        self,
        page: int,
        page_size: int,
        application_id: int | None,
        new_status: str | None,
        changed_by: str | None,
    ):
        total, records = self.repository.search(
            page,
            page_size,
            application_id,
            new_status,
            changed_by,
        )

        return ApplicationStatusHistoryListResponse(
            page=page,
            page_size=page_size,
            total_records=total,
            total_pages=ceil(total / page_size) if total else 0,
            data=records,
        )

    def update(
        self,
        history_id: int,
        request: ApplicationStatusHistoryUpdate,
    ):
        history = self.repository.get_by_id(history_id)

        if not history:
            raise ValueError("History record not found.")

        history.changed_by = request.changed_by
        history.remarks = request.remarks

        self.repository.update()

        return history

    def delete(
        self,
        history_id: int,
    ):
        history = self.repository.get_by_id(history_id)

        if not history:
            raise ValueError("History record not found.")

        self.repository.delete(history)
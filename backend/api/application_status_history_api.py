from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from backend.dependencies.database import get_db
from backend.schemas.application_status_history_schema import (
    ApplicationStatusHistoryCreate,
    ApplicationStatusHistoryUpdate,
    ApplicationStatusHistoryResponse,
    ApplicationStatusHistoryListResponse,
)
from backend.services.application_status_history_service import (
    ApplicationStatusHistoryService,
)

router = APIRouter(
    prefix="/application-status-history",
    tags=["Application Status History"],
)


@router.post(
    "/",
    response_model=ApplicationStatusHistoryResponse,
)
def create_history(
    request: ApplicationStatusHistoryCreate,
    db: Session = Depends(get_db),
):
    try:
        service = ApplicationStatusHistoryService(db)
        return service.create(request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get(
    "/",
    response_model=ApplicationStatusHistoryListResponse,
)
def search_history(
    page: Annotated[int, Query(ge=1)] = 1,
    page_size: Annotated[int, Query(ge=1, le=100)] = 10,
    application_id: int | None = None,
    new_status: str | None = None,
    changed_by: str | None = None,
    db: Session = Depends(get_db),
):
    service = ApplicationStatusHistoryService(db)

    return service.search(
        page,
        page_size,
        application_id,
        new_status,
        changed_by,
    )


@router.get(
    "/{history_id}",
    response_model=ApplicationStatusHistoryResponse,
)
def get_history(
    history_id: int,
    db: Session = Depends(get_db),
):
    try:
        service = ApplicationStatusHistoryService(db)
        return service.get_by_id(history_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put(
    "/{history_id}",
    response_model=ApplicationStatusHistoryResponse,
)
def update_history(
    history_id: int,
    request: ApplicationStatusHistoryUpdate,
    db: Session = Depends(get_db),
):
    try:
        service = ApplicationStatusHistoryService(db)
        return service.update(history_id, request)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete(
    "/{history_id}",
)
def delete_history(
    history_id: int,
    db: Session = Depends(get_db),
):
    try:
        service = ApplicationStatusHistoryService(db)
        service.delete(history_id)

        return {
            "message": "History record deleted successfully."
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
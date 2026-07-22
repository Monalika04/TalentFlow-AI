from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from backend.schemas.company_schema import CompanyUpdate

from backend.config.database import SessionLocal
from backend.schemas.company_schema import (
    CompanyCreate,
    CompanyResponse
)
from backend.services.company_service import CompanyService

router = APIRouter(
    prefix="/companies",
    tags=["Companies"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "/",
    response_model=CompanyResponse,
    status_code=status.HTTP_201_CREATED
)
def create_company(
    company: CompanyCreate,
    db: Session = Depends(get_db)
):
    service = CompanyService(db)
    return service.create_company(company)


@router.get(
    "/",
    response_model=list[CompanyResponse]
)
def get_companies(
    db: Session = Depends(get_db)
):
    service = CompanyService(db)
    return service.get_all_companies()


@router.get(
    "/{company_id}",
    response_model=CompanyResponse
)
def get_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    service = CompanyService(db)
    return service.get_company_by_id(company_id)

@router.put(
    "/{company_id}",
    response_model=CompanyResponse
)
def update_company(
    company_id: int,
    company: CompanyUpdate,
    db: Session = Depends(get_db)
):

    service = CompanyService(db)

    return service.update_company(
        company_id,
        company
    )
    
    
@router.delete("/{company_id}")
def delete_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    service = CompanyService(db)
    return service.delete_company(company_id)
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.config.database import SessionLocal
from backend.schemas.company_schema import CompanyResponse
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


@router.get(
    "/",
    response_model=list[CompanyResponse]
)
def get_companies(
    db: Session = Depends(get_db)
):

    service = CompanyService(db)

    return service.get_all_companies()
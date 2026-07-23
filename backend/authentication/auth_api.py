from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.authentication.auth_schema import (
    LoginRequest,
    LoginResponse,
)
from backend.authentication.auth_service import AuthService
from backend.dependencies.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=LoginResponse,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):

    service = AuthService(db)

    try:
        return service.login(
            email=request.email,
            password=request.password,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e),
        )
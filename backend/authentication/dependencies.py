from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from backend.authentication.security import security
from backend.authentication.jwt_handler import decode_access_token
from backend.dependencies.database import get_db
from backend.repositories.recruiter_repository import RecruiterRepository


def get_current_recruiter(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    
    print(">>> ENTERED get_current_recruiter")
    print("Credentials:", credentials)
    token = credentials.credentials

    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

    recruiter_id = int(payload["sub"])

    recruiter = RecruiterRepository(db).get_by_id(recruiter_id)

    if recruiter is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Recruiter not found",
        )

    return recruiter
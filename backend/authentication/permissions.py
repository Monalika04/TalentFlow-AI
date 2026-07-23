from fastapi import Depends, HTTPException, status

from backend.authentication.dependencies import get_current_recruiter
from backend.models.recruiter_model import Recruiter


def require_admin(
    current_recruiter: Recruiter = Depends(get_current_recruiter),
):
    if current_recruiter.role != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only ADMIN can perform this action.",
        )

    return current_recruiter


def require_recruiter(
    current_recruiter: Recruiter = Depends(get_current_recruiter),
):
    if current_recruiter.role not in ["ADMIN", "RECRUITER"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access denied.",
        )

    return current_recruiter
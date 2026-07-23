from sqlalchemy.orm import Session

from backend.authentication.password import verify_password
from backend.authentication.jwt_handler import create_access_token
from backend.repositories.recruiter_repository import RecruiterRepository


class AuthService:

    def __init__(self, db: Session):
        self.repository = RecruiterRepository(db)

    def login(
        self,
        email: str,
        password: str,
    ):

        recruiter = self.repository.get_by_email(email)

        if recruiter is None:
            raise ValueError("Invalid email or password.")

        if not verify_password(
            password,
            recruiter.password_hash,
        ):
            raise ValueError("Invalid email or password.")

        token = create_access_token(
            recruiter_id=recruiter.recruiter_id,
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        }
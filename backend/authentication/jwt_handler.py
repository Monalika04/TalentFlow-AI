from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError

from backend.config.settings import settings

ALGORITHM = "HS256"


def create_access_token(
    recruiter_id: int,
    expires_minutes: int = 60,
):
    expire = datetime.utcnow() + timedelta(
        minutes=expires_minutes
    )

    payload = {
        "sub": str(recruiter_id),
        "exp": expire,
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=ALGORITHM,
    )


def decode_access_token(
    token: str,
):
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        return payload

    except JWTError:
        return None
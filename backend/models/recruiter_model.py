from datetime import datetime

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base


class Recruiter(Base):
    __tablename__ = "recruiter"
    __table_args__ = {"schema": "core"}

    recruiter_id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    company_id: Mapped[int] = mapped_column(
        ForeignKey("core.company.company_id"),
        nullable=False,
    )

    first_name: Mapped[str] = mapped_column(nullable=False)

    last_name: Mapped[str] = mapped_column(nullable=False)

    email: Mapped[str] = mapped_column(
        nullable=False,
        unique=True,
    )

    password_hash: Mapped[str] = mapped_column(
        nullable=False,
    )

    role: Mapped[str] = mapped_column(
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        nullable=False,
        default="ACTIVE",
    )

    last_login: Mapped[datetime | None] = mapped_column(
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
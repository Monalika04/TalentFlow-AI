from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base


class Candidate(Base):
    __tablename__ = "candidate"
    __table_args__ = {"schema": "core"}

    candidate_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    first_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    last_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False
    )

    city: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    years_experience: Mapped[float] = mapped_column(
        Numeric(4, 1),
        default=0
    )

    current_ctc: Mapped[float] = mapped_column(
        Numeric(10, 2),
        default=0
    )

    expected_ctc: Mapped[float] = mapped_column(
        Numeric(10, 2),
        default=0
    )

    linkedin_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    github_url: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="ACTIVE"
    )
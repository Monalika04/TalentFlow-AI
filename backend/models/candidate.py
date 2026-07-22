from decimal import Decimal

from sqlalchemy import Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base


class Candidate(Base):
    __tablename__ = "candidate"
    __table_args__ = {"schema": "core"}

    candidate_id: Mapped[int] = mapped_column(primary_key=True)

    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )

    phone: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        unique=True
    )

    city: Mapped[str] = mapped_column(String(100))
    state: Mapped[str] = mapped_column(String(100))
    country: Mapped[str] = mapped_column(String(100))

    total_experience: Mapped[Decimal] = mapped_column(
        Numeric(4, 1),
        default=0
    )

    current_ctc: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        default=0
    )

    expected_ctc: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        default=0
    )

    notice_period_days: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    highest_education: Mapped[str] = mapped_column(
        String(100)
    )

    linkedin_url: Mapped[str | None] = mapped_column(Text)

    github_url: Mapped[str | None] = mapped_column(Text)

    portfolio_url: Mapped[str | None] = mapped_column(Text)

    status: Mapped[str] = mapped_column(
        String(20),
        default="ACTIVE"
    )
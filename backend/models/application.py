from datetime import datetime
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base


class Application(Base):
    __tablename__ = "application"
    __table_args__ = {"schema": "core"}

    application_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    candidate_id: Mapped[int] = mapped_column(
        ForeignKey("core.candidate.candidate_id"),
        nullable=False,
    )

    job_id: Mapped[int] = mapped_column(
        ForeignKey("core.job.job_id"),
        nullable=False,
    )

    application_date: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False,
    )

    application_status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="APPLIED",
    )

    ai_match_score: Mapped[Decimal | None] = mapped_column(
        Numeric(5, 2),
        nullable=True,
    )

    recruiter_notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    source: Mapped[str | None] = mapped_column(
        String(50),
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
from datetime import date, datetime

from sqlalchemy import Boolean, Date, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base


class Experience(Base):
    __tablename__ = "experience"
    __table_args__ = {"schema": "core"}

    experience_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    candidate_id: Mapped[int] = mapped_column(
        ForeignKey("core.candidate.candidate_id"),
        nullable=False,
    )

    company_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    job_title: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    employment_type: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    location: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    end_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    currently_working: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
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
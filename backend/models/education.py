from datetime import datetime

from sqlalchemy import ForeignKey, Integer, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base


class Education(Base):
    __tablename__ = "education"
    __table_args__ = {"schema": "core"}

    education_id: Mapped[int] = mapped_column(primary_key=True)

    candidate_id: Mapped[int] = mapped_column(
        ForeignKey("core.candidate.candidate_id"),
        nullable=False,
    )

    degree: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    field_of_study: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    institution_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    board_or_university: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    grade_or_percentage: Mapped[float | None] = mapped_column(
        Numeric(5, 2),
        nullable=True,
    )

    start_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    end_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
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
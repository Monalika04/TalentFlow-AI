from datetime import date, datetime

from sqlalchemy import Date, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base


class Project(Base):
    __tablename__ = "project"
    __table_args__ = {"schema": "core"}

    project_id: Mapped[int] = mapped_column(primary_key=True)

    candidate_id: Mapped[int] = mapped_column(
        ForeignKey("core.candidate.candidate_id"),
        nullable=False,
    )

    project_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    technologies: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    github_url: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    live_url: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    start_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    end_date: Mapped[date | None] = mapped_column(
        Date,
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
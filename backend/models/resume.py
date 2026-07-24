from datetime import datetime
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base


class Resume(Base):
    __tablename__ = "resume"
    __table_args__ = {"schema": "core"}

    resume_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    candidate_id: Mapped[int] = mapped_column(
        ForeignKey("core.candidate.candidate_id"),
        nullable=False,
    )

    file_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    file_path: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    file_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    file_size_kb: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    resume_version: Mapped[int] = mapped_column(
        nullable=False,
        default=1,
    )

    upload_date: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False,
    )

    parsing_status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="PENDING",
    )

    ai_summary: Mapped[str | None] = mapped_column(
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
    
    
    ai_analyses: Mapped[list["ResumeAIAnalysis"]] = relationship(
    "ResumeAIAnalysis",
    back_populates="resume",
    cascade="all, delete-orphan",
    )
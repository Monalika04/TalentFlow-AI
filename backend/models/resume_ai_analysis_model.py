from datetime import datetime
from enum import Enum

from sqlalchemy import (
    DateTime,
    Enum as SQLEnum,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.models.base import Base


class AIAnalysisStatus(str, Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class ResumeAIAnalysis(Base):
    __tablename__ = "resume_ai_analysis"
    __table_args__ = {"schema": "core"}

    analysis_id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    resume_id: Mapped[int] = mapped_column(
        ForeignKey(
            "core.resume.resume_id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    model_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    prompt_version: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    analysis_version: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
    )

    status: Mapped[AIAnalysisStatus] = mapped_column(
        SQLEnum(AIAnalysisStatus),
        nullable=False,
        default=AIAnalysisStatus.PENDING,
    )

    raw_resume_text: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    ai_response_json: Mapped[dict | None] = mapped_column(
        JSONB,
        nullable=True,
    )

    error_message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    execution_time_ms: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    prompt_tokens: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    completion_tokens: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    total_tokens: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    resume: Mapped["Resume"] = relationship(
        "Resume",
        back_populates="ai_analyses",
    )
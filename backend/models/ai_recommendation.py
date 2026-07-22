from datetime import datetime
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base


class AIRecommendation(Base):
    __tablename__ = "ai_recommendation"
    __table_args__ = {"schema": "ai"}

    recommendation_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    application_id: Mapped[int] = mapped_column(
        ForeignKey("core.application.application_id"),
        nullable=False,
        unique=True,
    )

    overall_score: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        nullable=False,
    )

    skill_score: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        nullable=False,
    )

    experience_score: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        nullable=False,
    )

    education_score: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        nullable=False,
    )

    confidence_score: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        nullable=False,
    )

    missing_skills: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    strengths: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    recommendation: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    reasoning: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    model_version: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    generated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False,
    )
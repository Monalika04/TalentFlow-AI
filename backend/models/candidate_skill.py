from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import Boolean, Date, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base


class CandidateSkill(Base):
    __tablename__ = "candidate_skill"
    __table_args__ = {"schema": "core"}

    candidate_skill_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    candidate_id: Mapped[int] = mapped_column(
        ForeignKey("core.candidate.candidate_id"),
        nullable=False,
    )

    skill_id: Mapped[int] = mapped_column(
        ForeignKey("core.skill.skill_id"),
        nullable=False,
    )

    proficiency_level: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    years_experience: Mapped[Decimal] = mapped_column(
        Numeric(4, 1),
        nullable=False,
        default=0,
    )

    last_used: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    is_primary: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False,
    )
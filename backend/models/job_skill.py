from datetime import datetime

from sqlalchemy import Boolean, ForeignKey, Integer, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base


class JobSkill(Base):
    __tablename__ = "job_skill"
    __table_args__ = {"schema": "core"}

    job_skill_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    job_id: Mapped[int] = mapped_column(
        ForeignKey("core.job.job_id"),
        nullable=False,
    )

    skill_id: Mapped[int] = mapped_column(
        ForeignKey("core.skill.skill_id"),
        nullable=False,
    )

    importance_weight: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=3,
    )

    is_mandatory: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False,
    )
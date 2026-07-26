from datetime import datetime
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, String, Text, Integer, func
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from backend.models.base import Base


class Job(Base):
    __tablename__ = "job"
    __table_args__ = {"schema": "core"}

    job_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    company_id: Mapped[int] = mapped_column(
        ForeignKey("core.company.company_id"),
        nullable=False,
    )

    job_title: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    department: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    job_description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    location: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    employment_type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    min_experience: Mapped[Decimal] = mapped_column(
        Numeric(4, 1),
        nullable=False,
    )

    max_experience: Mapped[Decimal] = mapped_column(
        Numeric(4, 1),
        nullable=False,
    )

    min_salary: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    max_salary: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    vacancies: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="OPEN",
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
    
    ai_analyses: Mapped[list["JobAIAnalysis"]] = relationship(
        "JobAIAnalysis",
        back_populates="job",
        cascade="all, delete-orphan",
    )
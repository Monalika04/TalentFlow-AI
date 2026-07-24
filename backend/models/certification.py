from datetime import date, datetime

from sqlalchemy import Date, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base


class Certification(Base):
    __tablename__ = "certification"
    __table_args__ = {"schema": "core"}

    certification_id: Mapped[int] = mapped_column(primary_key=True)

    candidate_id: Mapped[int] = mapped_column(
        ForeignKey("core.candidate.candidate_id"),
        nullable=False,
    )

    certification_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    issuing_organization: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    issue_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    expiry_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True,
    )

    credential_id: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    credential_url: Mapped[str | None] = mapped_column(
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
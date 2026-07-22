from datetime import datetime

from sqlalchemy import ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base


class ApplicationStatusHistory(Base):
    __tablename__ = "application_status_history"
    __table_args__ = {"schema": "core"}

    history_id: Mapped[int] = mapped_column(
        primary_key=True
    )

    application_id: Mapped[int] = mapped_column(
        ForeignKey("core.application.application_id"),
        nullable=False,
    )

    previous_status: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    new_status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )

    changed_by: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    changed_at: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        nullable=False,
    )

    remarks: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base


class Company(Base):
    __tablename__ = "company"
    __table_args__ = {"schema": "core"}

    company_id: Mapped[int] = mapped_column(primary_key=True)

    company_name: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False
    )

    industry: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    company_size: Mapped[str | None] = mapped_column(
        String(30)
    )

    headquarters: Mapped[str | None] = mapped_column(
        String(100)
    )

    website: Mapped[str | None] = mapped_column(
        Text
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="ACTIVE"
    )
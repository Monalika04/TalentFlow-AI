from datetime import datetime

from sqlalchemy import String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base


class Skill(Base):
    __tablename__ = "skill"
    __table_args__ = {"schema": "core"}

    skill_id: Mapped[int] = mapped_column(primary_key=True)

    skill_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
    )

    category: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="ACTIVE",
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


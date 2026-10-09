from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.dialects.postgresql import JSONB, UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[UUID] = mapped_column(
        PGUUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    type: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    payload: Mapped[dict] = mapped_column(
        JSONB,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String,
        nullable=False,
        default="queued",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=datetime.utcnow,
    )

    user_id: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    retry_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )
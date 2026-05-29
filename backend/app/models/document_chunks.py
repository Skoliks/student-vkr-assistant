from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pgvector.sqlalchemy import Vector

from app.models.base import Base

if TYPE_CHECKING:
    from app.models.document import Document


class DocumentChunk(Base):
    __tablename__ = "document_chunks"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    document_id: Mapped[int] = mapped_column(
        ForeignKey("documents.id"), 
        index=True, 
        nullable=False
    )
    
    chunk_index: Mapped[int] = mapped_column(
        Integer, 
        nullable=False
    )
    chunk_text: Mapped[str] = mapped_column(Text, nullable=False)
    
    embeding: Mapped[list[float] | None] = mapped_column(Vector(384), nullable=True)
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.now(UTC), 
        nullable=False
    )
    
    document: Mapped["Document"] = relationship(
        "Document", 
        back_populates="chunks"
    )
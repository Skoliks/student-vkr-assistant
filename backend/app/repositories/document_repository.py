from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.document import Document
from app.schemas.document import DocumentCreate


class DocumentRepository:
    async def create(self, db: AsyncSession, data: DocumentCreate) -> Document:
        document = Document(**data.model_dump())
        
        db.add(document)
        await db.commit()
        await db.refresh(document)
        
        return document
    
    async def get_all(self, db: AsyncSession) -> list[Document]:
        stmt = select(Document)
        result = await db.execute(stmt)
        
        documents = result.scalars().all()
        
        return documents
    
    async def get_by_id(self, db: AsyncSession, document_id: int) -> Document | None:
        return await db.get(Document, document_id)
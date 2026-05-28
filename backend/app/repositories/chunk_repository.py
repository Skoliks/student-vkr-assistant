from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete, select

from app.models.document_chunks import DocumentChunk

class ChunkRepository:
    
    async def delete_by_document_id(self, db: AsyncSession, document_id: int) -> None:
        stmt = delete(DocumentChunk).where(DocumentChunk.document_id == document_id)
        
        await db.execute(stmt)
        await db.commit()
        
        
    async def create_many(self, db: AsyncSession, document_id: int, chunks: list[str]) -> list[DocumentChunk]:
        chunk_objects = [
            DocumentChunk(
                document_id=document_id,
                chunk_index=index,
                chunk_text=chunk_text,
            )
            for index, chunk_text in enumerate(chunks)
        ]
        
        db.add_all(chunk_objects)
        await db.commit()
        
        return chunk_objects
        
    
    async def get_by_document_id(self, db: AsyncSession, document_id: int) -> list[DocumentChunk]:
        stmt = (
            select(DocumentChunk)
            .where(DocumentChunk.document_id == document_id)
            .order_by(DocumentChunk.chunk_index)
        )
        
        result = await db.execute(stmt)
        
        return list(result.scalars().all())
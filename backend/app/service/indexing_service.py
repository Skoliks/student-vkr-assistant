from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.document_repository import DocumentRepository
from app.repositories.chunk_repository import ChunkRepository
from app.service.chunking_service import ChunkingService


class IndexingService:
    def __init__(self):
        self.document_repository = DocumentRepository()
        self.chunk_repository = ChunkRepository()
        self.chunking_service = ChunkingService()
        
        
    async def index_document(
        self,
        db: AsyncSession,
        document_id: int,
    ) -> int | None:
        
        document = await self.document_repository.get_by_id(db=db, document_id=document_id)
        
        if document is None:
            return None
        
        chunks = self.chunking_service.split_text(document.text)
        
        await self.chunk_repository.delete_by_document_id(db=db, document_id=document_id)
        
        created_chunks = await self.chunk_repository.create_many(db=db, document_id=document_id, chunks=chunks)
        
        return len(created_chunks)
    
indexing_service = IndexingService()
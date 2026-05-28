from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.document_repository import DocumentRepository
from app.schemas.document import DocumentCreate
from app.models.document import Document

class DocumentService:
    def __init__(self):
        self.repository = DocumentRepository()
        
    async def create_document(self, db: AsyncSession, data: DocumentCreate) -> Document:
        return await self.repository.create(db=db, data=data)
        
    async def get_documents(self, db: AsyncSession) -> list[Document]:
        return await self.repository.get_all(db=db)
    
    async def get_document_by_id(self, db: AsyncSession, document_id: int) -> Document | None:
        return await self.repository.get_by_id(db=db, document_id=document_id)
    
    
document_service = DocumentService()
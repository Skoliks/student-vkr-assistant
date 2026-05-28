from fastapi import HTTPException, Depends, status, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.service.document_service import document_service
from app.service.indexing_service import indexing_service
from app.core.database import get_db
from app.schemas.document import (
    DocumentCreate, 
    DocumentFullRead, 
    DocumentShortRead, 
    DocumentIndexResponse
)


router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("", response_model=DocumentShortRead, status_code=status.HTTP_201_CREATED)
async def create_document_route(data: DocumentCreate, db: AsyncSession = Depends(get_db)):
    return await document_service.create_document(db=db, data=data)


@router.get("", response_model=list[DocumentShortRead])
async def get_all_documents_route(db: AsyncSession = Depends(get_db)):
    return await document_service.get_documents(db=db)


@router.get("/{document_id}", response_model=DocumentFullRead)
async def get_document_by_id(document_id: int, db: AsyncSession = Depends(get_db)):
    document = await document_service.get_document_by_id(db=db, document_id=document_id)
    
    if document is None:
          raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Document not found"
    )

    return document

@router.post(
    "{document_id}/index", 
    response_model=DocumentIndexResponse, 
    status_code=status.HTTP_201_CREATED)
async def index_document_route(
    document_id: int, 
    db: AsyncSession = Depends(get_db)
):
    created_chunks = await indexing_service.index_document(db=db, document_id=document_id)
    
    if created_chunks is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Document not found"
    )
    
    return DocumentIndexResponse(
        document_id=document_id, 
        status="indexed", 
        chunks_created=created_chunks
    )
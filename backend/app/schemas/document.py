from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class DocumentCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    source: str = Field(min_length=1, max_length=500)
    text: str = Field(min_length=1)
    

class DocumentShortRead(BaseModel):
    id: int
    title: str 
    source: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
    

class DocumentFullRead(BaseModel):
    id: int
    title: str 
    text: str
    source: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
from fastapi import FastAPI
import app.models

from app.api.health import router as health_router
from app.api.document import router as document_router
from app.core.config import settings

app = FastAPI(
    title="student-vkr-assistant",
    version="0.1.0",
    debug=settings.debug
)

app.include_router(health_router)
app.include_router(document_router)

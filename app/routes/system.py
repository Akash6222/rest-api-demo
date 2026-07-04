from fastapi import APIRouter
from app.config import settings

router = APIRouter(tags=["System"])

@router.get("/")
def get_root():
    """Returns API information."""
    return {
        "name": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "description": "A production-ready REST API demo using FastAPI",
        "docs_url": "/docs"
    }

@router.get("/health")
def get_health():
    """Health check endpoint."""
    return {"status": "healthy"}

@router.get("/version")
def get_version():
    """Returns the API version."""
    return {"version": settings.PROJECT_VERSION}

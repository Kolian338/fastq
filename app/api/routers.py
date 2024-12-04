from fastapi import APIRouter

from app.api.endpoints import project_router

v1_router = APIRouter()

v1_router.include_router(
    project_router,
    prefix='/project',
    tags=['Проекты'],
)

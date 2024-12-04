from fastapi import APIRouter, Body

from app.schemas.project import (CreateProjectCreate)

project_router = APIRouter()


@project_router.get(
    '/'
)
async def get_all_projects():
    return {'project_name': 'Need to do this'}


@project_router.post(
    '/',
    summary='Создать проект',
    description=(
        'Этот метод используется для создания нового проекта через API.'
    )
)
async def create_project(
    project: CreateProjectCreate = Body(
        openapi_examples=CreateProjectCreate.model_config["json_schema_extra"]
    )
):
    return {"message": project}

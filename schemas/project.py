from pydantic import (Field, field_validator, model_validator)
from enums.project import AccessLevel

from schemas.base import MyBaseModel


class CreateProjectCreate(MyBaseModel):
    title: str = Field(
        ...,
        description="Название проекта.")
    code: str = Field(
        ...,
        description=(
            "Код проекта. Уникальный для команды."
            "Цифры и специальные символы не допускаются."
        )
    )
    description: str = Field(
        None,
        description="Описание проекта"
    )
    access: AccessLevel = Field(
        None,
        description="Уровень доступа ('all' или 'group')",
    )
    group: list[int] = Field(
        None,
        description=(
            "Список идентификаторов групп пользователей,"
            " необходима, если уровень доступа - 'группа'")
    )

    @field_validator('title')
    def string_not_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError('Строка не должна быть пустой')
        return value

    @model_validator(mode='before')
    def check_group_access(cls, values):
        """Проверка, если доступ 'group', то group не может быть None."""
        access = values.get("access")
        group = values.get("group")

        if access == AccessLevel.group and not group:
            raise ValueError(
                "Если доступ 'group', то group не может быть None.")

        return values

    model_config = {
        "json_schema_extra": {
            "Только с обязательными полями": {
                "summary": "Обязательный набор",
                "description": "Только обязательные поля.",
                "value": {
                    "title": "Basic Project",
                    "code": "BP",
                    "description": None,
                    "access": "all",
                    "group": None,
                },
            },
            "Со всеми полями": {
                "summary": "Все поля",
                "description": "Отображены все поля.",
                "value": {
                    "title": "Detailed Project",
                    "code": "DP",
                    "description": "This is a detailed example project.",
                    "access": "group",
                    "group": [1, 2, 3],
                },
            },
        },
    }

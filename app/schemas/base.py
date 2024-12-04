from pydantic import (BaseModel, ConfigDict)


class MyBaseModel(BaseModel):
    """Кастомный базовый класс Pydantic."""
    model_config = ConfigDict(extra='allow',)

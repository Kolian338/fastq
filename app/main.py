import uvicorn
from fastapi import FastAPI

from app.api.routers import v1_router

app = FastAPI(
    title='FastQ тест-менеджмент система.',
    description='Тестируй быстро, работай качественно.',
    docs_url='/swagger',
)

# Подключаем роутер.
app.include_router(v1_router, prefix='/v1')

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)

from fastapi import FastAPI
from .routers import elasticRouter

app = FastAPI()
app.include_router(elasticRouter.router)
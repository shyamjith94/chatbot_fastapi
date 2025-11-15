from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from src.core import settings
from src.api.routes import blog_route
import os

app = FastAPI(
    description="Blog generation system based on topic",
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/read-doc",
)

os.environ["LANGCHAIN_PROJECT"] = settings.LANGCHAIN_PROJECT
os.environ["LANGCHAIN_API_KEY"] = settings.LANGCHAIN_API_KEY


@app.get("/")
def home():
    return JSONResponse(content="Welcome AI blog generation", status_code=200)

app.include_router(router=blog_route, prefix=settings.API_TAG_V1, tags=["blog"])



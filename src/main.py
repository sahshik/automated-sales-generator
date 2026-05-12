from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(
    title="Sales Proposal AI",
    version="1.0.0"
)

app.include_router(router)
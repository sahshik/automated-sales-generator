from fastapi import APIRouter

from src.api.routes.health import router as health_router
from src.api.routes.customer import router as customer_router
from src.api.routes.upload import router as upload_router

router = APIRouter()

router.include_router(health_router)

router.include_router(customer_router)

router.include_router(upload_router)
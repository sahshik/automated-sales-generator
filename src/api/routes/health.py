from fastapi import APIRouter
from src.db.redis_client import r

router = APIRouter()

@router.get("/")
def read_root():

    return {
        "message": "Sales Proposal AI Running"
    }

@router.get("/cache")
def cache_test():

    r.set("test_key", "Hello Redis")

    value = r.get("test_key")

    return {
        "cached_value": value
    }
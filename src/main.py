from fastapi import FastAPI
from src.redis_client import r

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Running"}

@app.get("/cache")
def cache_test():
    r.set("test_key", "Hello Redis")
    value = r.get("test_key")
    return {"cached_value": value}
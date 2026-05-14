from fastapi import APIRouter, UploadFile, File
from src.db.redis_client import r

import uuid
import os

router = APIRouter()

RAW_DIR = "data/raw"

os.makedirs(RAW_DIR, exist_ok=True)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    if not file.filename.endswith(".pdf"):

        return {
            "error": "Only PDF files allowed"
        }

    file_id = str(uuid.uuid4())

    file_path = f"{RAW_DIR}/{file_id}_{file.filename}"

    with open(file_path, "wb") as f:

        content = await file.read()

        f.write(content)

    r.lpush("parsing_queue", file_path)

    return {
        "message": "File uploaded successfully",
        "file_id": file_id,
        "file_path": file_path
    }
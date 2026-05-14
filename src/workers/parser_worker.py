import time

from src.db.redis_client import r

print("Worker started...")

while True:

    task = r.rpop("parsing_queue")

    if task:

        print(f"Processing file: {task}")

    time.sleep(1)
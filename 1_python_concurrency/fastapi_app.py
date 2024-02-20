import asyncio
import argparse
from fastapi import FastAPI
import time
import uvicorn

app = FastAPI(docs_url="/swagger")


@app.get("/health_check")
async def health_check():
    return {"message": "OK"}


@app.get("/sleep")
async def async_sleep():
    start_time = time.time()
    await asyncio.sleep(1)
    end_time = time.time()
    return dict(msg=f"elapsed_time: {end_time - start_time}")


@app.get("/count")
async def count_50_million():
    start_time = time.time()
    for _ in range(50000000):
        pass
    end_time = time.time()
    return dict(msg=f"elapsed_time: {end_time - start_time}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=1)
    args = parser.parse_args()

    uvicorn.run(app="fastapi_app:app", host="0.0.0.0", port=8000, workers=args.workers)

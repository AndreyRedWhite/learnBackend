import sys
from pathlib import Path

from fastapi import FastAPI
import uvicorn

sys.path.append(str(Path(__file__).parent.parent))

from src.api.hotels import router as hotels_r

app = FastAPI()
app.include_router(router=hotels_r)


@app.get("/")
def root():
    return "hello word"


import time
import asyncio


@app.get(path='/sync/{proc_id}')
def get_sync(proc_id: int):
    print(f"started working with: {proc_id}. time is: {time.time():.2f}")
    time.sleep(2)
    print(f'finished working with {proc_id}. time is: {time.time():.2f}')


@app.get(path='/async/{proc_id}')
async def get_sync(proc_id: int):
    print(f"started working with: {proc_id}. time is: {time.time():.2f}")
    await asyncio.sleep(2)
    print(f'finished working with {proc_id}. time is: {time.time():.2f}')


def main():
    uvicorn.run("main:app", reload=True)


if __name__ == '__main__':
    main()

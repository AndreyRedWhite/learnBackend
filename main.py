from fastapi import FastAPI
import uvicorn

from hotels import router as hotels_r

app = FastAPI()
app.include_router(router=hotels_r)


hotels = [
    {"id": 1, "title": "sochi", "name": "Sochi_Star"},
    {"id": 2, "title": "dubai", "name": "Dubai_parus"}
]


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
    uvicorn.run("main:app", reload=False)


if __name__ == '__main__':
    main()
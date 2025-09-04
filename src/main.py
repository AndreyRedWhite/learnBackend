import sys
from pathlib import Path

from fastapi import FastAPI
import uvicorn

sys.path.append(str(Path(__file__).parent.parent))

from src.api.hotels import router as hotels_r
from src.settings import settings

app = FastAPI()
app.include_router(router=hotels_r)


@app.get("/")
def root():
    return "hello word"


def main():
    uvicorn.run("main:app", reload=True)


if __name__ == '__main__':
    main()

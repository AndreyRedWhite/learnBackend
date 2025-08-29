from fastapi import FastAPI, Body, Query
import uvicorn

from todos import router as todos_r

app = FastAPI()
app.include_router(router=todos_r)


def main():
    uvicorn.run('main:app', workers=4, reload=True)


if __name__ == '__main__':
    main()

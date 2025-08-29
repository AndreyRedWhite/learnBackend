from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/')
def main_route():
    return 'hello word'


@app.get('/health')
def get_health():
    return {"status":"ok"}


@app.get('/echo')
def get_echo(name: str):
    return {"you_said": name}


def main():
    uvicorn.run("main:app", reload=True)


if __name__ == '__main__':
    main()

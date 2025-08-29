Цель: практиковать Pydantic-схемы (v2), body/response-модели и простейшее состояние в памяти.
Критерии готовности:

POST /todos (title:str, done:bool=false) → объект с id:int

GET /todos → список

GET /todos/{id} / PUT /todos/{id} / DELETE /todos/{id}

404 для несуществующих id
Самопроверка:

curl -s -X POST http://127.0.0.1:8000/todos -H "Content-Type: application/json" -d '{"title":"learn FastAPI"}'
curl -s http://127.0.0.1:8000/todos
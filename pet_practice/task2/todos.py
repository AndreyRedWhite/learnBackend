from fastapi import Body, APIRouter
from schemas import ToDoItemSchema


router = APIRouter(prefix='/todos')


todos = [
    {'id': 1, 'title': 'task_1', 'done': True},
    {'id': 2, 'title': 'task_2', 'done': True},
]


@router.get('/todos')
def get_todo_list():
    return {'todo_items': todos}


@router.post(path='/todos')
def post_todo_list(data: ToDoItemSchema = Body()):
    global todos
    if not len(todos):
        id = 1
    else:
        id = todos[-1]['id'] + 1
    new_todo = {'id': id, 'title': data.title, 'done': data.done}
    todos.append(new_todo)
    return {'Ok'}


@router.get('/todos/{id}')
def get_todo_item(id: int):
    global todos
    try:
        todo_item = todos[id - 1]
        return todo_item
    except ValueError:
        return 'wrong ID'


@router.put('/todos/{id}')
def put_todo_item(id: int, data: ToDoItemSchema = Body()):
    global todos
    todos[id-1] = {"id": id, 'title': data.title, 'done': data.done}
    return {'Ok'}


@router.delete('/todos/{id}')
def del_todo_item(id: int):
    global todos
    todos = [item for item in todos if item['id'] != id]
    return {'Ok'}
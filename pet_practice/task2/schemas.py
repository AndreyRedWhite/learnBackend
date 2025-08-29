from pydantic import BaseModel


class ToDoItemSchema(BaseModel):
    title: str
    done: bool = False

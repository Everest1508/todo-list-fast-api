from fastapi import APIRouter

todo_router = APIRouter(prefix="/api/todo",tags=["Todo"])

@todo_router.get("/")
def list_todos():
    return {"msg":'list'}

@todo_router.post("/")
def create_todos():
    return {"msg":'list'}

@todo_router.put("/{key}")
def update_todos(key: int):
    return {"msg":f'list {key}'}

@todo_router.delete("/{key}")
def delete_todos(key: int):
    return {"msg":key}
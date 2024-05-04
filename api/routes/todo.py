from fastapi import APIRouter, HTTPException, status
from api.models.todo import Todo
from api.schemas.todo import PostTodo, GetTodo, PutTodo

todo_router = APIRouter(prefix="/api/todo", tags=["Todo"])


@todo_router.get("/")
async def list_todos():
    todos = Todo.all()
    print(todos)
    return await GetTodo.from_queryset(todos)

@todo_router.post("/")
async def create_todos(body: PostTodo):
    todo = await Todo.create(**body.dict())
    return await GetTodo.from_tortoise_orm(todo)

@todo_router.put("/{key}")
async def update_todos(key: int, body: PutTodo):
    todo = await Todo.filter(id=key).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    await todo.update_from_dict(body.dict(exclude_unset=True))
    await todo.save()
    return await GetTodo.from_tortoise_orm(todo)


@todo_router.delete("/{key}")
async def delete_todos(key: int):
    deleted_count = await Todo.filter(id=key).delete()
    if not deleted_count:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return {"msg": "Todo Deleted Successfully"}
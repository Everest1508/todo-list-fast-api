from fastapi import APIRouter, HTTPException, status, Depends
from api.models.todo import Todo
from api.models.user import User
from api.schemas.todo import PostTodo, GetTodo, PutTodo
from api.schemas.user import UserResponse  
from api.utils.authentications import get_current_user  

todo_router = APIRouter(prefix="/api/todo", tags=["Todo"])


@todo_router.get("/")
async def list_todos(current_user: User = Depends(get_current_user)):
    todos = Todo.filter(user=current_user).all()
    return await GetTodo.from_queryset(todos)


@todo_router.post("/")
async def create_todos(body: PostTodo, current_user: User = Depends(get_current_user)):
    todo = await Todo.create(user=current_user, **body.dict()) 
    return await GetTodo.from_tortoise_orm(todo)


@todo_router.put("/{key}")
async def update_todos(key: int, body: PutTodo, current_user: User = Depends(get_current_user)):
    todo = await Todo.filter(id=key, user=current_user).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    await todo.update_from_dict(body.dict(exclude_unset=True))
    await todo.save()
    return await GetTodo.from_tortoise_orm(todo)


@todo_router.delete("/{key}")
async def delete_todos(key: int, current_user: User = Depends(get_current_user)):
    deleted_count = await Todo.filter(id=key, user=current_user).delete() 
    if not deleted_count:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")
    return {"msg": "Todo Deleted Successfully"}

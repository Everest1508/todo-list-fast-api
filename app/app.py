from fastapi import FastAPI
from api.routes.todo import todo_router
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()
app.include_router(todo_router)
register_tortoise(
    app=app,
    db_url = "mysql://root:@localhost:3306/todo-list",
    modules={"models": ["api.models.todo"]},
    add_exception_handlers=True,
    generate_schemas=True,
)

@app.get("/")
def index():
    return {'msg':'API started'}
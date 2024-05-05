from fastapi import FastAPI
from api.routes.todo import todo_router
from api.routes.user import auth_router
from tortoise.contrib.fastapi import register_tortoise
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()
app.include_router(todo_router)
app.include_router(auth_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)
register_tortoise(
    app=app,
    db_url = os.getenv('DB_URL'),
    modules={"models": ["api.models.todo","api.models.user"]},
    add_exception_handlers=True,
    generate_schemas=True,
)

@app.get("/")
def index():
    return {'msg':'API started'}
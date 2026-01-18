import os
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

DB_PATH = os.getenv("DATABASE", "./database.txt")

class Todo(BaseModel):
    title: str

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/todos")
def create_list(todo: Todo):
    with open(DB_PATH, "a") as f:
        f.write(f"{todo.title}\n")
    return {"detail": "message written"}

@app.get("/todos")
def get_todos():
    try:
        with open(DB_PATH, "r") as f:
            todos = [line.strip() for line in f.readlines()]
            return todos
    except FileNotFoundError:
        return []

@app.delete("/todos/{todo_name}")
def delete_todo(todo_name: str):
    try:
        with open(DB_PATH, "r") as f:
            lines = f.readlines()
        
        with open(DB_PATH, "w") as f:
            for line in lines:
                if line.strip("\n") != todo_name:
                    f.write(line)
        
        return {"detail": "Deleted successfully"}
    except FileNotFoundError:
        return {"detail": "File not found"}
    
# Serve the HTML file at the root
@app.get("/")
async def get_index():
    return FileResponse("index.html")
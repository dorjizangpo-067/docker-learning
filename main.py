from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware # 1. Import this

class Todo(BaseModel):
    title: str

app = FastAPI()
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware # 1. Import this

class Todo(BaseModel):
    title: str

app = FastAPI()

# 2. Add this block to allow your local file to talk to the server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins (including 'null')
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/todos")
def create_list(todo: Todo): # Changed from str to Todo model
    with open("./database.txt", "a") as f:
        f.write(f"{todo.title}\n")
    return {"detail": "message written"}

@app.get("/todos")
def get_todos():
    try:
        with open("./database.txt", "r") as f:
            todos = [line.strip() for line in f.readlines()]
            return todos
    except FileNotFoundError:
        return []

@app.delete("/todos/{todo_name}")
def delete_todo(todo_name: str):
    try:
        with open("./database.txt", "r") as f:
            lines = f.readlines()
        
        # Keep everything except the one we want to delete
        with open("./database.txt", "w") as f:
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
###🐳 Docker Learning: FastAPI Todo App
A simple, containerized Todo application built with FastAPI and Python. This project serves as a hands-on guide to learning Docker fundamentals, including Image building, Port Mapping, and Data Persistence using Named Volumes.

🚀 Project Overview
This app allows users to create, view, and delete "Todos." The data is stored in a database.txt file. By dockerizing this app, we ensure that the environment is consistent regardless of where it is run.

Features:
FastAPI Backend: High-performance Python API.

Static Frontend: Simple index.html served at the root.

Dockerized: Fully portable using python:3.12-alpine.

Persistent Storage: Uses Docker volumes to keep data safe after container restarts.

🛠️ Tech Stack
Language: Python 3.12

Framework: FastAPI

Web Server: Uvicorn

Containerization: Docker (Alpine Linux)

📦 Getting Started
1. Prerequisites
Ensure you have Docker installed on your machine.

2. Build the Docker Image
Navigate to the project directory and run:

Bash
docker build -t fastapi-todo .
3. Run the Container (With Data Persistence)
To ensure your todos aren't lost when the container stops, we use a Named Volume:

Bash
# Create the volume
docker volume create todo_storage

# Run the container
docker run -d \
  -p 8000:5000 \
  -v todo_storage:/data \
  --name my-todo-app \
  fastapi-todo
🔍 Understanding the Setup
Port Mapping (-p 8000:5000)
8000 (Host): The port you access in your browser (http://localhost:8000).

5000 (Container): The port the app is actually listening on inside the Docker container (defined by the ENV PORT variable).

Volume Mapping (-v todo_storage:/data)
todo_storage: A Docker-managed volume that survives container deletion.

:/data: The internal path where our app looks for database.txt.

🖼️ Application Preview
Output Screenshot
Add a screenshot of your browser running the app at localhost:8000 here.

📹 Demo Clip
Final Working Demo:

[!TIP] Replace the placeholder below with a GIF or a link to your screen recording.

📂 Project Structure
Plaintext
.
├── main.py            # FastAPI Application
├── index.html         # Frontend interface
├── Dockerfile         # Container configuration
├── requirements.txt   # Python dependencies
└── database.txt       # Local DB (Only used if not using volumes)
📜 License
MIT - Feel free to use this for your own learning!

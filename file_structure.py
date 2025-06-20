import os

base_path = "to-do-fastapi"

folders = [
    "app/api",
    "app/schemas",
    "app/models",
    "app/db",
    "app/services",
    "app/core",
    "app/templates"
]

files = [
    "app/api/auth.py",
    "app/api/user.py",
    "app/api/todo.py",
    "app/api/__init__.py",
    
    "app/schemas/auth.py",
    "app/schemas/user.py",
    "app/schemas/todo.py",
    "app/schemas/__init__.py",
    
    "app/models/base.py",
    "app/models/user.py",
    "app/models/todo.py",
    "app/models/__init__.py",
    
    "app/db/database.py",
    "app/db/__init__.py",
    
    "app/services/auth.py",
    "app/services/user.py",
    "app/services/todo.py",
    "app/services/utils.py",
    "app/services/email.py",
    "app/services/__init__.py",
    
    "app/core/middleware.py",
    "app/core/__init__.py",
    
    "app/templates/.gitkeep",  # placeholder file
    
    "app/main.py",
    "app/settings.py",
    
    "runserver.py",
    "Dockerfile",
    "docker-compose.yml",
    "requirements.txt",
    ".env"
]

# Create folders
for folder in folders:
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

# Create files with a simple placeholder comment
for file in files:
    file_path = os.path.join(base_path, file)
    with open(file_path, 'w') as f:
        if file.endswith(".py"):
            f.write(f"# {os.path.basename(file)}\n")
        elif file.endswith(".env"):
            f.write("# Example: DB_URL=postgresql://user:pass@db:5432/todo_db\n")
        else:
            f.write("")

print(f"Project structure for '{base_path}' has been created successfully.")

# main.py
from fastapi import FastAPI
from app.api import api_router


app = FastAPI(title="TO-DO FASTAPI")

# define the routers
app.include_router(api_router, prefix="/api")


@app.on_event("startup")
async def startup():
    print("STARTING THE APP in http://127.0.0.1:8000/")
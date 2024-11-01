from fastapi import FastAPI
from .database.db import create_db_and_tables
from .routers import products


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def read_root():
    return {"hello World"}


app.include_router(products.router)

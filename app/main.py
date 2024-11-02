from fastapi import FastAPI
from .database.db import create_db_and_tables
from .routers import products, orders, order_window


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(products.router)
app.include_router(orders.router)
app.include_router(order_window.router)

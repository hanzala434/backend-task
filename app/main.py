from fastapi import FastAPI
from .routers import products, sales, inventory
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="E-Commerce Admin API")

app.include_router(products.router)
app.include_router(sales.router)
app.include_router(inventory.router)

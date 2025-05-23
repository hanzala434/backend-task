from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas
from app.crud import product_crud
from ..database import SessionLocal

router = APIRouter(prefix="/products", tags=["Products"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Product)
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return product_crud.create_product(db, product)

@router.get("/", response_model=list[schemas.Product])
def list_products(db: Session = Depends(get_db)):
    return product_crud.get_all_products(db)

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas
from app.crud import inventory_crud
from ..database import SessionLocal

router = APIRouter(prefix="/inventory", tags=["Inventory"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Inventory])
def list_inventory(db: Session = Depends(get_db)):
    return inventory_crud.get_inventory(db)

@router.post("/", response_model=schemas.Inventory)
def add_inventory(inventory: schemas.InventoryCreate, db: Session = Depends(get_db)):
    return inventory_crud.create_inventory(db, inventory)

@router.get("/low-stock", response_model=list[schemas.Inventory])
def low_stock_inventory(db: Session = Depends(get_db)):
    return inventory_crud.get_low_stock(db)

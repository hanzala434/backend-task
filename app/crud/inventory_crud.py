from sqlalchemy.orm import Session
from .. import models, schemas
from datetime import date

def get_inventory(db: Session):
    return db.query(models.Inventory).all()

def create_inventory(db: Session, inventory: schemas.InventoryCreate):
    db_inv = models.Inventory(**inventory.dict())
    db.add(db_inv)
    db.commit()
    db.refresh(db_inv)
    return db_inv

def get_low_stock(db: Session, threshold=10):
    return db.query(models.Inventory).filter(models.Inventory.quantity < threshold).all()

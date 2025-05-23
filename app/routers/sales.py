from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from .. import schemas
from app.crud import sale_crud
from ..database import SessionLocal
from datetime import date

router = APIRouter(prefix="/sales", tags=["Sales"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Sale)
def add_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    return sale_crud.create_sale(db, sale)

@router.get("/", response_model=list[schemas.Sale])
def get_all_sales(db: Session = Depends(get_db)):
    return sale_crud.get_all_sales(db)

@router.get("/filter", response_model=list[schemas.Sale])
def get_filtered_sales(
    start_date: date,
    end_date: date,
    product_id: int = None,
    category: str = None,
    db: Session = Depends(get_db)
):
    return sale_crud.filter_sales(db, start_date, end_date, product_id, category)

#revenue: daily, weekly, monthly, yearly
@router.get("/revenue/aggregate")
def revenue_aggregate(
    mode: str = Query(..., regex="^(daily|weekly|monthly|yearly)$"),
    db: Session = Depends(get_db)
):
    return sale_crud.aggregate_revenue(db, mode)

#revenue between two periods
@router.get("/revenue/compare")
def revenue_compare(
    period1_start: date,
    period1_end: date,
    period2_start: date,
    period2_end: date,
    category: str = None,
    db: Session = Depends(get_db)
):
    rev1, rev2 = sale_crud.compare_revenue(
        db, period1_start, period1_end, period2_start, period2_end, category
    )
    return {
        "period1": {"start": period1_start, "end": period1_end, "revenue": rev1},
        "period2": {"start": period2_start, "end": period2_end, "revenue": rev2},
        "difference": rev2 - rev1
    }
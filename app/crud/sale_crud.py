from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date
from .. import models, schemas

def create_sale(db: Session, sale: schemas.SaleCreate):
    db_sale = models.Sale(**sale.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale

def get_all_sales(db: Session):
    return db.query(models.Sale).all()


def filter_sales(db: Session, start_date, end_date, product_id=None, category=None):
    query = db.query(models.Sale).join(models.Product)
    query = query.filter(models.Sale.date >= start_date, models.Sale.date <= end_date)
    if product_id:
        query = query.filter(models.Sale.product_id == product_id)
    if category:
        query = query.filter(models.Product.category == category)
    return query.all()

def aggregate_revenue(db: Session, mode: str):
    group_by = {
        "daily": func.date(models.Sale.date),
        "weekly": func.week(models.Sale.date),
        "monthly": func.month(models.Sale.date),
        "yearly": func.year(models.Sale.date),
    }[mode]

    result = db.query(
        group_by.label("period"),
        func.sum(models.Sale.total_price).label("revenue")
    ).group_by("period").all()

    # serialize result manually
    return [
        {
            "period": str(row.period),
            "revenue": float(row.revenue)
        }
        for row in result
    ]


def compare_revenue(db: Session, start1: date, end1: date, start2: date, end2: date, category: str = None):
    def get_revenue(start, end):
        q = db.query(func.sum(models.Sale.total_price)).join(models.Product)
        q = q.filter(models.Sale.date >= start, models.Sale.date <= end)
        if category:
            q = q.filter(models.Product.category == category)
        return q.scalar() or 0.0
    rev1 = get_revenue(start1, end1)
    rev2 = get_revenue(start2, end2)
    return rev1, rev2

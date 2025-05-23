from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    category = Column(String(255))
    price = Column(Float)
    stock = Column(Integer)

    sales = relationship("Sale", back_populates="product")
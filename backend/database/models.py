import sqlalchemy
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy import Table
from sqlalchemy import DateTime
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base

from backend.domain.food import FoodCategory, FoodType

Base = declarative_base()

class Food(Base):
    __tablename__ = 'food_items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(), nullable=False)
    category = Column(Enum(FoodCategory), nullable=False)
    type = Column(Enum(FoodType), nullable=False)
    last_used = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

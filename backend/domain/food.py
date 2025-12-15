from enum import Enum

class FoodCategory(Enum):
    Breakfast = 1
    Meal = 2

class FoodType(Enum):
    NA = 1
    Veg = 2
    Non_Veg = 3

class FoodItems:
    def __init__(self, name: str, category: FoodCategory, type: FoodType):
        self.name = name
        self.category = category
        self.type = type


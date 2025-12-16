from random import randint
import pandas as pd
from datetime import datetime, timedelta

from backend.database.models import FoodCategory, FoodType

class RandomSelector:
    def __init__(self):
        pass

    def select_element(self, df):
        random_dish = df.loc[randint(0,len(df)), 'name']
        return random_dish
    
    def select_element(self, df, category, type):
        yesterday = (datetime.now() - timedelta(days=1)).date()
        df = df[(df['last_used'].dt.date != yesterday) & 
                (df['last_used'].dt.date != datetime.now().date())]
        if category == 'Breakfast' or type == 'NA':
            df = df[df['category'] == FoodCategory[category]]
        else:
            df = df[(df['category'] == FoodCategory[category]) & (df['type'] == FoodType[type])]
        rand_index = randint(0, len(df)-1)
        random_dish = df.iloc[rand_index]['name']
        #random_dish_id = df.iloc[rand_index]['id']
        return random_dish

    def food_selected_today(self, df, category):
        df = df[df['category'] == FoodCategory[category]]
        df = df[df['last_used'].dt.date == datetime.now().date()]
        return not df.empty
from random import randint

class RandomSelector:
    def __init__(self):
        pass

    def select_element(self, df):
        print("len of df:", len(df))
        random_dish = df.loc[randint(0,len(df)), 'Food']
        return random_dish

from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from backend.database.models import Food
from backend.database.write import write_items
from backend.src.data_reader import DataReader
from backend.database.connect import connect_db

#if not engine:
#    path="postgresql://daisy@localhost:5432/food"
#    engine = create_engine(path, echo=True)
#session = Session(engine)
class DatabasePopulator:
    def __init__(self):
        engine = connect_db()
        if engine is not None:
            self.session = Session(engine)

    def populate_database(self, food_df):
        food_df = food_df.to_dict(orient='records')
        try:
            write_items(self.session, Food, food_df)
            #print(items)
        except Exception as e:
            print('Error populating database:', repr(e))
        finally:
            self.session.commit()
            self.session.close()

if __name__ == "__main__":
    file_path = "./data/dishes.numbers"
    reader = DataReader(file_path)
    data = reader.read_data_excel()
    populator = DatabasePopulator()
    populator.populate_database(data)
import pandas as pd
from numbers_parser import Document
from sqlalchemy.orm import Session

from backend.database.read import read_items
from backend.database.models import Food
from backend.database.connect import ConnectDB
from backend.services.settings import FILE_PATH

connectdb = ConnectDB()

class DataReader():
    def __init__(self, file_path: str):
        self.doc = Document(file_path)
        self.df = None
        connectdb.connect_db()

    def read_data_excel(self) -> pd.DataFrame:
        sheet = self.doc.sheets[0]
        table = sheet.tables[0]
        data = table.rows()
        headers = [cell.value for cell in data[0]]
        rows = [[cell.value for cell in row] for row in data[1:]]
        df = pd.DataFrame(rows, columns=headers)
        self.df = df
        return df
    
    def read_data_db(self) -> pd.DataFrame:
        try:
            session = Session(connectdb.engine)
            df = read_items(session, Food)
            return df
        except Exception as e:
            print('Error reading from database:', repr(e))
            return None
        finally:
            session.close()
        
    def get_categories(self) -> list:
        df = self.read_data_db()
        categories = df['category'].unique().tolist()
        return [c.name for c in categories]
    
    def get_types(self) -> list:
        df = self.read_data_db()
        types = df['type'].unique().tolist()
        return [t.name for t in types]

if __name__ == "__main__":
    file_path = FILE_PATH
    reader = DataReader(file_path)
    data = reader.read_data_excel()
    #print(data)
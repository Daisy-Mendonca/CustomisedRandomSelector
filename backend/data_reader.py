import pandas as pd
from numbers_parser import Document


class DataReader():
    def __init__(self, file_path: str):
        self.doc = Document(file_path)

    def read_data(self) -> pd.DataFrame:
        sheet = self.doc.sheets[0]
        table = sheet.tables[0]
        data = table.rows()
        headers = [cell.value for cell in data[0]]
        rows = [[cell.value for cell in row] for row in data[1:]]
        df = pd.DataFrame(rows, columns=headers)
        return df



if __name__ == "__main__":
    file_path = "./data/dishes.numbers"
    reader = DataReader(file_path)
    data = reader.read_data()
    print(data)
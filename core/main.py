from backend.data_reader import DataReader
from core.selector import RandomSelector


def run_dish_selector(file_path: str):
    data_reader= DataReader(file_path)
    data_frame = data_reader.read_data()
    random_dish = RandomSelector().select_element(data_frame)
    print(f"Selected Dish: {random_dish}")
    
if __name__ == "__main__":
    file_path = "./data/dishes.numbers"
    run_dish_selector(file_path)
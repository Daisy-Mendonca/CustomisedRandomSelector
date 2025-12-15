import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL", "postgresql://daisy@localhost:5432/food")
FILE_PATH = os.getenv("FILE_PATH", "./data/dishes.numbers") 
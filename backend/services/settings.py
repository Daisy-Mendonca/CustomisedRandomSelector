import os
from dotenv import load_dotenv

load_dotenv()

#DB_URL = os.getenv("DB_URL", "postgresql://daisy@localhost:5432/food")
DB_USER = os.environ["DB_USER"]
DB_PASS = os.environ["DB_PASS"]
DB_HOST = os.environ["DB_HOST"]
DB_NAME = os.environ["DB_NAME"]
DB_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
FILE_PATH = os.getenv("FILE_PATH", "./data/dishes.numbers") 
PORT = int(os.getenv("PORT", 8000))
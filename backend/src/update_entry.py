from sqlalchemy.orm import Session

from backend.database.update import update_timestamp_by_name
from backend.database.connect import ConnectDB
from backend.database.models import Food

connectdb = ConnectDB()
engine = connectdb.connect_db()

def new_timestamp(dish_name):
    try:
        session = Session(connectdb.engine)
        update_timestamp_by_name(session, Food, dish_name)
    except Exception as e:
        print('Error updating timestamp:', repr(e))
    finally:
        session.close()
    
from sqlalchemy import create_engine

from backend.services.settings import DB_URL

class ConnectDB:
    _instance = None
    engine = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def connect_db(self):
        try:
            if self.engine is not None:
                return self.engine
            self.engine = create_engine(DB_URL, echo=True)
            return self.engine
        except Exception as e:
            print('Unable to access postgresql database', repr(e))
            exit(1)




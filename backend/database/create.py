from backend.database.models import Base

def create_db(engine):
    if engine is not None:
        Base.metadata.create_all(engine)
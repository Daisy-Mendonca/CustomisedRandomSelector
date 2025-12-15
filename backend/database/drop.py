from backend.database.models import Base

def drop_dbs(engine, models):
    if engine is not None:
        tables = [model.__tablename__ for model in models]
        Base.metadata.drop_all(engine, tables=tables)
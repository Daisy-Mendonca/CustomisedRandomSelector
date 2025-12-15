import pandas as pd

def read_items(session, model) -> pd.DataFrame:
    table = model.__table__
    stmt = table.select()
    result = session.execute(stmt)
    rows = result.mappings().all() 
    df = pd.DataFrame(rows)
    return df
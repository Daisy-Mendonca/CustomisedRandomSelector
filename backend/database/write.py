from sqlalchemy import insert

def write_items(session, model, items: list[dict]):
    table = model.__table__
    stmt = (
        insert(table)
        .values(items)
        .returning(*table.c)
    )
    session.execute(stmt)
    #return result.fetchall()
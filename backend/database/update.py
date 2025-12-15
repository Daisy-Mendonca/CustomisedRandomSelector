from datetime import datetime

def update_timestamp_by_name(session, model, dish_name):
    table = model.__table__
    stmt = (
        table.update()
        .where(table.c.name == dish_name)
        .values(last_used=datetime.now())
    )
    session.execute(stmt)
    session.commit()
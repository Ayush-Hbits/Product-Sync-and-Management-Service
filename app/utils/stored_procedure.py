from sqlalchemy import text
from sqlalchemy.exc import ResourceClosedError


def execute_sp(db, procedure_name, params=None):

    params = params or {}

    placeholders = ", ".join(
        [f":{key}" for key in params.keys()]
    )

    sql = f"CALL {procedure_name}({placeholders})"

    result = db.execute(text(sql), params)
    db.commit()
    try:
        rows = result.mappings().all()
        return [dict(row) for row in rows]

    except ResourceClosedError:
        return None



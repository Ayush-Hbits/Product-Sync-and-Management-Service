from sqlalchemy import text

def execute_sp(db, sp_name:str, params:dict | None = None):
    params = params or {}
    placeholders = ", ".join([f":{key}" for key in params.keys()])
    sql = f"CALL {sp_name}({placeholders})"
    result =db.execute(text(sql), params)
    rows = result.mappings().all()
    return [dict(row) for row in rows]




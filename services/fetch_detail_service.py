from routes import db

def get_risk_detail(rkid, severity):
    TbName = "risk_" + severity.lower()
    cur = db.connection.cursor()
    cur.execute(f"SELECT risk_name, risk_description, risk_solution FROM {TbName} WHERE risk_id = '{rkid}'")
    row = cur.fetchone()
    cur.close()

    data = {
        "risk_name": row[0],
        "risk_description": row[1],
        "risk_solution": row[2]
    }

    return data

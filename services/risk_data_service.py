from routes import db

class GetWebsiteRiskData():
    def __init__(self, website_name):
        self.website_name = website_name

    def get_website_data(self):
        cur = db.connection.cursor()
        cur.execute(f"SELECT collection, rejected FROM websites WHERE website_name = '{self.website_name}'")
        result = cur.fetchone()
        collection, rejected = result
        return collection, rejected

    def get_nessus_risks(self):
        cur = db.connection.cursor()
        cur.execute(f"SELECT wr.risk_quantity, r.risk_id, r.risk_severity FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_severity = 'low'")
        rklow = cur.fetchall()

        cur.execute(f"SELECT wr.risk_quantity, r.risk_id, r.risk_severity FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_severity = 'medium'")
        rkmedium = cur.fetchall()

        cur.execute(f"SELECT wr.risk_quantity, r.risk_id, r.risk_severity FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_severity = 'high'")
        rkhigh = cur.fetchall()

        cur.execute(f"SELECT wr.risk_quantity, r.risk_id, r.risk_severity FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_severity = 'critical'")
        rkcritical = cur.fetchall()

        cur.close()
        return rklow, rkmedium, rkhigh, rkcritical

    def get_zap_risks(self):
        cur = db.connection.cursor()
        cur.execute(f"SELECT wr.risk_quantity, r.risk_id, r.risk_severity FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_id = 'low'")
        rklow = cur.fetchall()

        cur.execute(f"SELECT wr.risk_quantity, r.risk_id, r.risk_severity FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_id = 'medium'")
        rkmedium = cur.fetchall()

        cur.execute(f"SELECT wr.risk_quantity, r.risk_id, r.risk_severity FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_id = 'high'")
        rkhigh = cur.fetchall()

        cur.close()
        return rklow, rkmedium, rkhigh

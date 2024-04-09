from routes import db

class GetWebsiteRiskData():
    def __init__(self, website_name):
        self.website_name = website_name

    def get_website_data(self):
        cur = db.connection.cursor()
        cur.execute(f"SELECT collection, rejected FROM websites WHERE website_name = '{self.website_name}'")
        result = cur.fetchone()
        collection, rejected = result

        cur.close()
        return collection, rejected

    def get_nessus_risks(self):
        chart_data = []
        cur = db.connection.cursor()

        cur.execute(f"SELECT r.risk_id, r.risk_name, r.risk_synopsis ,wr.risk_quantity FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_severity = 'low'")
        rklow = cur.fetchall()
        cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_severity = 'low'")
        chart_data.append(cur.fetchone()[0])

        cur.execute(f"SELECT r.risk_id, r.risk_name, r.risk_synopsis ,wr.risk_quantity FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_severity = 'medium'")
        rkmedium = cur.fetchall()
        cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_severity = 'medium'")
        chart_data.append(cur.fetchone()[0])

        cur.execute(f"SELECT r.risk_id, r.risk_name, r.risk_synopsis ,wr.risk_quantity FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_severity = 'high'")
        rkhigh = cur.fetchall()
        cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_severity = 'high'")
        chart_data.append(cur.fetchone()[0])

        cur.execute(f"SELECT r.risk_id, r.risk_name, r.risk_synopsis ,wr.risk_quantity FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_severity = 'critical'")
        rkcritical = cur.fetchall()
        cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_severity = 'critical'")
        chart_data.append(cur.fetchone()[0])

        cur.close()
        return rklow, rkmedium, rkhigh, rkcritical, chart_data

    def get_zap_risks(self):
        chart_data = []
        cur = db.connection.cursor()

        cur.execute(f"SELECT r.risk_id, r.risk_name, r.risk_synopsis ,wr.risk_quantity FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_severity = 'low'")
        rklow = cur.fetchall()
        cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_severity = 'low'")
        chart_data.append(cur.fetchone()[0])

        cur.execute(f"SELECT r.risk_id, r.risk_name, r.risk_synopsis ,wr.risk_quantity FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_severity = 'medium'")
        rkmedium = cur.fetchall()
        cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_severity = 'medium'")
        chart_data.append(cur.fetchone()[0])

        cur.execute(f"SELECT r.risk_id, r.risk_name, r.risk_synopsis ,wr.risk_quantity FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_severity = 'high'")
        rkhigh = cur.fetchall()
        cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = '{self.website_name}' AND r.risk_severity = 'high'")
        chart_data.append(cur.fetchone()[0])

        cur.close()
        return rklow, rkmedium, rkhigh, chart_data

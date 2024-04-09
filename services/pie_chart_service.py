from routes import db

def get_nessus_pie_data():
    cur = db.connection.cursor()

    nessus_social_data = []
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'nessus_social' AND r.risk_severity = 'low'")
    nessus_social_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'nessus_social' AND r.risk_severity = 'medium'")
    nessus_social_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'nessus_social' AND r.risk_severity = 'high'")
    nessus_social_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'nessus_social' AND r.risk_severity = 'critical'")
    nessus_social_data.append(cur.fetchone()[0])
    nessus_social_data = ['0' if quantity is None else quantity for quantity in nessus_social_data]

    nessus_application_data = []
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'nessus_application' AND r.risk_severity = 'low'")
    nessus_application_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'nessus_application' AND r.risk_severity = 'medium'")
    nessus_application_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'nessus_application' AND r.risk_severity = 'high'")
    nessus_application_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'nessus_application' AND r.risk_severity = 'critical'")
    nessus_application_data.append(cur.fetchone()[0])
    nessus_application_data = ['0' if quantity is None else quantity for quantity in nessus_application_data]


    nessus_transaction_data = []
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'nessus_transaction' AND r.risk_severity = 'low'")
    nessus_transaction_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'nessus_transaction' AND r.risk_severity = 'medium'")
    nessus_transaction_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'nessus_transaction' AND r.risk_severity = 'high'")
    nessus_transaction_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'nessus_transaction' AND r.risk_severity = 'critical'")
    nessus_transaction_data.append(cur.fetchone()[0])
    nessus_transaction_data = ['0' if quantity is None else quantity for quantity in nessus_transaction_data]

    nessus_information_data = []
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'nessus_information' AND r.risk_severity = 'low'")
    nessus_information_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'nessus_information' AND r.risk_severity = 'medium'")
    nessus_information_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'nessus_information' AND r.risk_severity = 'high'")
    nessus_information_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'nessus_information' AND r.risk_severity = 'critical'")
    nessus_information_data.append(cur.fetchone()[0])
    nessus_information_data = ['0' if quantity is None else quantity for quantity in nessus_information_data]

    return nessus_social_data, nessus_application_data, nessus_transaction_data, nessus_information_data


def get_zap_pie_data():
    cur = db.connection.cursor()

    zap_social_data = []
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'zap_social' AND r.risk_severity = 'low'")
    zap_social_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'zap_social' AND r.risk_severity = 'medium'")
    zap_social_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'zap_social' AND r.risk_severity = 'high'")
    zap_social_data.append(cur.fetchone()[0])
    zap_social_data = ['0' if quantity is None else quantity for quantity in zap_social_data]

    zap_application_data = []
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'zap_application' AND r.risk_severity = 'low'")
    zap_application_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'zap_application' AND r.risk_severity = 'medium'")
    zap_application_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'zap_application' AND r.risk_severity = 'high'")
    zap_application_data.append(cur.fetchone()[0])
    zap_application_data = ['0' if quantity is None else quantity for quantity in zap_application_data]

    zap_transaction_data = []
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'zap_transaction' AND r.risk_severity = 'low'")
    zap_transaction_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'zap_transaction' AND r.risk_severity = 'medium'")
    zap_transaction_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'zap_transaction' AND r.risk_severity = 'high'")
    zap_transaction_data.append(cur.fetchone()[0])
    zap_transaction_data = ['0' if quantity is None else quantity for quantity in zap_transaction_data]

    zap_information_data = []
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'zap_information' AND r.risk_severity = 'low'")
    zap_information_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'zap_information' AND r.risk_severity = 'medium'")
    zap_information_data.append(cur.fetchone()[0])
    cur.execute(f"SELECT SUM(wr.risk_quantity) FROM website_risks wr JOIN websites w ON wr.website_id = w.website_id JOIN risks r ON wr.risk_id = r.risk_id WHERE w.website_name = 'zap_information' AND r.risk_severity = 'high'")
    zap_information_data.append(cur.fetchone()[0])
    zap_information_data = ['0' if quantity is None else quantity for quantity in zap_information_data]

    return zap_social_data, zap_application_data, zap_transaction_data, zap_information_data

from routes import app
from flask import render_template
from services.pie_chart_service import get_nessus_pie_data, get_zap_pie_data

@app.route('/')
def home_page():
    nessus_social, nessus_application, nessus_transaction, nessus_information = get_nessus_pie_data()
    zap_social, zap_application, zap_transaction, zap_information = get_zap_pie_data()
    return render_template('/home.html', 
                           nessus_social=nessus_social, nessus_application=nessus_application,
                           nessus_transaction=nessus_transaction, nessus_information=nessus_information,
                           zap_social=zap_social, zap_application=zap_application,
                           zap_transaction=zap_transaction, zap_information=zap_information
                           )

if __name__ == '__main__':
    app.run(debug=True)

from routes import app
from services.risk_data_service import GetWebsiteRiskData
from services.fetch_detail_service import get_risk_detail
from flask import render_template, abort, redirect, url_for, request, jsonify
from flask_login import current_user

@app.route("/risk_analysis/<website_name>")
def risk_analysis(website_name):
    if not current_user.is_authenticated:
      return redirect(url_for('login_page'))

    website = ["nessus_social", "nessus_application", "nessus_transaction", "nessus_information", "zap_social", "zap_application", "zap_transaction", "zap_information"]
    if website_name in website:
      collection, rejected = GetWebsiteRiskData(website_name).get_website_data()
      if website_name[0] == "n":
        low_risk, medium_risk, high_risk, critical_risk, chart_data = GetWebsiteRiskData(website_name).get_nessus_risks()

        return render_template(f"/risk_analysis/nessus/{website_name}.html",
                          low_risk=low_risk,
                          medium_risk=medium_risk,
                          high_risk=high_risk,
                          critical_risk=critical_risk,
                          collection=collection, rejected=rejected, chart_data=chart_data
                        )
      elif website_name[0] == "z":
        low_risk, medium_risk, high_risk, chart_data = GetWebsiteRiskData(website_name).get_zap_risks()

        return render_template(f"/risk_analysis/zap/{website_name}.html",
                          low_risk=low_risk,
                          medium_risk=medium_risk,
                          high_risk=high_risk,
                          collection=collection, rejected=rejected, chart_data=chart_data
                        )

    abort(404)

@app.route("/fetch_detail")
def fetch_detail():
  rkid = request.args.get('id')

  data = get_risk_detail(rkid)

  return jsonify(data)

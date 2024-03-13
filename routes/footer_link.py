from routes import app
from flask import render_template, request

def monitor_click_link():
    title = request.args.get('title', '')
    return title

@app.route('/about')
def about_page():
    title = monitor_click_link()
    return render_template('/footer_link/about.html', title=title)

@app.route('/instruct')
def instruct_page():
    title = monitor_click_link()
    return render_template('/footer_link/instruct.html', title=title)

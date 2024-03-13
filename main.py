from routes import app
from flask import render_template

@app.route('/')
def home_page():
    return render_template('/home.html')

if __name__ == '__main__':
    app.run(debug=True)

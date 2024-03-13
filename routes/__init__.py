from flask import Flask
from flask_login import LoginManager
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__,
            template_folder='../templates',
            static_folder='../assets',
            static_url_path='/assets'
            )

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'uch_user'
app.config['MYSQL_PASSWORD'] = 'uch543827'
app.config['MYSQL_DB'] = 'risk_analysis'

db = MySQL(app)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+mysqldb://uch_user:uch543827@localhost/account_data"
)
app.config['SECRET_KEY'] = 'fc61c76741f827d5061d85c821d433a0fb5792706a7dcf5c46e29be6e2d44eb6'

user_db = SQLAlchemy(app)
login_manager = LoginManager(app)

from routes import footer_link
from routes import header_link
from routes import user_routes

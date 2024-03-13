from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class RegisterForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    confirm_password = PasswordField(label="Confirm Password", validators=[DataRequired()])
    submit = SubmitField(label="註冊")
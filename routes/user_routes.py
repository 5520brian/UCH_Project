from routes import app
from forms.login_form import LoginForm
from forms.register_form import RegisterForm
from services.user_service import UserService
from flask import render_template, flash, redirect, url_for
from flask_login import logout_user

@app.route("/sign-in", methods=['GET', 'POST'])
def login_page():
  form = LoginForm()
  if form.validate_on_submit():
    result = UserService().do_login(username=form.username.data, password=form.password.data)
    if result:
      return redirect(url_for('home_page'))
    elif UserService().user_exists(username=form.username.data):
      flash("密碼輸入錯誤，請重新嘗試")
    else:
      flash("此用戶不存在，請重新嘗試")
      
  return render_template("/sign-in.html", form=form)


@app.route("/sign-out")
def logout_page():
  logout_user()
  return redirect(url_for('home_page'))

@app.route("/register", methods=['GET', 'POST'])
def register_page():
  form = RegisterForm()
  if form.validate_on_submit():
    msg = UserService().check_form_data(username=form.username.data, password=form.password.data, confirm_password=form.confirm_password.data)
    if msg != None:
      flash(msg)
      
    result = UserService().do_register(username=form.username.data, password=form.password.data)
    if result:
      flash("帳戶註冊成功，請返回登入頁面")
      return redirect(url_for('login_page'))
    else:
      flash("註冊失敗，請重新嘗試或聯絡我們")

  return render_template("/register.html", form=form)

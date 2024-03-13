from sqlalchemy import Select
from routes import user_db
from models.user import User
from flask_login import login_user
import re
import bcrypt

class UserService:
    def do_login(self, username: str, password: str) -> bool:
        query = Select(User).where(User.username == username)
        attempted_user = user_db.session.scalar(query)
        if attempted_user and attempted_user.check_password_correction(attempted_password=password):
            login_user(attempted_user)
            return True

        return False

    def user_exists(self, username: str) -> bool:
        query = Select(User).where(User.username == username)
        existing_user = user_db.session.scalar(query)
        return existing_user is not None

    def check_form_data(self, username: str, password: str, confirm_password: str):
        if self.user_exists(username):
            return "該用戶已存在，請重新嘗試"

        if password != confirm_password:
            return "密碼不匹配，請重新嘗試"

        username_pattern = re.compile(r"^[a-zA-Z0-9]{5,20}$")
        if not username_pattern.match(username):
            return "請輸入長度為 5 到 20 的英文或數字作為使用者名稱"

        password_pattern = re.compile(r"^[a-zA-Z0-9]{8,20}$")
        if not password_pattern.match(password):
            return "請輸入長度介於 8 到 20 的英文或數字作為密碼"

        return None
        

    def do_register(self, username: str, password: str) -> bool:
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        new_user = User(username=username, password_hash=hashed_password)
        user_db.session.add(new_user)
        user_db.session.commit()

        return User.query.filter_by(username=username).first() is not None
from flask_login import UserMixin
from routes import user_db, login_manager
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
import bcrypt

@login_manager.user_loader
def load_user(user_id):
    return user_db.session.get(User, user_id)

class User(user_db.Model, UserMixin):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String, primary_key=True)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)

    def check_password_correction(self, attempted_password):
        password_hashed = self.password_hash.encode()
        return bcrypt.checkpw(attempted_password.encode(), password_hashed)

    def get_id(self):
        return self.username
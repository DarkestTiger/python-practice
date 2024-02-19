from flask import Blueprint, redirect, render_template, request, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user

views = Blueprint('views', __name__)

@views.route('/log-in', methods=['GET', 'POST'])
def login():
  # login
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password1')

        # search User in database & compare password
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password1):
                flash('로그인 완료', category='success')
                return redirect(url_for('views.home'))
            else: 
                flash('비밀번호가 다릅니다.', category='error')
        else:
            flash('해당 이메일 정보가 없습니다.', category='error')
  return render_template("login.html")


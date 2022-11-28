from app import app
import json
from werkzeug.urls import url_parse
from flask import request, render_template, redirect, url_for, flash, jsonify
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Usuario
from app.form import LoginForm
from app import db


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title='Home')

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('register.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User(nombre=form.nombre.data, apellido=form.apellido.data, email=form.email.data, edad=form.edad.data)
        user.set_password(form.password.data)        
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/register_url", methods=['GET', 'POST'])
def hello_there():
    body = request.get_json()
    try:     
        newUser = Usuario(nombre=body["nombre"], apellido=body["apellido"], email=body["email"], password=body["password"], edad=int(body["edad"]))
        db.session.add(newUser)
    except Exception as error:
        print("Invalid user", error)
        return "Invalid user"     
    finally:
        db.session.commit()  
        return "Usuario añadido"

@app.route('/get_user', methods=["POST"])
def getUser():
    body = request.get_json()
    user = Usuario.query.filter(Usuario.email == body["email"] and Usuario.password == body["password"]).first()
    return json.dumps({"id": user.id, "nombre": user.nombre, "apellido": user.apellido, "edad": user.edad, "email": user.email, "password": user.password})

from app import app
import json
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, render_template, redirect, url_for, flash, jsonify
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Usuario
from app.form import LoginForm
from app import db


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title='Home')

@app.route("/register", methods=['GET', 'POST'])
def register():
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

@app.route('/users', methods=["POST", "GET"])
def getUsers():
    users = []
    user = Usuario.query.all()
    for usr in user:
        users.append({"id": usr.id, "nombre": usr.nombre, "apellido": usr.apellido, "edad": usr.edad, "email": usr.email, "password": usr.password})
    return json.dumps(users)

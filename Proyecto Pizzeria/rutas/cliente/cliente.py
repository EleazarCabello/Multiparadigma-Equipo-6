from flask import Blueprint,request,redirect,render_template,url_for,send_from_directory,jsonify
from sqlalchemy import exc
from app import db,bcrypt
from models import Usuarios
import os

appCliente = Blueprint('appcliente', __name__, template_folder="templates",static_folder='static')



@appCliente.route('/cliente')
def inicio_cliente():
    return render_template('inicioCliente.html')
from flask import Blueprint,request,redirect,render_template,url_for,send_from_directory,jsonify
from sqlalchemy import exc
from app import db,bcrypt
from models import Usuarios
import os

appAdmin = Blueprint('appadmin', __name__, template_folder="templates",static_folder='static_admin')

@appAdmin.route('/admin')
def inicio_administrador():
    return render_template('inicioAdmin.html')
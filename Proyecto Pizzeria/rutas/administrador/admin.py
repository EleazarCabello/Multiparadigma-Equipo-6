from flask import Blueprint,request,redirect,render_template,url_for,send_from_directory,jsonify
from sqlalchemy import exc
from app import db,bcrypt
from models import Usuarios
from models import Ingredientes
from models import Productos
from models import Pedidos
from models import Ventas   
from datetime import datetime
import os

appAdmin = Blueprint('appadmin', __name__, template_folder="templates",static_folder='static_admin')

@appAdmin.route('/admin')
def inicio_administrador():
    
    tablaUsuarios = Usuarios.query.all()
    tablaIngredientes = Ingredientes.query.all()
    tablaProductos = Productos.query.all()
    tablaVentas = Ventas.query.all()
    tablaPedidos = Pedidos.query.all()
    
    return render_template('admin.html',tablaUsuarios=tablaUsuarios,tablaIngredientes=tablaIngredientes,tablaProductos=tablaProductos,tablaVentas=tablaVentas,tablaPedidos=tablaPedidos)
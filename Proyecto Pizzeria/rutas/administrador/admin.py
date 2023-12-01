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

@appAdmin.route('/admin/agregar',methods=['POST'])
def admin_agregar():

    
    tabla = request.json['tabla']
   
    if tabla == "usuarios" :
        
        nombres = request.json['nombres']
        apellidos = request.json['apellidos']
        direccion = request.json['direccion']
        correo = request.json['correo']
        password = request.json['password']
        admin = bool(request.json['admin'])
        
        
        miUsuario = Usuarios(nombres=nombres,apellidos=apellidos,direccion=direccion,correo=correo,password=password,admin=admin)
        usuarioExistente = Usuarios.query.filter_by(correo=correo).first()
        
        if not usuarioExistente:
            
            db.session.add(miUsuario)
            db.session.commit()
            responseObject={
                'status':'success',
                'message':"Registro exitoso"
            }   
        else:
            responseObject={
                'status':'error',
                'message':'usuario existente'
            }
        return jsonify(responseObject)
    
    elif tabla == "productos":
        precio = request.json['precio']
        nombre = request.json['nombre']

        producto = Productos(precio=precio,nombre=nombre)
        db.session.add(producto)
        db.session.commit()
        
    elif tabla == "ingredientes":
        precio = request.json['precio']
        nombre = request.json['nombre']
        categoria = request.json['categoria']
        
        ingrediente = Ingredientes(precio=precio,categoria=categoria,nombre=nombre)
        db.session.add(ingrediente)
        db.session.commit()
        
        
    

    responseObject={
            'status':'Exitoso',
            'message':'Se agrego correctamente'
        }
    return jsonify(responseObject)



@appAdmin.route('/admin/editar',methods=['POST'])
def admin_editar():
    
    
    
    tabla = request.json['tabla']
    id = request.json['id']
    if tabla == "usuarios":
        UsuarioEncontrado = Usuarios.query.get(id)
        
        UsuarioEncontrado.nombres = request.json['nombres']
        UsuarioEncontrado.apellidos = request.json['apellidos']
        UsuarioEncontrado.direccion = request.json['direccion']
        UsuarioEncontrado.correo= request.json['correo']
        UsuarioEncontrado.password = request.json['password']
        UsuarioEncontrado.admin = bool(request.json['admin'])
        
        db.session.commit()
        
    elif tabla == "productos":
        ProductosEncontrado = Productos.query.get(id)
        
        ProductosEncontrado.nombre = request.json['nombre']
        ProductosEncontrado.precio = request.json['precio']
        db.session.commit()

        
    elif tabla == "ingredientes":
        IngredientesEncontrado = Ingredientes.query.get(id)
        
        IngredientesEncontrado.nombre = request.json['nombre']
        IngredientesEncontrado.precio = request.json['precio']
        IngredientesEncontrado.categoria = request.json['categoria']
        db.session.commit()

        
    responseObject={
            'status':'Exitoso',
            'message':'Se edito correctamente'
        }
    return jsonify(responseObject)
        
    
@appAdmin.route('/admin/eliminar',methods=['POST'])
def admin_eliminar():
    
    registro = request.json['registro']
    tabla = registro['tabla']
    id = registro['id']
    
    if tabla == "pedidos":
        pedido = Pedidos.query.get_or_404(id)
        db.session.delete(pedido)
        
    elif tabla == "ventas":
        venta = Ventas.query.get_or_404(id)
        db.session.delete(venta)
        
    elif tabla == "productos":
        producto = Productos.query.get_or_404(id)
        db.session.delete(producto)
        
    elif tabla == "ingredientes":
        ingrediente = Ingredientes.query.get_or_404(id)
        db.session.delete(ingrediente)
        
    elif tabla == "usuarios":
        usuario = Usuarios.query.get_or_404(id)
        db.session.delete(usuario)

    db.session.commit()
    responseObject={
            'status':'Exitoso',
            'message':'Se elimino correctamente'
        }
    return jsonify(responseObject)

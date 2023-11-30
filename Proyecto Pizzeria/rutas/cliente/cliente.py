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

appCliente = Blueprint('appcliente', __name__, template_folder="templates",static_folder='static_cliente')



@appCliente.route('/cliente')
def inicio_cliente():
    misIngredientes = Ingredientes.query.all()
    misProductos = Productos.query.all()
    return render_template('cliente.html',misIngredientes=misIngredientes, misProductos=misProductos)

@appCliente.route('/cliente/insertar_pedido',methods=["POST"])
def insertar_pedido():
    
    id_usuario=request.json['id_usuario']
    precio_total=request.json['precio_total']
    fecha = datetime.now()
    
    miPedido = Pedidos(fecha=fecha,precio_total=precio_total,id_usuario=id_usuario)
    
    #print(miPedido.id_usuario)
    #print(miPedido.fecha)
    #print(miPedido.precio_total)
    
    db.session.add(miPedido)
    db.session.commit()
    
    ultimoPedido = Pedidos.query.order_by(Pedidos.id.desc()).first()

    print(ultimoPedido)
    
    
    productos = request.json['ventas_individuales']
    for producto in productos:
        
        BuscarProducto = Productos.query.filter_by(nombre=producto['nombre']).first()
        
        if BuscarProducto == None:
            miVenta = Ventas(fecha=fecha,precio=producto['precio'],id_producto=7,id_pedido=ultimoPedido.id)
            db.session.add(miVenta)
            db.session.commit()
        else:
            if producto['precio'] != 0:
                miVenta = Ventas(fecha=fecha,precio=producto['precio'],id_producto=BuscarProducto.id,id_pedido=ultimoPedido.id)
                db.session.add(miVenta)
                db.session.commit()
            
        
        print(producto)
    
    responseObject={
            'status':'Exitoso',
            'message':'Se agregaron las ventas y el pedido'
        }
    return jsonify(responseObject)

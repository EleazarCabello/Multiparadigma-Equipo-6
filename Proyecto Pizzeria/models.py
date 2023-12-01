import jwt
import datetime
from config import BaseConfig
from app import db,bcrypt

class Usuarios(db.Model):
    __tablename__="usuarios"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombres=db.Column(db.String(255),nullable=True)
    apellidos=db.Column(db.String(255),nullable=True)
    direccion=db.Column(db.String(255),nullable=True)
    correo=db.Column(db.String(255),unique=True,nullable=True)
    password=db.Column(db.String(255),nullable=False)
    admin = db.Column(db.Boolean,nullable=False,default=False)
    
    def __init__(self,nombres,apellidos,direccion,correo,password,admin=False):
        self.nombres=nombres
        self.apellidos=apellidos
        self.direccion=direccion
        self.correo=correo
        self.password=bcrypt.generate_password_hash(password,BaseConfig.BCRYPT_LOG_ROUNDS).decode()
        self.admin=admin
    
    @classmethod
    def constructor_temporal(self,correo,password):
        return self(
            nombres="temp",
            apellidos="temp",
            direccion="temp",
            correo=correo,
            password=bcrypt.generate_password_hash(password,BaseConfig.BCRYPT_LOG_ROUNDS).decode(),
            admin=False
        )
    
    def encode_auth_token(self,id):
        try:
            print('USER',id)
            payload={
                'exp':datetime.datetime.utcnow()+datetime.timedelta(hours=5),
                'iat':datetime.datetime.utcnow(),
                'sub':id
            }
            print("PAYLOAD",payload)
            return jwt.encode(
                payload,
                BaseConfig.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            print("EXCEPTION")
            print(e)
            return e
    
        
        
class Ingredientes(db.Model):
    __tablename__="ingredientes"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre=db.Column(db.String(255),nullable=True)
    categoria=db.Column(db.String(255),nullable=True)
    precio=db.Column(db.Float)
    url_imagen=db.Column(db.String(1000))
    
    def __init__(self,nombre,categoria,precio,url_imagen):
        self.nombre=nombre
        self.categoria=categoria
        self.precio=precio
        self.url_imagen=url_imagen
    
class Productos(db.Model):
    __tablename__="productos"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    nombre=db.Column(db.String(255),nullable=True)
    precio=db.Column(db.Float)
    url_imagen=db.Column(db.String(1000))
    
    def __init__(self,nombre,precio,url_imagen):
        self.nombre=nombre
        self.precio=precio
        self.url_imagen=url_imagen
    
class Pedidos(db.Model):
    __tablename__="pedidos"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    fecha=db.Column(db.DateTime,nullable = False)
    precio_total=db.Column(db.Float)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    
    def __init__(self,fecha,precio_total,id_usuario):
        self.fecha=fecha
        self.precio_total=precio_total
        self.id_usuario=id_usuario

    
class Ventas(db.Model):
    __tablename__="ventas"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    fecha=db.Column(db.DateTime,nullable = False)
    precio=db.Column(db.Float)
    id_producto = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    
    def __init__(self,fecha,precio,id_producto,id_pedido):
        self.fecha=fecha
        self.precio=precio
        self.id_producto=id_producto
        self.id_pedido=id_pedido
    
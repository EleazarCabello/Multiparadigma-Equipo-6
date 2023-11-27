from flask import Blueprint,request,redirect,render_template,url_for,send_from_directory,jsonify
from sqlalchemy import exc
from app import db,bcrypt
from models import Usuarios
import os

appIndex = Blueprint('appindex', __name__, template_folder="templates",static_folder='static')



@appIndex.route('/')
def inicio():
    return render_template('index.html')

@appIndex.route('/login')
def login():
    return render_template('login.html')

@appIndex.route('/register')
def register():
    return render_template('register.html')

@appIndex.route('/register/crear_cuenta',methods=["GET","POST"])
def crear_cuenta():
    if request.method=="GET":
        return render_template('register.html')
    else:
        nombres=request.json['nombres']
        apellidos=request.json['apellidos']
        direccion=request.json['direccion']
        correo=request.json['correo']
        password=request.json['password']
        
        miUsuario = Usuarios(nombres=nombres,apellidos=apellidos,direccion=direccion,correo=correo,password=password)
        usuarioExistente = Usuarios.query.filter_by(correo=correo).first()
        
        if not usuarioExistente:
            try:
                db.session.add(miUsuario)
                db.session.commit()
                responseObject={
                    'status':'success',
                    'message':"Registro exitoso"
                }   
            except exc.SQLAlchemyError as e:
                    responseObject={
                    'status':'error',
                    'message':e
                }
        else:
            responseObject={
                'status':'error',
                'message':'suario existente'
            }
        return jsonify(responseObject)
    
    
@appIndex.route('/login/iniciar_sesion',methods=["GET","POST"])
def iniciar_sesion():
    
    if(request.method=="GET"):
        #token = request.args.get('token')
        #if token:
        #    info = verificar(token)
        #    if(info['status']!="fail"):
        #        responseObject={
        #            'status':"success",
        #            'message':'valid token',
        #            'info':info
        #        }
        #        return jsonify(responseObject)
        return render_template('login.html')
    else:
        correo = request.json['correo']
        password = request.json['password']
        
        if password == "":
            password = "vacio"
        
        print(correo,password)
        miUsuario = Usuarios.constructor_temporal(correo=correo,password=password)
        
        buscarUsuario = Usuarios.query.filter_by(correo=correo).first()
        if buscarUsuario:
            validacion = bcrypt.check_password_hash(buscarUsuario.password,password)
            
            if validacion:
                print(miUsuario)
                auth_token = miUsuario.encode_auth_token(id=buscarUsuario.id)
                responseObject={
                    'status':"success",
                    'login':'Loggin exitoso',
                    'auth_token':auth_token,
                    'message':"Inicio exitoso",
                    'admin': miUsuario.admin
                }
                return jsonify(responseObject)
        return jsonify({'message':"Datos incorrectos"})
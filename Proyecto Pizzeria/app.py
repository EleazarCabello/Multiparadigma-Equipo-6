from flask import Flask
from flask_cors import CORS
from database import db
from encriptador import bcrypt
from config import BaseConfig
from flask_migrate import Migrate
from rutas.index.index import appIndex
from rutas.administrador.admin import appAdmin
from rutas.cliente.cliente import appCliente


app = Flask(__name__, static_url_path='')
app.register_blueprint(appIndex)
app.register_blueprint(appAdmin)
app.register_blueprint(appCliente)
app.config.from_object(BaseConfig)
CORS(app)

bcrypt.init_app(app)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app,db)
from flask import Blueprint, Response
from models import Usuarios
from models import Productos
from models import Ingredientes
from models import Ventas
from models import Pedidos

appCSV = Blueprint("appcsv", __name__, template_folder="templates")

def generate_csv(tabla):
    # Consulta a la base de datos para obtener los datos de la tabla
    data = tabla.query.all()

    # Crea una lista para almacenar los datos en formato CSV
    csv_data = []

    # Encabezados de las columnas
    headers = [column.name for column in tabla.__table__.columns]
    csv_data.append(headers)

    # Agrega filas de datos
    for row in data:
        row_data = [str(getattr(row, column)) for column in headers]
        csv_data.append(row_data)

    # Crea un generador para yield de filas CSV
    def generate():
        for row in csv_data:
            yield ','.join(row) + '\n'

    # Configura los encabezados de la respuesta para indicar el contenido CSV
    response_headers = {
        'Content-Disposition': f'attachment; filename={tabla.__tablename__}_data.csv',
        'Content-Type': 'text/csv'
    }

    # Retorna un objeto de respuesta Flask con el generador CSV
    return Response(generate(), headers=response_headers)

# Ruta para descargar CSV de la tabla de Usuarios
@appCSV.route('/descargar_csv/usuarios')
def descargar_csv_usuarios():
    return generate_csv(Usuarios)

# Ruta para descargar CSV de la tabla de Ingredientes
@appCSV.route('/descargar_csv/ingredientes')
def descargar_csv_ingredientes():
    return generate_csv(Ingredientes)

@appCSV.route('/descargar_csv/productos')
def descargar_csv_productos():
    return generate_csv(Productos)

@appCSV.route('/descargar_csv/ventas')
def descargar_csv_ventas():
    return generate_csv(Ventas)

@appCSV.route('/descargar_csv/pedidos')
def descargar_csv_pedidos():
    return generate_csv(Pedidos)

from flask import Blueprint, make_response
from models import Ingredientes, Productos, Ventas, Pedidos,Usuarios
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER

appPDF = Blueprint('apppdf', __name__, template_folder="templates")

def generate_pdf(data, filename):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    
    # Crear la tabla con los datos proporcionados
    table = Table(data)

    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 16),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ])

    table.setStyle(style)
    elements = [table]

    doc.build(elements)

    buffer.seek(0)
    response = make_response(buffer.read())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = f'inline; filename={filename}.pdf'
    return response

@appPDF.route('/generarPdf/ingredientes')
def generate_pdf_ingredientes():
    ingredientes = Ingredientes.query.all()
    data = [["ID", "NOMBRE", "CATEGORIA","PRECIO"]]
    for ingrediente in ingredientes:
        data.append([ingrediente.id, ingrediente.nombre, ingrediente.categoria,ingrediente.precio])
    return generate_pdf(data, "ingredientes")

@appPDF.route('/generarPdf/productos')
def generate_pdf_productos():
    productos = Productos.query.all()
    data = [["ID", "NOMBRE", "PRECIO"]]
    for producto in productos:
        data.append([producto.id, producto.nombre, producto.precio])
    return generate_pdf(data, "productos")

@appPDF.route('/generarPdf/ventas')
def generate_pdf_ventas():
    ventas = Ventas.query.all()
    data = [["ID", "FECHA", "PRECIO", "ID_PRODUCTO","ID_PEDIDO"]]
    for venta in ventas:
        data.append([venta.id, venta.fecha, venta.precio, venta.id_producto,venta.id_pedido])
    return generate_pdf(data, "ventas")

@appPDF.route('/generarPdf/pedidos')
def generate_pdf_pedidos():
    pedidos = Pedidos.query.all()
    data = [["ID", "FECHA", "PRECIO_TOTAL", "ID_USUARIO"]]
    for pedido in pedidos:
        data.append([pedido.id, pedido.fecha, pedido.precio_total, pedido.id_usuario])
    return generate_pdf(data, "pedidos")

@appPDF.route('/generarPdf/usaurios')
def generate_pdf_usuarios():
    usuarios = Usuarios.query.all()
    data = [["ID", "Nombres", "Apellidos", "Dirección", "Correo", "Admin"]]
    for usuario in usuarios:
        data.append([usuario.id, usuario.nombres, usuario.apellidos, usuario.direccion, usuario.correo, usuario.admin])
    return generate_pdf(data, "usuarios")

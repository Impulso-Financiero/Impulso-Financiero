#Categorias
from models.categoria import Categoria

# Define tus categorías disponibles aquí
CATEGORIAS_INGRESOS_DISPONIBLES = [
    Categoria(id_categoria=1, nombre="Salario", tipo="Ingreso"),
    Categoria(id_categoria=2, nombre="Freelance", tipo="Ingreso"),
]

CATEGORIAS_GASTOS_DISPONIBLES =[
    Categoria(id_categoria=1, nombre="Alimentación", tipo="Gasto"),
    Categoria(id_categoria=2, nombre="Transporte", tipo="Gasto"),
    Categoria(id_categoria=3, nombre="Entretenimiento", tipo="Gasto"),
    Categoria(id_categoria=4, nombre="Servicios", tipo="Gasto"),
    Categoria(id_categoria=5, nombre="Salud", tipo="Gasto"),
    Categoria(id_categoria=6, nombre="Tarjeta de Credito", tipo="Gasto"),
    Categoria(id_categoria=7, nombre="Mascota", tipo="Gasto")
    # Puedes añadir más categorías aquí si lo necesitas
]

# Tipos de alertas
ALERTAS_TIPOS = ["Exceso de gasto", "Meta alcanzada", "Recordatorio"]

# Límites de presupuesto por defecto
LIMITE_ALIMENTACION = 0.0
LIMITE_SERVICIOS = 0.0
LIMITE_TRANSPORTE = 0.0
LIMITE_OCIO = 0.0
LIMITE_OTROS = 0.0

# Otros valores globales
MAX_DESCRIPCION = 30  # longitud máxima de descripciones

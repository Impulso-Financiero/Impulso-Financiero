#Categorias
from models.categoria import Categoria

# Definir categorías de ingresos
CATEGORIAS_INGRESOS_DISPONIBLES = [
    Categoria(id_categoria=1, nombre="Salario", tipo="Ingreso"),
    Categoria(id_categoria=2, nombre="Ventas", tipo="Ingreso"),
    Categoria(id_categoria=3, nombre="Intereses", tipo="Ingreso"),
    Categoria(id_categoria=4, nombre="Inversiones", tipo="Ingreso"),
    Categoria(id_categoria=5, nombre="Regalos", tipo="Ingreso"),
]

# Definir categorías de gastos
CATEGORIAS_GASTOS_DISPONIBLES = [
    Categoria(id_categoria=11, nombre="Alimentación", tipo="Gasto"),
    Categoria(id_categoria=12, nombre="Transporte", tipo="Gasto"),
    Categoria(id_categoria=13, nombre="Vivienda", tipo="Gasto"),
    Categoria(id_categoria=14, nombre="Entretenimiento", tipo="Gasto"),
    Categoria(id_categoria=15, nombre="Educación", tipo="Gasto"),
    Categoria(id_categoria=16, nombre="Salud", tipo="Gasto"),
    Categoria(id_categoria=17, nombre="Servicios", tipo="Gasto"),
    Categoria(id_categoria=18, nombre="Delivery", tipo="Gasto"),
    Categoria(id_categoria=19, nombre="Ropa", tipo="Gasto"),
    Categoria(id_categoria=20, nombre="Mascota", tipo="Gasto")
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

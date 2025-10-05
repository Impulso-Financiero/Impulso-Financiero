import datetime
from .categoria import Categoria # Importa la clase Categoria

class Gasto:
    def __init__(self, id_gasto: int, monto: float, categoria: Categoria, fecha: datetime.date, tipo: str, descripcion: str):
        self.id_gasto = id_gasto
        self.monto = monto
        self.categoria = categoria # Objeto Categoria
        self.fecha = fecha
        self.tipo = tipo # "Fijo" o "Variable"
        self.descripcion = descripcion # Añadir si es necesario y está en UML

    def modificar_gasto(self, monto: float = None, categoria: Categoria = None, fecha: datetime.date = None):
        """Permite actualizar los detalles de un gasto."""
        if monto is not None:
            self.monto = monto
        if categoria:
            self.categoria = categoria
        if fecha:
            self.fecha = fecha
        print(f"Gasto {self.id_gasto} modificado.")

    def calcular_total_mensual(self):
        """Calcula el total mensual si el gasto es recurrente (lógica no implementada aquí)."""
        # Similar a Ingreso, retorna el monto para un gasto puntual.
        return self.monto

    def obtener_detalle(self) -> str:
        """Devuelve una cadena con los detalles completos del gasto."""
        return f"Gasto ID: {self.id_gasto}, Monto: ${self.monto}, Categoría: {self.categoria.nombre}, Fecha: {self.fecha}, Tipo: {self.tipo}"

    def __str__(self):
        return f"Gasto de ${self.monto} en {self.categoria.nombre} el {self.fecha}"

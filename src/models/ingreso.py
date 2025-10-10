import datetime
from .categoria import Categoria # Importa la clase Categoria

class Ingreso:
    def __init__(self, id_ingreso: int, monto: float, categoria: Categoria, fecha: datetime.date, tipo: str):
        self.id = id_ingreso
        self.monto = monto
        self.categoria = categoria # Objeto Categoria
        self.fecha = fecha
        self.tipo = tipo # "Fijo" o "Variable"
        # self.descripcion = descripcion # Añadir si es necesario y está en UML

    def calcular_total_mensual(self):
        """Calcula el total mensual si el ingreso es recurrente (lógica no implementada aquí)."""
        # Esta lógica dependería de si el ingreso es recurrente o puntual.
        # Por simplicidad, se retorna el monto para un ingreso puntual.
        return self.monto

    def modificar_ingreso(self, monto: float = None, categoria: Categoria = None, fecha: datetime.date = None):
        """Permite actualizar los detalles de un ingreso."""
        if monto is not None:
            self.monto = monto
        if categoria:
            self.categoria = categoria
        if fecha:
            self.fecha = fecha
        print(f"Ingreso {self.id} modificado.")

    def obtener_detalle(self) -> str:
        """Devuelve una cadena con los detalles completos del ingreso."""
        return f"Ingreso ID: {self.id}, Monto: ${self.monto}, Categoría: {self.categoria.nombre}, Fecha: {self.fecha}, Tipo: {self.tipo}"

    def __str__(self):
        return f"Ingreso de ${self.monto} en {self.categoria.nombre} el {self.fecha}"

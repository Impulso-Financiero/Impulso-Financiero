import datetime
# Importamos la clase Usuario ya que Alerta tiene una composición con Usuario
from .usuario import Usuario 

class Alerta:
    def __init__(self, id_alerta: int, usuario: Usuario, tipo: str, mensaje: str, fecha: datetime.date):
        self.id_alerta = id_alerta
        self.usuario = usuario # Objeto Usuario al que pertenece la alerta
        self.tipo = tipo # Ej: "gasto", "ahorro", "vencimiento"
        self.mensaje = mensaje
        self.fecha = fecha
        self.activo = True # Por defecto, la alerta está activa al crearse

    def crear_alerta(self, tipo: str, mensaje: str, fecha: datetime.date):
        """Reconfigura una alerta existente o simula la creación (constructor alternativo)."""
        self.tipo = tipo
        self.mensaje = mensaje
        self.fecha = fecha
        self.activo = True

    def activar(self):
        """Activa la alerta."""
        self.activo = True
        print(f"Alerta {self.id_alerta} activada.")

    def desactivar(self):
        """Desactiva la alerta."""
        self.activo = False
        print(f"Alerta {self.id_alerta} desactivada.")

    def editar_mensaje(self, nuevo_mensaje: str):
        """Modifica el mensaje de la alerta."""
        self.mensaje = nuevo_mensaje
        print(f"Mensaje de Alerta {self.id_alerta} modificado.")

    def obtener_detalle(self) -> str:
        """Devuelve una cadena con la información completa de la alerta."""
        estado = "Activa" if self.activo else "Inactiva"
        return f"ID Alerta: {self.id_alerta}, Tipo: {self.tipo}, Mensaje: '{self.mensaje}', Fecha: {self.fecha}, Estado: {estado}, Usuario: {self.usuario.nombre}"

    def enviar_notificacion(self):
        """Envía la alerta al usuario (simulación)."""
        if self.activo:
            print(f"--- NOTIFICACIÓN ---")
            print(f"Para: {self.usuario.nombre} ({self.usuario.email})")
            print(f"Alerta de {self.tipo.upper()}: {self.mensaje}")
            print(f"Fecha: {self.fecha}")
            print(f"--------------------")
        else:
            print(f"Alerta {self.id_alerta} está inactiva y no se envió la notificación.")

    def __str__(self):
        return f"Alerta ({self.tipo}): {self.mensaje}"
    
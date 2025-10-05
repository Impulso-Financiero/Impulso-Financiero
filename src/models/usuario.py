import datetime
from .perfil_financiero import PerfilFinanciero 
from .alerta import Alerta # Si Alerta también se importa aquí

class Usuario:
    def __init__(self, id_usuario: int, nombre: str, email: str, password: str):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.password = password
        self.perfil_financiero = None # Se asignará más tarde, ej. al registrar
        self.alertas = [] # Lista para almacenar objetos Alerta

    def registrar_usuario(self, nombre: str, email: str, password: str):
        # Lógica para registrar un nuevo usuario
        # En una implementación real, esto interactuaría con db_controller.py
        self.nombre = nombre
        self.email = email
        self.password = password
        print(f"Usuario {self.nombre} registrado con éxito.")
        
    def editar_perfil(self, nuevo_nombre: str = None, nuevo_email: str = None):
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nuevo_email:
            self.email = nuevo_email
        print(f"Datos del usuario {self.nombre} actualizados.")

    def obtener_perfil(self):
        return self.perfil_financiero

    def __str__(self):
        return f"Usuario: {self.nombre} ({self.email})"
    
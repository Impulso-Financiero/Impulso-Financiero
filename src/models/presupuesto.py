import datetime
from .usuario import Usuario
from .categoria import Categoria
from .alerta import Alerta # Para crear objetos Alerta

class Presupuesto:
    def __init__(self, id_presupuesto: int, usuario: Usuario, monto_total: float, mes: int, anio: int):
        self.id_presupuesto = id_presupuesto
        self.usuario = usuario # Objeto Usuario asociado (para crear alertas)
        self.monto_total = monto_total # Monto total presupuestado para el mes
        self.categorias = {}  # Diccionario: {Categoria.nombre: {'limite': float, 'gastado_actual': float}}
        self.mes = mes
        self.anio = anio
        self.ingreso_total_real = 0.0 # Ingresos reales para el periodo del presupuesto

    def crear_presupuesto(self, monto_total: float, limites_por_categoria: dict):
        """Define el presupuesto mensual y asigna límites por categoría."""
        self.monto_total = monto_total
        for categoria_nombre, limite in limites_por_categoria.items():
            # Asumimos que categoria_nombre es un string. Si fuera objeto Categoria, ajustar
            self.categorias[categoria_nombre] = {'limite': limite, 'gastado_actual': 0.0}
        print(f"Presupuesto {self.mes}/{self.anio} creado con éxito.")

    def modificar_limite_categoria(self, categoria_nombre: str, nuevo_limite: float):
        """Cambia el límite de una categoría específica."""
        if categoria_nombre in self.categorias:
            self.categorias[categoria_nombre]['limite'] = nuevo_limite
            print(f"Límite de categoría '{categoria_nombre}' modificado a ${nuevo_limite}.")
        else:
            print(f"Error: Categoría '{categoria_nombre}' no encontrada en este presupuesto.")

    def obtener_limite_categoria(self, categoria_nombre: str) -> float:
        """Devuelve el límite asignado a la categoría."""
        return self.categorias.get(categoria_nombre, {}).get('limite', 0.0)

    def restar_gasto(self, categoria: Categoria, monto: float) -> bool:
        """Actualiza el presupuesto restante de la categoría tras registrar un gasto y verifica sobrepaso."""
        categoria_nombre = categoria.nombre
        if categoria_nombre in self.categorias:
            self.categorias[categoria_nombre]['gastado_actual'] += monto
            print(f"Gasto de ${monto} registrado en '{categoria_nombre}'. Gastado actual: ${self.categorias[categoria_nombre]['gastado_actual']}")

            if self.alerta_sobrepaso(categoria):
                mensaje_alerta = f"¡Alerta! Has excedido el límite de ${self.categorias[categoria_nombre]['limite']} en la categoría '{categoria_nombre}' para {self.mes}/{self.anio}. Gastado: ${self.categorias[categoria_nombre]['gastado_actual']}"
                
                # Generar un ID simple para la alerta (en un sistema real usarías un generador de IDs)
                id_nueva_alerta = len(self.usuario.alertas) + 1 
                nueva_alerta = Alerta(
                    id_alerta=id_nueva_alerta, 
                    usuario=self.usuario, # Pasa el objeto Usuario
                    tipo="gasto",
                    mensaje=mensaje_alerta,
                    fecha=datetime.date.today()
                )
                self.usuario.alertas.append(nueva_alerta) # Añadir al Usuario
                nueva_alerta.enviar_notificacion()
                return True # Se generó una alerta
            return False # No se generó alerta
        else:
            print(f"Advertencia: Gasto en categoría '{categoria_nombre}' no presupuestada para {self.mes}/{self.anio}.")
            return False

    def resumen_presupuesto(self) -> str:
        """Devuelve un resumen con el total gastado y saldo restante por categoría y total."""
        resumen = f"--- Resumen Presupuesto {self.mes}/{self.anio} ---\n"
        resumen += f"Monto Total Presupuestado: ${self.monto_total}\n"
        resumen += f"Ingresos Reales Registrados: ${self.ingreso_total_real}\n"
        total_gastado_en_categorias = 0.0
        
        for cat_nombre, datos in self.categorias.items():
            resumen += f"  - {cat_nombre}: Límite {datos['limite']}$, Gastado ${datos['gastado_actual']}"
            if datos['gastado_actual'] > datos['limite']:
                resumen += " (¡LÍMITE EXCEDIDO!)\n"
            else:
                resumen += "\n"
            total_gastado_en_categorias += datos['gastado_actual']
            
        resumen += f"Total Gastado en Categorías Presupuestadas: ${total_gastado_en_categorias}\n"
        saldo_restante_estimado = self.monto_total - total_gastado_en_categorias
        resumen += f"Saldo Restante Estimado (sin considerar ingresos reales): ${saldo_restante_estimado}\n"
        return resumen

    def alerta_sobrepaso(self, categoria: Categoria) -> bool:
        """Devuelve verdadero si el gasto de la categoría supera el límite asignado."""
        categoria_nombre = categoria.nombre
        if categoria_nombre in self.categorias:
            return self.categorias[categoria_nombre]['gastado_actual'] > self.categorias[categoria_nombre]['limite']
        return False # Si la categoría no está presupuestada, no hay límite que sobrepasar

    def modificar_ingreso_total(self, monto: float):
        """Actualiza el total de ingresos reales para el periodo del presupuesto."""
        self.ingreso_total_real += monto
        print(f"Ingreso total real para {self.mes}/{self.anio} actualizado a ${self.ingreso_total_real}.")

    def __str__(self):
        return f"Presupuesto {self.mes}/{self.anio} - Total: ${self.monto_total}"

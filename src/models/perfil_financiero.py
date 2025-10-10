from __future__ import annotations 
import datetime

from typing import TYPE_CHECKING 
# Solo importa Usuario si estamos en un contexto de verificación de tipos
if TYPE_CHECKING:
    from .usuario import Usuario # Para la anotación de tipo
    from .ahorro import Ahorro
from .ingreso import Ingreso
from .gasto import Gasto
from .presupuesto import Presupuesto
from .alerta import Alerta


class PerfilFinanciero:
    def __init__(self, usuario: Usuario):
        self.usuario = usuario # Composición con Usuario
        self.ingresos_registrados = []  # Lista de objetos Ingreso
        self.gastos_registrados = []    # Lista de objetos Gasto
        self.metas_ahorro = []          # Lista de objetos Ahorro
        self.presupuestos = {}          # Diccionario: {f"mes_anio": Presupuesto_objeto}
        self.balance_actual = 0.0
        self.nivel_salud_financiera = "Desconocido" # Se calcula luego
        self.deudas_pendientes = [] 

    def agregar_ingreso(self, ingreso: Ingreso):
        """Añade un ingreso al perfil y actualiza el balance y presupuesto."""
        self.ingresos_registrados.append(ingreso)
        self.calcular_balance()
        # Si hay un presupuesto activo para el mes/año del ingreso, actualizarlo
        mes_anio_clave = f"{ingreso.fecha.month}_{ingreso.fecha.year}"
        if mes_anio_clave in self.presupuestos:
            self.presupuestos[mes_anio_clave].modificar_ingreso_total(ingreso.monto)
        print(f"Ingreso de ${ingreso.monto} registrado en Perfil Financiero.")

    def agregar_gasto(self, gasto: Gasto):
        """Añade un gasto al perfil y actualiza el balance y presupuesto."""
        self.gastos_registrados.append(gasto)
        self.calcular_balance()
        self.verificar_alertas_balance()
        # Si hay un presupuesto activo para el mes/año del gasto, restar el monto
        mes_anio_clave = f"{gasto.fecha.month}_{gasto.fecha.year}"
        if mes_anio_clave in self.presupuestos:
            self.presupuestos[mes_anio_clave].restar_gasto(gasto.categoria, gasto.monto)
            # El método restar_gasto de Presupuesto se encarga de generar la alerta si aplica
        print(f"Gasto de ${gasto.monto} registrado en Perfil Financiero.")

    def calcular_balance(self):
        """Calcula ingresos – gastos para determinar el saldo disponible."""
        total_ingresos = sum(ingreso.monto for ingreso in self.ingresos_registrados)
        total_gastos = sum(gasto.monto for gasto in self.gastos_registrados)
        self.balance_actual = total_ingresos - total_gastos
        print(f"Balance actualizado: {self.balance_actual}$")

    def calcular_nivel_salud_financiera(self):
        """Evalúa el nivel de salud financiera según balance y metas de ahorro."""
        # Lógica más compleja para evaluar la salud financiera (ej. ratios, % de ahorro)
        if self.balance_actual >= 0 and sum(a.monto_actual for a in self.metas_ahorro) > 0:
            self.nivel_salud_financiera = "Saludable"
        elif self.balance_actual < 0:
            self.nivel_salud_financiera = "En Riesgo"
        else:
            self.nivel_salud_financiera = "Normal"
        print(f"Nivel de salud financiera: {self.nivel_salud_financiera}")

    def obtener_resumen_financiero(self) -> str:
        """Devuelve un resumen completo de ingresos, gastos, ahorro y nivel de salud financiera."""
        resumen = f"--- Resumen Financiero de {self.usuario.nombre} ---\n"
        resumen += f"Balance Actual: {self.balance_actual}$\n"
        #resumen += f"Nivel de Salud Financiera: {self.nivel_salud_financiera}\n"
        resumen += "\nIngresos Registrados:\n"
        for i in self.ingresos_registrados:
            resumen += f"  - {i.obtener_detalle()}\n"
        resumen += "\nGastos Registrados:\n"
        for g in self.gastos_registrados:
            resumen += f"  - {g.obtener_detalle()}\n"
        resumen += "\nMetas de Ahorro:\n"
        if not self.metas_ahorro:
            resumen += "  No hay metas de ahorro definidas.\n"
        else:
            for a in self.metas_ahorro:
                resumen += f"  - {a.estado_ahorro()}\n"
        return resumen
    
    def agregar_ahorro(self, ahorro: Ahorro):
        """Agrega una meta de ahorro a la lista del perfil."""
        self.metas_ahorro.append(ahorro)
        
    def agregar_presupuesto(self, presupuesto: Presupuesto):
        """Agrega un presupuesto al perfil financiero."""
        clave = f"{presupuesto.mes}_{presupuesto.anio}"
        self.presupuestos[clave] = presupuesto
        print(f"Presupuesto {presupuesto.mes}/{presupuesto.anio} agregado al perfil.")

    def obtener_resumen_financiero_presupuesto(self, mes: int, anio: int) -> str:
        """Obtiene el resumen de presupuesto para un mes y año específicos."""
        clave = f"{mes}_{anio}"
        if clave in self.presupuestos:
            return self.presupuestos[clave].resumen_presupuesto()
        return f"No hay presupuesto configurado para {mes}/{anio}."
    
    def obtener_datos_agregados_para_reglas(self, mes: int, anio: int) -> dict:
        """
        Recopila y agrega los datos necesarios de PerfilFinanciero
        para que la clase ReglasLogicas pueda evaluarlos.
        """
        gastos_total_mes = 0.0
        ingreso_total_mes = 0.0
        gastos_delivery_mes = 0.0
        gastos_ocio_mes = 0.0

        # Filtrar transacciones del mes y año específicos
        transacciones_mes_actual = [
            t for t in self.ingresos_registrados + self.gastos_registrados
            if t.fecha.month == mes and t.fecha.year == anio
        ]

        # Calcular agregados
        for t in transacciones_mes_actual:
            if isinstance(t, Gasto):
                gastos_total_mes += t.monto
                # Asumiendo que 'Delivery' y 'Entretenimiento' son categorías de gasto
                if t.categoria.nombre == "Delivery":
                    gastos_delivery_mes += t.monto
                if t.categoria.nombre == "Entretenimiento":
                    gastos_ocio_mes += t.monto
            elif isinstance(t, Ingreso):
                ingreso_total_mes += t.monto
        
        # Calcular ahorro_mensual y ahorro_excedente para el mes
        ahorro_mensual_calculado = ingreso_total_mes - gastos_total_mes
        # Esto es una simplificación, tu lógica de ahorro_excedente real puede ser más compleja
        ahorro_objetivo_pct = 0.10 # Ejemplo: objetivo del 10% de ahorro
        ahorro_excedente_calculado = max(0, ahorro_mensual_calculado - (ingreso_total_mes * ahorro_objetivo_pct))
        
        return {
            'gastos_total': gastos_total_mes,
            'ingreso': ingreso_total_mes,
            'ahorro_mensual': ahorro_mensual_calculado,
            'gastos_delivery': gastos_delivery_mes,
            'gastos_ocio': gastos_ocio_mes,
            'ahorro_excedente': ahorro_excedente_calculado,
            # Añadir más datos según necesiten tus reglas (ej. total deuda, etc.)
        }
    
    def verificar_alertas_balance(self):
        """Genera una alerta si el balance actual es negativo."""
        if self.balance_actual < 0:
            mensaje = f"⚠️ Alerta: tu balance actual es negativo: ${self.balance_actual:.2f}"
            
            # Crear alerta
            id_alerta = len(self.usuario.alertas) + 1
            alerta = Alerta(
                id_alerta=id_alerta,
                usuario=self.usuario,
                tipo="balance",
                mensaje=mensaje,
                fecha=datetime.date.today()
            )
            self.usuario.alertas.append(alerta)
            alerta.enviar_notificacion()
            
    def obtener_ahorro_actual(self) -> float:
        """Devuelve el balance actual como una medida de ahorro inicial."""
        return self.balance_actual

    def obtener_deuda_total(self) -> float:
        """Calcula y devuelve el total de las deudas pendientes."""
        return sum(deuda.monto for deuda in self.deudas_pendientes)

    def obtener_resumen_ahorro_y_recomendaciones(self) -> str:
        """Evalúa el ahorro y genera recomendaciones."""
        resumen_total_ahorros = ""
        recomendaciones_list = []  # Usamos una lista para almacenar las recomendaciones

        if self.metas_ahorro:
            for meta_ahorro in self.metas_ahorro:
                # Resumen individual del estado de cada ahorro
                resumen_estado_individual = meta_ahorro.estado_ahorro()
                progreso_individual = meta_ahorro.calcular_progreso()
                resumen_total_ahorros += f"- {resumen_estado_individual} (Progreso: {progreso_individual:.2f}%)\n"

                # Genera la recomendación para la meta actual
                recomendacion_individual = meta_ahorro.recomendacion_mensual()
                recomendaciones_list.append(recomendacion_individual)

                # Une todas las recomendaciones en una sola cadena
                recomendaciones = "\n".join(recomendaciones_list)
        else:
            resumen_total_ahorros = "No hay metas de ahorro definidas."
            recomendaciones = "Define una meta de ahorro para recibir recomendaciones."

        return f"--- Resumen de Ahorros ---\n{resumen_total_ahorros}\n--- Recomendaciones ---\n{recomendaciones}"

    def __str__(self):
        return f"Perfil Financiero de {self.usuario.nombre}"
    
import datetime

class Ahorro:
    def __init__(self, id_ahorro: int, monto_actual: float, meta: float, tipo: str, fecha_inicio: datetime.date, fecha_meta: datetime.date):
        self.id_ahorro = id_ahorro
        self.monto_actual = monto_actual
        self.meta = meta
        self.tipo = tipo # Ej: "Emergencia", "Inversión", "Viaje"
        self.fecha_inicio = fecha_inicio
        self.fecha_meta = fecha_meta

    def agregar_monto(self, monto: float):
        """Suma un monto al ahorro actual."""
        if monto > 0:
            self.monto_actual += monto
            print(f"Se agregaron ${monto} al ahorro {self.id_ahorro}. Nuevo total: ${self.monto_actual}")
        else:
            print("El monto a agregar debe ser positivo.")

    def retirar_monto(self, monto: float):
        """Resta un monto del ahorro actual, si hay fondos suficientes."""
        if 0 < monto <= self.monto_actual:
            self.monto_actual -= monto
            print(f"Se retiraron ${monto} del ahorro {self.id_ahorro}. Nuevo total: ${self.monto_actual}")
        else:
            print("Monto de retiro inválido o insuficiente.")

    def calcular_progreso(self) -> float:
        """Calcula el porcentaje de la meta alcanzado."""
        if self.meta > 0:
            return (self.monto_actual / self.meta) * 100
        return 0.0 # Si la meta es 0, no hay progreso calculado

    def simular_meta(self, monto_objetivo: float, meses: int) -> float:
        """Simula cuánto se necesita ahorrar por mes para cumplir una meta."""
        if meses > 0:
            monto_restante = monto_objetivo - self.monto_actual
            if monto_restante > 0:
                return monto_restante / meses
        return 0.0

    def recomendacion_mensual(self) -> str:
        """
        Genera una recomendación sobre cuánto ahorrar cada mes para alcanzar la meta.
        """
        hoy = datetime.date.today()

        if self.fecha_meta is None or self.fecha_meta <= hoy:
            return f"¡Tu meta '{self.tipo}' ya pasó o no tiene fecha límite! Por favor, actualiza la fecha."

        # Calcula el número de meses restantes.
        meses_restantes = (self.fecha_meta.year - hoy.year) * 12 + (self.fecha_meta.month - hoy.month)
        if meses_restantes <= 0:
            return f"¡Tu meta '{self.tipo}' ya debería haberse cumplido! Revisa tu plazo."

        monto_pendiente = self.meta - self.monto_actual

        if monto_pendiente <= 0:
            return f"¡Felicidades! Ya alcanzaste o superaste tu meta de {self.tipo}."

        monto_sugerido = monto_pendiente / meses_restantes

        return f"Para alcanzar tu meta de {self.tipo} de ${self.meta:.2f}, se recomienda ahorrar al menos ${monto_sugerido:.2f} mensuales."
    
    def estado_ahorro(self) -> str:
        """Devuelve un resumen simple del estado actual y la meta del ahorro."""
        progreso = self.calcular_progreso()
        fecha_actual = datetime.date.today()
        return f"Ahorro ID: {self.id_ahorro}, Actual: ${self.monto_actual}, Meta: ${self.meta}, Progreso: {progreso:.2f}%, Fecha actual: {fecha_actual}, Fecha de Finalización: {self.fecha_meta}"

    def __str__(self):
        return f"Meta de Ahorro: {self.meta}$, Actual: ${self.monto_actual}"

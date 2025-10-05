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

    def recomendacion_mensual(self, ingresos_netos: float, gastos_fijos: float) -> str:
        """Genera una recomendación sobre cuánto ahorrar cada mes."""
        # Esta lógica es simplificada
        monto_sugerido = (ingresos_netos - gastos_fijos) * 0.10 # Sugerir un 10% del saldo disponible
        if monto_sugerido > 0:
            return f"Se recomienda ahorrar al menos ${monto_sugerido:.2f} mensuales para tus metas."
        return "Considera ajustar tus finanzas para poder ahorrar."

    def estado_ahorro(self) -> str:
        """Devuelve un resumen simple del estado actual y la meta del ahorro."""
        progreso = self.calcular_progreso()
        return f"Ahorro ID: {self.id_ahorro}, Actual: ${self.monto_actual}, Meta: ${self.meta}, Progreso: {progreso:.2f}%"

    def __str__(self):
        return f"Meta de Ahorro: {self.meta}$, Actual: ${self.monto_actual}"

from typing import List, Union
from .gasto import Gasto
from .ingreso import Ingreso
from .categoria import Categoria

class ProyeccionesFinancieras:
    """
    Implementa sucesiones aritméticas, geométricas y principios de conteo
    """
    
    @staticmethod
    def sucesion_aritmetica_ahorro(ahorro_inicial: float, aporte_mensual: float, meses: int):
        """
        Ejemplo del ABP: an = a1 + (n-1) * d
        Si ahorro_mensual = $20,000 por 12 meses:
        a12 = 20000 + (12-1) * 20000 = $240,000
        """
        # La fórmula an = a1 + (n-1) * d calcula el término n-ésimo, no el total acumulado
        # Si a1 es el primer aporte (no el ahorro_inicial previo), entonces:
        # ahorro_total = ahorro_inicial + (meses * aporte_mensual)  <-- Esta calcula el total simple
        # Para la sucesión aritmética acumulada:
        
        proyeccion = []
        for mes in range(1, meses + 1):
            # Acumulado después del aporte del mes 'mes'
            valor_acumulado = ahorro_inicial + (aporte_mensual * mes) 
            proyeccion.append({
                'mes': mes,
                'aporte': aporte_mensual, # El aporte en ese mes
                'acumulado': valor_acumulado # El total acumulado hasta ese mes
            })
        
        ahorro_total_final = ahorro_inicial + (aporte_mensual * meses) # Total simple acumulado
        
        return ahorro_total_final, proyeccion # Retornamos el total final y la proyección detallada
    
    @staticmethod
    def interes_compuesto(capital_inicial: float, tasa_mensual: float, meses: int):
        """
        Sucesión Geométrica: F = P(1 + i)^n
        Para modelar rendimiento de inversiones
        """
        monto_final = capital_inicial * ((1 + tasa_mensual) ** meses)
        return monto_final
    
    @staticmethod
    def amortizacion_francesa(deuda_total: float, tasa_mensual: float, cuotas: int):
        """
        Cuota = P * [i(1+i)^n] / [(1+i)^n - 1]
        Para estrategia de eliminación de deudas
        """
        if tasa_mensual == 0:
            return deuda_total / cuotas
        
        # Ajuste a la fórmula para evitar errores si tasa_mensual es muy cercana a 0 pero no 0
        if cuotas == 0: # Evitar división por cero si no hay cuotas
            return 0 

        factor_numerador = tasa_mensual * ((1 + tasa_mensual) ** cuotas)
        factor_denominador = ((1 + tasa_mensual) ** cuotas) - 1
        
        # Cuidado con factor_denominador siendo muy pequeño o cero si tasa_mensual es casi cero
        if factor_denominador == 0: # Esto debería ocurrir solo si tasa_mensual es 0, ya manejado arriba
             return float('inf') # O manejar como un error o caso especial
             
        cuota_mensual = deuda_total * (factor_numerador / factor_denominador)
        
        return cuota_mensual
    
    @staticmethod
    def impacto_inflacion(ahorro_actual: float, tasa_inflacion_anual: float, meses: int):
        """
        Calcula pérdida de poder adquisitivo
        """
        # Convertir tasa anual a mensual y a decimal
        tasa_inflacion_mensual = (tasa_inflacion_anual / 100) / 12 
        
        poder_adquisitivo = ahorro_actual / ((1 + tasa_inflacion_mensual) ** meses)
        perdida = ahorro_actual - poder_adquisitivo
        
        return {
            'poder_adquisitivo_final': poder_adquisitivo,
            'perdida_por_inflacion': perdida,
            'porcentaje_perdida': (perdida / ahorro_actual) * 100 if ahorro_actual else 0
        }
    
    @staticmethod
    def contar_frecuencia_categoria(transacciones: List[Union['Gasto', 'Ingreso']], categoria_objeto: 'Categoria'):
        """
        Principio de Conteo: Analiza frecuencia de eventos
        Acepta una lista de objetos Gasto/Ingreso y un objeto Categoria.
        """
        # Asegúrate de que las transacciones sean objetos y tengan un atributo 'categoria' que sea un objeto Categoria
        return sum(1 for t in transacciones if t.categoria.nombre == categoria_objeto.nombre)
    
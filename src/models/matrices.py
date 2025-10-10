import numpy as np

class AlgebraLinealFinanciera:
    """
    Usa matrices y vectores para estructurar y analizar datos financieros
    """
    
    @staticmethod
    def crear_matriz_gastos(datos_categorias, meses):
        """
        Crea matriz donde:
        - Filas = Categorías (Alimentación, Servicios, Transporte, Ocio)
        - Columnas = Meses
        
        Ejemplo del ABP:
        [[50000, 55000, 60000],  # Alimentación
         [30000, 32000, 35000],  # Servicios
         [20000, 22000, 25000]]  # Transporte
        """
        return np.array(datos_categorias)
    
    def sumar_matrices_trimestres(self, matriz_trim1, matriz_trim2):
        """
        Operación: Calcular gasto total semestral
        Gastos_Semestre = Gastos_Trimestre1 + Gastos_Trimestre2
        """
        return matriz_trim1 + matriz_trim2
    
    @staticmethod
    def gasto_total_mensual(matriz_gastos):
        """
        Vector resultante: Suma vertical (por columnas)
        Retorna vector con gasto total de cada mes
        """
        return np.sum(matriz_gastos, axis=0)
    
    @staticmethod
    def gasto_total_categoria(matriz_gastos):
        """
        Vector resultante: Suma horizontal (por filas)
        Retorna vector con gasto total de cada categoría
        """
        return np.sum(matriz_gastos, axis=1)
    
    def analisis_matricial_completo(self, matriz_gastos, categorias, meses):
        """
        Genera reporte completo usando álgebra lineal
        """
        total_mensual = self.gasto_total_mensual(matriz_gastos)
        total_categoria = self.gasto_total_categoria(matriz_gastos)
        total_general = np.sum(matriz_gastos)
        
        # Porcentajes por categoría
        porcentajes = (total_categoria / total_general) * 100
        
        return {
            'matriz_original': matriz_gastos,
            'total_por_mes': total_mensual,
            'total_por_categoria': total_categoria,
            'total_general': total_general,
            'porcentajes_categoria': dict(zip(categorias, porcentajes)),
            'categoria_mayor_gasto': categorias[np.argmax(total_categoria)],
            'mes_mayor_gasto': meses[np.argmax(total_mensual)]
        }
    
    @staticmethod
    def vector_transaccion(monto, categoria_id, fecha):
        """
        Representa una transacción como vector [monto, categoría, fecha]
        Facilita procesamiento y optimización
        """
        return np.array([monto, categoria_id, fecha])
    
import statistics

class AnalisisEstadistico:
    """
    Análisis estadístico de transacciones
    """
    
    @staticmethod
    def resumen_financiero(transacciones):
        """Genera resumen estadístico completo"""
        montos = [t['monto'] for t in transacciones if t['tipo'] == 'gasto']
        
        if not montos:
            return {}
        
        return {
            'media': statistics.mean(montos),
            'mediana': statistics.median(montos),
            'moda': statistics.mode(montos) if len(set(montos)) < len(montos) else None,
            'desviacion_estandar': statistics.stdev(montos) if len(montos) > 1 else 0,
            'rango': max(montos) - min(montos),
            'total_gastos': sum(montos),
            'cantidad_transacciones': len(montos)
        }
    
    @staticmethod
    def porcentaje_por_categoria(transacciones):
        """Calcula distribución porcentual de gastos"""
        gastos_por_categoria = {}
        total_gastos = 0
        
        for t in transacciones:
            if t['tipo'] == 'gasto':
                cat = t['categoria']
                gastos_por_categoria[cat] = gastos_por_categoria.get(cat, 0) + t['monto']
                total_gastos += t['monto']
        
        if total_gastos == 0:
            return {}
        
        return {
            cat: {
                'monto': monto,
                'porcentaje': (monto / total_gastos) * 100
            }
            for cat, monto in gastos_por_categoria.items()
        }

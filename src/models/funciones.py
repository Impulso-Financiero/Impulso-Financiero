class FuncionesMatematicas:
    """
    Implementa funciones lineales f(x) = mx + b y cuadráticas f(x) = ax² + bx + c
    para modelado de escenarios financieros
    """
    
    @staticmethod
    def funcion_lineal(x, m, b):
        """
        f(x) = mx + b
        Modela tasa de ahorro o endeudamiento constante
        
        Parámetros:
        - x: tiempo (meses)
        - m: pendiente (tasa de cambio, ej. ahorro mensual)
        - b: intercepto (saldo inicial)
        """
        return m * x + b
    
    def modelar_ahorro_lineal(self, meses, ahorro_mensual, saldo_inicial):
        """
        Ejemplo del ABP: Modelar ahorro con función lineal
        Y = ahorro_mensual * X + saldo_inicial
        """
        proyeccion = []
        for mes in range(0, meses + 1):
            saldo = self.funcion_lineal(mes, ahorro_mensual, saldo_inicial)
            proyeccion.append({
                'mes': mes,
                'saldo': saldo
            })
        
        return proyeccion
    
    @staticmethod
    def funcion_cuadratica(x, a, b, c):
        """
        f(x) = ax² + bx + c
        Para optimización de rendimiento de inversiones
        """
        return a * (x ** 2) + b * x + c
    
    @staticmethod
    def calcular_vertice(a, b, c):
        """
        Encuentra el punto óptimo (vértice) de una parábola
        
        Vértice: x = -b/(2a)
        
        Aplicación ABP: Maximizar ahorro o minimizar impacto de gasto variable
        """
        if a == 0:
            return None, "No es una función cuadrática"
        
        x_vertice = -b / (2 * a)
        y_vertice = a * (x_vertice ** 2) + b * x_vertice + c
        
        tipo = "máximo" if a < 0 else "mínimo"
        
        return {
            'x_optimo': x_vertice,
            'y_optimo': y_vertice,
            'tipo': tipo
        }
    
    def optimizar_inversion(self, a, b, c):
        """
        Ejemplo: Encuentra el tiempo óptimo para una inversión
        donde el rendimiento sigue f(x) = ax² + bx + c
        """
        vertice = self.calcular_vertice(a, b, c)
        
        if vertice:
            return {
                'meses_optimos': vertice['x_optimo'],
                'rendimiento_maximo': vertice['y_optimo'],
                'interpretacion': f"El {vertice['tipo']} rendimiento se alcanza en {vertice['x_optimo']:.1f} meses"
            }
        
        return None
    
    @staticmethod
    def definir_dominio_imagen(funcion_tipo, rango_ingresos):
        """
        Define Dominio (ingresos posibles) e Imagen (gastos/ahorros resultantes)
        para asegurar coherencia financiera
        
        Ejemplo ABP: Dominio = [ingresos mínimos, máximos]
        """
        if funcion_tipo == 'lineal':
            return {
                'dominio': f"Ingresos mensuales en rango {rango_ingresos}",
                'imagen': "Montos de ahorro/gasto coherentes con ingresos",
                'restriccion': "Gastos no pueden superar ingresos (realidad financiera)"
            }

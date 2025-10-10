class AnalisisDerivadas:
    """
    Implementa cálculo de derivadas (tasas de cambio) para
    análisis predictivo y alertas proactivas
    """
    
    @staticmethod
    def derivada_discreta(valor_anterior, valor_actual, delta_tiempo=1):
        """
        Aproximación de derivada: f'(x) ≈ Δy/Δx
        
        Tasa de Cambio = (Saldo(t2) - Saldo(t1)) / (t2 - t1)
        """
        return (valor_actual - valor_anterior) / delta_tiempo
    
    def calcular_tasa_vulnerabilidad(self, saldo_mes_anterior, saldo_actual):
        """
        R3: Riesgo de Endeudamiento Inminente (Proactivo)
        
        Aplica derivada para medir velocidad de agotamiento del presupuesto
        """
        tasa = self.derivada_discreta(saldo_mes_anterior, saldo_actual)
        
        # Umbrales de riesgo
        if tasa < -20000:
            nivel_riesgo = "CRÍTICO"
            mensaje = "La tasa de vulnerabilidad es muy alta. El saldo disminuye rápidamente."
        elif tasa < -10000:
            nivel_riesgo = "ALTO"
            mensaje = "Tendencia negativa significativa en el saldo."
        elif tasa < 0:
            nivel_riesgo = "MODERADO"
            mensaje = "El saldo está disminuyendo."
        else:
            nivel_riesgo = "ESTABLE"
            mensaje = "Situación financiera estable o mejorando."
        
        return {
            'tasa_cambio': tasa,
            'nivel_riesgo': nivel_riesgo,
            'mensaje': mensaje,
            'alerta_proactiva': nivel_riesgo in ["CRÍTICO", "ALTO"]
        }
    
    def proyectar_tendencia(self, historial_saldos):
        """
        Usa derivadas para proyectar cuándo el saldo llegará a cero
        """
        if len(historial_saldos) < 2:
            return None
        
        # Calcular tasa promedio de cambio
        tasas = []
        for i in range(1, len(historial_saldos)):
            tasa = self.derivada_discreta(historial_saldos[i-1], historial_saldos[i])
            tasas.append(tasa)
        
        tasa_promedio = sum(tasas) / len(tasas)
        saldo_actual = historial_saldos[-1]
        
        if tasa_promedio >= 0:
            return {
                'tendencia': 'positiva',
                'meses_hasta_cero': None,
                'mensaje': 'El saldo está creciendo o estable'
            }
        
        # Proyectar meses hasta llegar a cero
        meses_hasta_cero = abs(saldo_actual / tasa_promedio)
        
        return {
            'tendencia': 'negativa',
            'tasa_promedio': tasa_promedio,
            'meses_hasta_cero': meses_hasta_cero,
            'mensaje': f'Al ritmo actual, el saldo llegará a cero en {meses_hasta_cero:.1f} meses'
        }
    
    @staticmethod
    def verificar_continuidad(historial_saldos):
        """
        Asegura que el modelo de simulación sea estable y predecible
        
        Continuidad: La función puede trazarse sin levantar el lápiz
        En finanzas: Sin saltos bruscos inexplicables en el saldo
        """
        if len(historial_saldos) < 3:
            return True, "Datos insuficientes para verificar continuidad"
        
        cambios = []
        for i in range(1, len(historial_saldos)):
            cambio = abs(historial_saldos[i] - historial_saldos[i-1])
            cambios.append(cambio)
        
        # Detectar saltos bruscos (cambios > 5x el cambio promedio)
        cambio_promedio = sum(cambios) / len(cambios)
        saltos_bruscos = [c for c in cambios if c > cambio_promedio * 5]
        
        if saltos_bruscos:
            return False, f"Se detectaron {len(saltos_bruscos)} saltos bruscos. Revisar transacciones."
        
        return True, "El modelo presenta continuidad adecuada"
    
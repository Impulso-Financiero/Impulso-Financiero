from src.models.derivadas import AnalisisDerivadas

def test_derivada_discreta():
    tasa = AnalisisDerivadas.derivada_discreta(1000, 1100, 1)
    assert tasa == 100

def test_calcular_tasa_vulnerabilidad():
    # Caso 1: Crítico
    analisis_critico = AnalisisDerivadas().calcular_tasa_vulnerabilidad(200000, 150000)
    assert analisis_critico['nivel_riesgo'] == "CRÍTICO"
    assert analisis_critico['alerta_proactiva'] is True
    
    # Caso 2: Alto
    analisis_alto = AnalisisDerivadas().calcular_tasa_vulnerabilidad(100000, 95000)
    assert analisis_alto['nivel_riesgo'] == "ALTO"
    assert analisis_alto['alerta_proactiva'] is True
    
    # Caso 3: Moderado
    analisis_moderado = AnalisisDerivadas().calcular_tasa_vulnerabilidad(50000, 49000)
    assert analisis_moderado['nivel_riesgo'] == "MODERADO"
    assert analisis_moderado['alerta_proactiva'] is False
    
    # Caso 4: Estable
    analisis_estable = AnalisisDerivadas().calcular_tasa_vulnerabilidad(50000, 51000)
    assert analisis_estable['nivel_riesgo'] == "ESTABLE"
    assert analisis_estable['alerta_proactiva'] is False

def test_proyectar_tendencia():
    # Tendencia negativa
    historial_negativo = [1000, 900, 800]
    tendencia_negativa = AnalisisDerivadas().proyectar_tendencia(historial_negativo)
    assert tendencia_negativa['tendencia'] == 'negativa'
    assert tendencia_negativa['meses_hasta_cero'] == 8.0 # 800 / 100 = 8
    
    # Tendencia positiva
    historial_positivo = [1000, 1100, 1200]
    tendencia_positiva = AnalisisDerivadas().proyectar_tendencia(historial_positivo)
    assert tendencia_positiva['tendencia'] == 'positiva'
    assert tendencia_positiva['meses_hasta_cero'] is None
    
    # Datos insuficientes
    tendencia_insuficiente = AnalisisDerivadas().proyectar_tendencia([1000])
    assert tendencia_insuficiente is None
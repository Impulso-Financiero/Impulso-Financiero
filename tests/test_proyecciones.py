import pytest
from src.models.proyecciones import ProyeccionesFinancieras

def test_sucesion_aritmetica_ahorro():
    proy = ProyeccionesFinancieras()
    total, detalle = proy.sucesion_aritmetica_ahorro(ahorro_inicial=1000, aporte_mensual=100, meses=3)
    
    assert total == 1300
    assert len(detalle) == 3
    assert detalle[2]['acumulado'] == 1300

def test_interes_compuesto():
    proy = ProyeccionesFinancieras()
    monto_final = proy.interes_compuesto(capital_inicial=1000, tasa_mensual=0.01, meses=3)
    assert monto_final == pytest.approx(1030.301, 0.001)

def test_amortizacion_francesa():
    proy = ProyeccionesFinancieras()
    cuota = proy.amortizacion_francesa(deuda_total=10000, tasa_mensual=0.01, cuotas=12)
    assert cuota == pytest.approx(888.487, 0.001)

def test_impacto_inflacion():
    proy = ProyeccionesFinancieras()
    resultado = proy.impacto_inflacion(ahorro_actual=10000, tasa_inflacion_anual=5.0, meses=12)
    
    assert resultado['poder_adquisitivo_final'] == pytest.approx(9513.06, 0.01)
    assert resultado['perdida_por_inflacion'] == pytest.approx(486.94, 0.01)

def test_contar_frecuencia_categoria():
    proy = ProyeccionesFinancieras()
    
    class MockCategoria:
        def __init__(self, nombre):
            self.nombre = nombre
            
    class MockTransaccion:
        def __init__(self, monto, categoria):
            self.monto = monto
            self.categoria = categoria
            
    cat_comida = MockCategoria("Comida")
    cat_transporte = MockCategoria("Transporte")
    
    transacciones = [
        MockTransaccion(100, cat_comida),
        MockTransaccion(50, cat_comida),
        MockTransaccion(20, cat_transporte),
    ]
    
    frecuencia = proy.contar_frecuencia_categoria(transacciones, cat_comida)
    assert frecuencia == 2
    
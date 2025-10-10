import pytest
from src.models.reglas_logicas import ReglasLogicas

def test_evaluar_regla_and():
    # Todas las condiciones se cumplen
    assert ReglasLogicas.evaluar_regla([(10, '>', 5), (20, '<', 30)], operador='AND') is True
    # Una condición no se cumple
    assert ReglasLogicas.evaluar_regla([(10, '>', 5), (20, '<', 15)], operador='AND') is False

def test_evaluar_regla_or():
    # Una condición se cumple
    assert ReglasLogicas.evaluar_regla([(10, '>', 5), (20, '<', 15)], operador='OR') is True
    # Ninguna condición se cumple
    assert ReglasLogicas.evaluar_regla([(10, '<', 5), (20, '<', 15)], operador='OR') is False

def test_generar_alerta_financiera():
    reglas = ReglasLogicas()
    
    # Caso R1: Gastos > 80% ingreso
    perfil_datos_r1 = {'gastos_total': 1800, 'ingreso': 2000}
    alertas_r1 = reglas.generar_alerta_financiera(perfil_datos_r1)
    assert any("ALERTA R1" in msg for msg in alertas_r1)
    
    # Caso R2: Gastos no esenciales > 15% ingreso y ahorro < 5% ingreso
    perfil_datos_r2 = {'gastos_total': 1500, 'ingreso': 2000, 'gastos_delivery': 350, 'gastos_ocio': 200, 'ahorro_mensual': 50}
    alertas_r2 = reglas.generar_alerta_financiera(perfil_datos_r2)
    assert any("SUGERENCIA R2" in msg for msg in alertas_r2)
    
    # Caso R4: Ahorro excedente
    perfil_datos_r4 = {'ahorro_excedente': 100}
    alertas_r4 = reglas.generar_alerta_financiera(perfil_datos_r4)
    assert any("OPORTUNIDAD R4" in msg for msg in alertas_r4)
    
def test_cuantificador_existencial():
    transacciones = ["gasto1", "gasto2", "ingreso1"]
    condicion_gasto = lambda t: "gasto" in t
    
    assert ReglasLogicas.cuantificador_existencial(transacciones, condicion_gasto) is True

def test_cuantificador_universal():
    transacciones_solo_gastos = ["gasto1", "gasto2"]
    condicion_gasto = lambda t: "gasto" in t
    
    assert ReglasLogicas.cuantificador_universal(transacciones_solo_gastos, condicion_gasto) is True
    
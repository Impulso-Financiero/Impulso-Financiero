import pytest
import statistics
from src.models.estadistica import AnalisisEstadistico

def test_resumen_financiero():
    transacciones_gastos = [
        {'monto': 100, 'tipo': 'gasto'},
        {'monto': 50, 'tipo': 'gasto'},
        {'monto': 100, 'tipo': 'gasto'},
        {'monto': 200, 'tipo': 'gasto'}
    ]
    
    resumen = AnalisisEstadistico.resumen_financiero(transacciones_gastos)
    
    assert resumen['media'] == 112.5
    assert resumen['mediana'] == 100.0
    assert resumen['moda'] == 100
    assert resumen['total_gastos'] == 450
    assert resumen['cantidad_transacciones'] == 4

def test_porcentaje_por_categoria():
    transacciones_mixtas = [
        {'monto': 100, 'categoria': 'Alimentación', 'tipo': 'gasto'},
        {'monto': 50, 'categoria': 'Transporte', 'tipo': 'gasto'},
        {'monto': 1500, 'categoria': 'Salario', 'tipo': 'ingreso'},
        {'monto': 200, 'categoria': 'Alimentación', 'tipo': 'gasto'}
    ]
    
    porcentajes = AnalisisEstadistico.porcentaje_por_categoria(transacciones_mixtas)
    
    assert 'Alimentación' in porcentajes
    assert 'Transporte' in porcentajes
    assert porcentajes['Alimentación']['porcentaje'] == pytest.approx(66.67, 0.01)
    assert porcentajes['Transporte']['porcentaje'] == pytest.approx(33.33, 0.01)

def test_resumen_vacio():
    resumen = AnalisisEstadistico.resumen_financiero([])
    assert resumen == {}
    
    porcentajes = AnalisisEstadistico.porcentaje_por_categoria([])
    assert porcentajes == {}
    
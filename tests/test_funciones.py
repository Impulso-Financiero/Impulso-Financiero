import pytest
from src.models.funciones import FuncionesMatematicas

def test_funcion_lineal():
    resultado = FuncionesMatematicas.funcion_lineal(x=10, m=5, b=100)
    assert resultado == 150

def test_modelar_ahorro_lineal():
    funciones = FuncionesMatematicas()
    proyeccion = funciones.modelar_ahorro_lineal(meses=3, ahorro_mensual=100, saldo_inicial=500)
    
    assert len(proyeccion) == 4 # Incluye el mes 0
    assert proyeccion[0]['saldo'] == 500
    assert proyeccion[3]['saldo'] == 800

def test_funcion_cuadratica():
    resultado = FuncionesMatematicas.funcion_cuadratica(x=2, a=2, b=3, c=1)
    assert resultado == 15 # 2*(2^2) + 3*2 + 1 = 8 + 6 + 1

def test_calcular_vertice():
    # Parábola hacia arriba (mínimo)
    vertice_minimo = FuncionesMatematicas.calcular_vertice(a=1, b=-2, c=1)
    assert vertice_minimo['x_optimo'] == 1.0
    assert vertice_minimo['y_optimo'] == 0.0
    assert vertice_minimo['tipo'] == "mínimo"
    
    # Parábola hacia abajo (máximo)
    vertice_maximo = FuncionesMatematicas.calcular_vertice(a=-1, b=2, c=1)
    assert vertice_maximo['x_optimo'] == 1.0
    assert vertice_maximo['y_optimo'] == 2.0
    assert vertice_maximo['tipo'] == "máximo"

def test_optimizar_inversion():
    funciones = FuncionesMatematicas()
    optimizacion = funciones.optimizar_inversion(a=-1, b=10, c=0)
    
    assert optimizacion['meses_optimos'] == 5.0
    assert optimizacion['rendimiento_maximo'] == 25.0
    
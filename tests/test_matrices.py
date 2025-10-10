import numpy as np
from src.models.matrices import AlgebraLinealFinanciera

def test_crear_matriz_gastos():
    datos_categorias = [[50000, 55000], [30000, 32000]]
    matriz = AlgebraLinealFinanciera.crear_matriz_gastos(datos_categorias, meses=2)
    assert np.array_equal(matriz, np.array([[50000, 55000], [30000, 32000]]))

def test_sumar_matrices_trimestres():
    matriz_trim1 = np.array([[1, 2], [3, 4]])
    matriz_trim2 = np.array([[5, 6], [7, 8]])
    suma = AlgebraLinealFinanciera().sumar_matrices_trimestres(matriz_trim1, matriz_trim2)
    assert np.array_equal(suma, np.array([[6, 8], [10, 12]]))

def test_gasto_total_mensual():
    matriz = np.array([[50000, 55000, 60000], [30000, 32000, 35000]])
    total_mensual = AlgebraLinealFinanciera().gasto_total_mensual(matriz)
    assert np.array_equal(total_mensual, np.array([80000, 87000, 95000]))

def test_gasto_total_categoria():
    matriz = np.array([[50000, 55000, 60000], [30000, 32000, 35000]])
    total_categoria = AlgebraLinealFinanciera().gasto_total_categoria(matriz)
    assert np.array_equal(total_categoria, np.array([165000, 97000]))
    
import datetime
from src.models.conjuntos_financieros import ConjuntosFinancieros
from src.models.categoria import Categoria
from src.models.ingreso import Ingreso
from src.models.gasto import Gasto

def test_filtrar_por_categoria():
    categoria_ingreso = Categoria(1, "Salario", "Ingreso")
    categoria_gasto = Categoria(101, "Comida", "Gasto")
    
    transacciones = [
        Ingreso(1, 1000, categoria_ingreso, datetime.date.today(), "Fijo"),
        Gasto(2, 50, categoria_gasto, datetime.date.today(), "Variable", "Comida rápida"),
        Gasto(3, 20, categoria_gasto, datetime.date.today(), "Variable", "Café")
    ]
    
    conjuntos = ConjuntosFinancieros(transacciones)
    
    # Test para la categoría de gasto
    ids_gastos = conjuntos.filtrar_por_categoria(categoria_gasto)
    assert ids_gastos == {2, 3}
    
    # Test para la categoría de ingreso
    ids_ingresos = conjuntos.filtrar_por_categoria(categoria_ingreso)
    assert ids_ingresos == {1}

def test_interseccion_union_diferencia():
    categoria_gasto1 = Categoria(101, "Comida", "Gasto")
    categoria_gasto2 = Categoria(102, "Transporte", "Gasto")
    
    transacciones = [
        Gasto(1, 50, categoria_gasto1, datetime.date.today(), "Variable", "Comida"),
        Gasto(2, 100, categoria_gasto1, datetime.date.today(), "Fijo", "Comida recurrente"),
        Gasto(3, 25, categoria_gasto2, datetime.date.today(), "Variable", "Gasolina")
    ]
    
    conjuntos = ConjuntosFinancieros(transacciones)
    
    # Intersección (debería ser vacía)
    interseccion = conjuntos.interseccion_gastos(categoria_gasto1, categoria_gasto2)
    assert interseccion == set()
    
    # Unión
    union = conjuntos.union_categorias(categoria_gasto1, categoria_gasto2)
    assert union == {1, 2, 3}
    
    # Diferencia
    diferencia = conjuntos.diferencia_gastos(categoria_gasto1, categoria_gasto2)
    assert diferencia == {1, 2}
    
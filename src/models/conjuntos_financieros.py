from .categoria import Categoria
from .ingreso import Ingreso
from .gasto import Gasto

class ConjuntosFinancieros:
    """
    Implementa operaciones de Teoría de Conjuntos para clasificar,
    agrupar y filtrar transacciones financieras.
    """
    
    def __init__(self, transacciones: list[Gasto | Ingreso]):
        self.transacciones = transacciones
    
    def filtrar_por_categoria(self, categoria_objeto: Categoria) -> set[int]:
        """Filtra transacciones por categoría y devuelve un conjunto de IDs."""
        return {t.id for t in self.transacciones if t.categoria.nombre == categoria_objeto.nombre}
    
    def interseccion_gastos(self, categoria_a: Categoria, categoria_b: Categoria) -> set[int]:
        """Calcula la intersección entre los IDs de dos categorías de gasto."""
        conjunto_a = self.filtrar_por_categoria(categoria_a)
        conjunto_b = self.filtrar_por_categoria(categoria_b)
        return conjunto_a.intersection(conjunto_b)
    
    def union_categorias(self, categoria_a: Categoria, categoria_b: Categoria) -> set[int]:
        """Calcula la unión de los IDs de dos categorías."""
        conjunto_a = self.filtrar_por_categoria(categoria_a)
        conjunto_b = self.filtrar_por_categoria(categoria_b)
        return conjunto_a.union(conjunto_b)
    
    def diferencia_gastos(self, categoria_total: Categoria, categoria_excluir: Categoria) -> set[int]:
        """Calcula la diferencia de los IDs entre dos categorías."""
        conjunto_total = self.filtrar_por_categoria(categoria_total)
        conjunto_excluir = self.filtrar_por_categoria(categoria_excluir)
        return conjunto_total.difference(conjunto_excluir)
    
    def gastos_por_rango_fechas(self, fecha_inicio: str, fecha_fin: str) -> set[int]:
        """Devuelve un conjunto de IDs de transacciones en un rango de fechas."""
        from datetime import datetime
        
        fecha_inicio_dt = datetime.strptime(fecha_inicio, '%Y-%m-%d')
        fecha_fin_dt = datetime.strptime(fecha_fin, '%Y-%m-%d')
        
        return {
            t.id for t in self.transacciones
            if fecha_inicio_dt <= t.fecha <= fecha_fin_dt and t.categoria.tipo == 'Gasto'
        }
        
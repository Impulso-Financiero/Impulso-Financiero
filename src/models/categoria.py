class Categoria:
    def __init__(self, id_categoria: int, nombre: str, tipo: str):
        self.id_categoria = id_categoria
        self.nombre = nombre # Ej: "Alimentación", "Transporte", "Salario"
        self.tipo = tipo     # Ej: "Ingreso" o "Gasto"

    def asignar_categoria(self, nombre: str, tipo: str):
        """Asigna o reasigna el nombre y tipo de la categoría."""
        self.nombre = nombre
        self.tipo = tipo
        print(f"Categoría actualizada a: {self.nombre} ({self.tipo})")

    def editar_categoria(self, nuevo_nombre: str = None, nuevo_tipo: str = None):
        """Permite modificar el nombre o tipo de la categoría."""
        if nuevo_nombre:
            self.nombre = nuevo_nombre
        if nuevo_tipo:
            self.tipo = nuevo_tipo
        print(f"Categoría '{self.id_categoria}' modificada. Nuevo nombre: {self.nombre}, Nuevo tipo: {self.tipo}")

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"

    def __repr__(self):
        return f"Categoria(id={self.id_categoria}, nombre='{self.nombre}', tipo='{self.tipo}')"

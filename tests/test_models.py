import pytest
import datetime
import unittest.mock
# Importa las clases a testear desde la carpeta models
from models.usuario import Usuario
from models.perfil_financiero import PerfilFinanciero
from models.categoria import Categoria
from models.ingreso import Ingreso
from models.gasto import Gasto
from models.ahorro import Ahorro
from models.presupuesto import Presupuesto
from models.alerta import Alerta

# Importa las constantes si las usas en las pruebas o para inicialización
from utils.CONSTANTES import CATEGORIAS_DISPONIBLES


# --- Fixtures para reutilizar objetos inicializados en las pruebas ---

@pytest.fixture
def categoria_test():
    """Fixture para una instancia de Categoria."""
    return Categoria(1, "Test", "Gasto")

@pytest.fixture
def ahorro_test():
    """Fixture para una instancia de Ahorro."""
    return Ahorro(1, 100.0, 1000.0, "Vacaciones", datetime.date(2025, 1, 1), datetime.date(2025, 12, 31))

@pytest.fixture
def categorias_ingreso_gasto():
    return (
        Categoria(id_categoria=1, nombre='Salario', tipo='Ingreso'),
        Categoria(id_categoria=3, nombre='Alimentación', tipo='Gasto'),
        Categoria(id_categoria=4, nombre='Transporte', tipo='Gasto')
    )
    
@pytest.fixture
def ingreso_test(categorias_ingreso_gasto):
    """Fixture para una instancia de Ingreso."""
    cat_salario, _, _ = categorias_ingreso_gasto
    return Ingreso(1, 1000.0, cat_salario, datetime.date(2025, 10, 1), "Fijo")

@pytest.fixture
def gasto_test(categorias_ingreso_gasto):
    """Fixture para una instancia de Gasto."""
    _, cat_alimentacion, _ = categorias_ingreso_gasto
    return Gasto(1, 50.0, cat_alimentacion, datetime.date(2025, 10, 5), "Variable", "Supermercado")

@pytest.fixture
def usuario_test():
    """Fixture para una instancia de Usuario."""
    return Usuario(1, "Test User", "test@example.com", "password")

@pytest.fixture
def perfil_test(usuario_test):
    """Fixture para una instancia de PerfilFinanciero asociado a un Usuario."""
    perfil = PerfilFinanciero(usuario=usuario_test)
    usuario_test.perfil_financiero = perfil
    return usuario_test.perfil_financiero

@pytest.fixture
def presupuesto_test(usuario_test, categorias_ingreso_gasto):
    """Fixture para una instancia de Presupuesto."""
    _, cat_alimentacion, cat_transporte = categorias_ingreso_gasto
    presupuesto = Presupuesto(1, usuario_test, 1000.0, 10, 2025)
    limites = {cat_alimentacion.nombre: 200.0, cat_transporte.nombre: 100.0}
    presupuesto.crear_presupuesto(500.0, limites)
    return presupuesto


# --- Pruebas de las clases ---

def test_categoria_init(categoria_test):
    assert categoria_test.id_categoria == 1
    assert categoria_test.nombre == "Test"
    assert categoria_test.tipo == "Gasto"

def test_categoria_editar_categoria(categoria_test):
    categoria_test.editar_categoria(nuevo_nombre="Test Modificado", nuevo_tipo="Ingreso")
    assert categoria_test.nombre == "Test Modificado"
    assert categoria_test.tipo == "Ingreso"
    categoria_test.editar_categoria(nuevo_nombre="Solo Nombre")
    assert categoria_test.nombre == "Solo Nombre"
    assert categoria_test.tipo == "Ingreso"

def test_ahorro_agregar_monto(ahorro_test):
    ahorro_test.agregar_monto(50.0)
    assert ahorro_test.monto_actual == 150.0
    ahorro_test.agregar_monto(-10.0) # No debería agregar montos negativos
    assert ahorro_test.monto_actual == 150.0

def test_ahorro_retirar_monto(ahorro_test):
    ahorro_test.retirar_monto(30.0)
    assert ahorro_test.monto_actual == 70.0
    ahorro_test.retirar_monto(100.0) # No debería retirar más de lo que hay
    assert ahorro_test.monto_actual == 70.0 # El monto actual no cambia
    ahorro_test.retirar_monto(-5.0) # No debería retirar montos negativos
    assert ahorro_test.monto_actual == 70.0 # El monto actual no cambia

def test_ahorro_calcular_progreso(ahorro_test):
    assert ahorro_test.calcular_progreso() == 10.0 # 100/1000 * 100
    ahorro_test.meta = 0 # Test para meta cero
    assert ahorro_test.calcular_progreso() == 0.0

def test_ahorro_simular_meta(ahorro_test):
    ahorro_test.monto_actual = 100.0
    ahorro_test.meta = 1100.0
    # Necesitas ahorrar 1000 en 10 meses = 100 por mes
    assert ahorro_test.simular_meta(ahorro_test.meta, 10) == 100.0
    assert ahorro_test.simular_meta(500.0, 5) == 80.0 # 400 restantes en 5 meses
    assert ahorro_test.simular_meta(50.0, 5) == 0.0 # Ya se superó el objetivo
    assert ahorro_test.simular_meta(1000.0, 0) == 0.0 # Meses cero

def test_ingreso_detalle(ingreso_test):
    assert "Monto: $1000.0" in ingreso_test.obtener_detalle()
    assert "Categoría: Salario" in ingreso_test.obtener_detalle()

def test_ingreso_modificar_ingreso(ingreso_test, categorias_ingreso_gasto):
    _, cat_alimentacion, _ = categorias_ingreso_gasto
    ingreso_test.modificar_ingreso(monto=1200.0, categoria=cat_alimentacion, fecha=datetime.date(2025, 11, 1))
    assert ingreso_test.monto == 1200.0
    assert ingreso_test.categoria == cat_alimentacion
    assert ingreso_test.fecha == datetime.date(2025, 11, 1)

def test_gasto_detalle(gasto_test):
    assert "Monto: $50.0" in gasto_test.obtener_detalle()
    assert "Categoría: Alimentación" in gasto_test.obtener_detalle()

def test_gasto_modificar_gasto(gasto_test, categorias_ingreso_gasto):
    cat_salario, _, _ = categorias_ingreso_gasto
    gasto_test.modificar_gasto(monto=75.0, categoria=cat_salario, fecha=datetime.date(2025, 11, 10))
    assert gasto_test.monto == 75.0
    assert gasto_test.categoria == cat_salario
    assert gasto_test.fecha == datetime.date(2025, 11, 10)

def test_perfil_init(usuario_test, perfil_test):
    usuario_test = Usuario(1, "Test User", "test@example.com", "password")
    perfil_test = PerfilFinanciero(usuario=usuario_test)
    usuario_test.perfil_financiero = perfil_test
    assert isinstance(usuario_test.perfil_financiero, PerfilFinanciero)
    assert perfil_test.usuario == usuario_test
    assert perfil_test.balance_actual == 0.0

def test_perfil_agregar_ingreso(perfil_test, ingreso_test):
    perfil_test.agregar_ingreso(ingreso_test)
    assert len(perfil_test.ingresos_registrados) == 1
    assert perfil_test.balance_actual == 1000.0

def test_perfil_agregar_gasto(perfil_test, ingreso_test, gasto_test):
    perfil_test.agregar_ingreso(ingreso_test) # Necesario para tener balance
    perfil_test.agregar_gasto(gasto_test)
    assert len(perfil_test.gastos_registrados) == 1
    assert perfil_test.balance_actual == 950.0 # 1000 - 50

def test_perfil_calcular_nivel_salud_financiera(perfil_test):
    # Sin ingresos/gastos, balance 0
    perfil_test.calcular_nivel_salud_financiera()
    assert perfil_test.nivel_salud_financiera == "Normal"

    # Crea una instancia de Ahorro con todos los argumentos requeridos.
    ahorro_meta = Ahorro(
        id_ahorro=1,
        monto_actual=100.0,
        meta=500.0,
        tipo="Viaje",
        fecha_inicio=datetime.date.today(),
        fecha_meta=datetime.date.today() + datetime.timedelta(days=100) # Ejemplo de fecha futura
    )
    perfil_test.agregar_ahorro(ahorro_meta)

    # Vuelve a calcular el nivel de salud financiera después de agregar el ahorro.
    perfil_test.calcular_nivel_salud_financiera()

    # Ahora la aserción debería pasar (si la lógica en el método es correcta).
    assert perfil_test.nivel_salud_financiera == "Saludable"


def test_presupuesto_crear_presupuesto(presupuesto_test, categorias_ingreso_gasto):
    _, cat_alimentacion, cat_transporte = categorias_ingreso_gasto
    assert presupuesto_test.monto_total == 500.0
    assert cat_alimentacion.nombre in presupuesto_test.categorias
    assert presupuesto_test.categorias[cat_alimentacion.nombre]['limite'] == 200.0
    assert cat_transporte.nombre in presupuesto_test.categorias
    assert presupuesto_test.categorias[cat_transporte.nombre]['limite'] == 100.0
    assert presupuesto_test.categorias[cat_alimentacion.nombre]['gastado_actual'] == 0.0

def test_presupuesto_modificar_limite_categoria(presupuesto_test, categorias_ingreso_gasto):
    _, cat_alimentacion, _ = categorias_ingreso_gasto
    presupuesto_test.modificar_limite_categoria(cat_alimentacion.nombre, 250.0)
    assert presupuesto_test.categorias[cat_alimentacion.nombre]['limite'] == 250.0
    # Intentar modificar una categoría que no existe
    presupuesto_test.modificar_limite_categoria("Inexistente", 50.0) # Esto debería imprimir un mensaje, pero no romper la prueba

def test_presupuesto_restar_gasto_y_alerta(presupuesto_test, gasto_test, usuario_test, categorias_ingreso_gasto):
    # Asegurarse de que el usuario tiene la lista de alertas vacía antes
    usuario_test.alertas = []
    _, cat_alimentacion, _ = categorias_ingreso_gasto

    # Usar el contexto de patch para simular la función
    with unittest.mock.patch('models.alerta.Alerta.enviar_notificacion') as mock_enviar_notificacion:
        # Configurar el gasto para que sea mayor que el límite del presupuesto
        presupuesto_test.categorias[cat_alimentacion.nombre]['limite'] = 50.0
        gasto_test.monto = 60.0
        gasto_test.categoria = cat_alimentacion
        
        # Llamar al método pasando la categoría y el monto por separado
        presupuesto_test.restar_gasto(gasto_test.categoria, gasto_test.monto)
    
        # Verificar que el método simulado fue llamado
        mock_enviar_notificacion.assert_called_once()
    
    # Asegurarse de que el gasto se restó correctamente
    assert presupuesto_test.categorias[cat_alimentacion.nombre]['gastado_actual'] == 60.0
    assert presupuesto_test.categorias[cat_alimentacion.nombre]['limite'] == 50.0
    
def test_presupuesto_modificar_ingreso_total(presupuesto_test):
    presupuesto_test.modificar_ingreso_total(1500.0)
    assert presupuesto_test.ingreso_total_real == 1500.0
    presupuesto_test.modificar_ingreso_total(500.0)
    assert presupuesto_test.ingreso_total_real == 2000.0


def test_alerta_init(usuario_test):
    alerta = Alerta(1, usuario_test, "gasto", "Límite de gasto excedido", datetime.date.today())
    assert alerta.tipo == "gasto"
    assert alerta.activo is True

def test_alerta_desactivar(usuario_test):
    alerta = Alerta(1, usuario_test, "gasto", "Mensaje", datetime.date.today())
    alerta.desactivar()
    assert alerta.activo is False

def test_alerta_editar_mensaje(usuario_test):
    alerta = Alerta(1, usuario_test, "gasto", "Mensaje original", datetime.date.today())
    alerta.editar_mensaje("Nuevo mensaje")
    assert alerta.mensaje == "Nuevo mensaje"
    
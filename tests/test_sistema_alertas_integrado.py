import datetime
from src.models.sistema_alertas_integrado import SistemaAlertasIntegrado
from src.models.usuario import Usuario
from src.models.categoria import Categoria
from src.models.gasto import Gasto
from src.models.alerta import Alerta

# Mock de usuario para los tests
class MockUsuario(Usuario):
    def __init__(self):
        super().__init__(1, "TestUser", "test@mail.com", "pass")
        self.perfil_financiero = self

    def obtener_datos_agregados_para_reglas(self, mes, anio):
        return {
            'gastos_total': 1500,
            'ingreso': 2000,
            'ahorro_mensual': 500,
            'gastos_delivery': 350,
            'gastos_ocio': 200,
            'ahorro_excedente': 0,
        }

# Mock de transacciones para el análisis estadístico
transacciones_mock = [
    {'monto': 100, 'categoria': 'Alimentación', 'tipo': 'gasto'},
    {'monto': 50, 'categoria': 'Alimentación', 'tipo': 'gasto'},
    {'monto': 350, 'categoria': 'Delivery', 'tipo': 'gasto'},
    {'monto': 200, 'categoria': 'Ocio', 'tipo': 'gasto'},
]

def test_analisis_completo():
    usuario = MockUsuario()
    sistema = SistemaAlertasIntegrado()
    
    historial_saldos = [1000, 800, 600]
    
    alertas = sistema.analisis_completo(usuario, transacciones_mock, historial_saldos)
    
    # Verificar que se generen alertas
    assert len(alertas) > 0
    
    # Verificar un tipo de alerta específico (ej: la de derivadas)
    alerta_derivada_encontrada = False
    for alerta in alertas:
        if alerta.tipo == "derivada":
            alerta_derivada_encontrada = True
            break
    assert alerta_derivada_encontrada is True
    
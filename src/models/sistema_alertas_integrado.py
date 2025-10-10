from datetime import datetime, date
from .derivadas import AnalisisDerivadas
from .estadistica import AnalisisEstadistico
from .reglas_logicas import ReglasLogicas
from .inferencias import Inferencias
from .alerta import Alerta
from .usuario import Usuario

class SistemaAlertasIntegrado:
    """
    Sistema que integra todos los módulos matemáticos para generar
    alertas inteligentes y contextualizadas como objetos Alerta
    """
    
    def __init__(self):
        self.reglas_logicas = ReglasLogicas()
        self.inferencias = Inferencias()
        self.derivadas = AnalisisDerivadas()
        self.estadistica = AnalisisEstadistico()
    
    def analisis_completo(self, usuario: Usuario, transacciones, historial_saldos):
        alertas_objetos = []
        id_alerta = 1
        
        # Obtener los datos del perfil financiero del usuario
        perfil_datos = usuario.perfil_financiero.obtener_datos_agregados_para_reglas(
            date.today().month, date.today().year
        )

        # 1. Alertas de Lógica Proposicional
        alertas_texto = self.reglas_logicas.generar_alerta_financiera(perfil_datos)
        for msg in alertas_texto:
            alertas_objetos.append(Alerta(id_alerta, usuario, "logica", msg, date.today()))
            id_alerta += 1
        
        # 2. Alertas de Inferencias
        saldo_actual = historial_saldos[-1] if historial_saldos else 0
        necesita_ajuste, justificacion = self.inferencias.justificar_recomendacion(saldo_actual)
        if necesita_ajuste:
            alertas_objetos.append(Alerta(id_alerta, usuario, "inferencia", justificacion, date.today()))
            id_alerta += 1
        
        # 3. Alertas de Derivadas
        if len(historial_saldos) >= 2:
            analisis_tasa = self.derivadas.calcular_tasa_vulnerabilidad(
                historial_saldos[-2], 
                historial_saldos[-1]
            )
            if analisis_tasa['alerta_proactiva']:
                msg = f"{analisis_tasa['mensaje']} (Tasa: ${analisis_tasa['tasa_cambio']:,.0f}/mes)"
                alertas_objetos.append(Alerta(id_alerta, usuario, "derivada", msg, date.today()))
                id_alerta += 1
        
        # 4. Alertas Estadísticas
        alertas_objetos += self._generar_alertas_estadisticas(transacciones, usuario, id_alerta)
        
        # 5. Alertas Temporales
        alertas_objetos += self._generar_alertas_temporales(usuario, id_alerta)
        
        return alertas_objetos
    
    def _generar_alertas_estadisticas(self, transacciones, usuario: Usuario, id_inicial):
        """Alertas basadas en análisis de distribución de gastos"""
        alertas = []
        id_alerta = id_inicial
        porcentajes = self.estadistica.porcentaje_por_categoria(transacciones)
        
        for categoria, datos in porcentajes.items():
            porcentaje = datos['porcentaje']
            if categoria == 'Alimentación' and porcentaje > 33:
                msg = f"{categoria}: {porcentaje:.1f}% supera recomendación del 33%"
                alertas.append(Alerta(id_alerta, usuario, "estadistica", msg, date.today()))
                id_alerta += 1
            elif categoria in ['Delivery', 'Ocio'] and porcentaje > 15:
                msg = f"{categoria}: {porcentaje:.1f}% es muy alto para gastos no esenciales"
                alertas.append(Alerta(id_alerta, usuario, "estadistica", msg, date.today()))
                id_alerta += 1
        
        return alertas
    
    def _generar_alertas_temporales(self, usuario: Usuario, id_inicial):
        """Alertas basadas en calendario"""
        alertas = []
        id_alerta = id_inicial
        hoy = datetime.now()
        
        if hoy.day >= 25:
            dias_para_cobro = 30 - hoy.day
            msg = f"Solo {dias_para_cobro} días para fin de mes"
            alertas.append(Alerta(id_alerta, usuario, "temporal", msg, date.today()))
        
        return alertas
    
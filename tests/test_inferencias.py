from src.models.inferencias import Inferencias

def test_modus_ponens():
    # Si P es verdadero, devuelve Q
    resultado1 = Inferencias.modus_ponens(True, "Conclusión Q")
    assert resultado1 == "Conclusión Q"
    
    # Si P es falso, devuelve None
    resultado2 = Inferencias.modus_ponens(False, "Conclusión Q")
    assert resultado2 is None

def test_justificar_recomendacion():
    inferencias = Inferencias()
    
    # Caso de saldo insuficiente (aplicar recomendación)
    aplica1, justificacion1 = inferencias.justificar_recomendacion(saldo_actual=500, umbral_critico=1000)
    assert aplica1 is True
    assert "Ajustar presupuesto" in justificacion1
    
    # Caso de saldo adecuado (no aplicar recomendación)
    aplica2, justificacion2 = inferencias.justificar_recomendacion(saldo_actual=1500, umbral_critico=1000)
    assert aplica2 is False
    assert "Saldo adecuado" in justificacion2
    
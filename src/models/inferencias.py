class Inferencias:
    """
    Implementa métodos de demostración lógica: Modus Ponens, 
    Contrarrecíproca, etc.
    """
    
    @staticmethod
    def modus_ponens(premisa_p, implicacion_p_implica_q):
        """
        Modus Ponens: Si P y (P → Q), entonces Q
        """
        if premisa_p:
            return implicacion_p_implica_q
        return None
    
    def justificar_recomendacion(self, saldo_actual, umbral_critico=1000):
        """
        R6: Justificación de Recomendación usando Modus Ponens
        """
        P_saldo_insuficiente = (saldo_actual < umbral_critico)
        Q_recomendacion = "Ajustar presupuesto mensual para evitar endeudamiento"
        
        resultado = self.modus_ponens(P_saldo_insuficiente, Q_recomendacion)
        
        if resultado:
            justificacion = f"""
            DEMOSTRACIÓN (Modus Ponens):
            ─────────────────────────────
            Premisa Mayor: Si (Saldo < ${umbral_critico:,.0f}) → (Riesgo de crédito)
            Premisa Menor: Saldo actual = ${saldo_actual:,.2f} < ${umbral_critico:,.0f}
            ∴ Conclusión: {resultado}
            """
            return True, justificacion
        
        return False, "Saldo adecuado. No se requiere ajuste urgente."

    # Podrías añadir otros métodos de inferencia aquí (Contrarrecíproca, etc.)
    # @staticmethod
    # def contrarreciproca(implicacion_p_implica_q, negacion_q):
    #     """
    #     Contrarrecíproca: Si (P → Q) y ¬Q, entonces ¬P
    #     """
    #     if not negacion_q: # Si no Q es verdadero, entonces Q es falso
    #         return not implicacion_p_implica_q # y por lo tanto no P es verdadero
    #     return None
    
class ReglasLogicas:
    """
    Implementa lógica proposicional con operadores AND, OR, NOT
    y cuantificadores ∀ (para todo) y ∃ (existe)
    """
    
    @staticmethod
    def evaluar_regla(condiciones, operador='AND'):
        """
        Evalúa múltiples condiciones con operador lógico
        Ejemplo: [(gastos, '>', 100000), (ahorro, '<', 50000)]
        """
        resultados = []
        for variable, operador_comparacion, valor in condiciones:
            if operador_comparacion == '>':
                resultados.append(variable > valor)
            elif operador_comparacion == '<':
                resultados.append(variable < valor)
            elif operador_comparacion == '>=':
                resultados.append(variable >= valor)
            elif operador_comparacion == '<=':
                resultados.append(variable <= valor)
            elif operador_comparacion == '==':
                resultados.append(variable == valor)
            elif operador_comparacion == '!=':
                resultados.append(variable != valor)
        
        if operador == 'AND':
            return all(resultados)  # ∧ (conjunción)
        elif operador == 'OR':
            return any(resultados)  # ∨ (disyunción)
    
    def generar_alerta_financiera(self, perfil_usuario):
        """
        R1-R6: Aplica reglas lógicas del ABP para alertas personalizadas
        """
        alertas = []
        
        # R1: Alerta de Sobregiro (P → Q)
        if self.evaluar_regla([
            (perfil_usuario['gastos_total'], '>', perfil_usuario['ingreso'] * 0.80)
        ]):
            alertas.append("⚠️ ALERTA R1: Gastos superan 80% del ingreso mensual")
        
        # R2: Detección de Gastos No Esenciales
        gastos_no_esenciales = perfil_usuario.get('gastos_delivery', 0) + perfil_usuario.get('gastos_ocio', 0)
        if self.evaluar_regla([
            (gastos_no_esenciales, '>', perfil_usuario['ingreso'] * 0.15),
            (perfil_usuario['ahorro_mensual'], '<', perfil_usuario['ingreso'] * 0.05)
        ], operador='AND'):
            alertas.append("💡 SUGERENCIA R2: Reducir gastos no esenciales para aumentar ahorro")
        
        # R3: Riesgo de Endeudamiento (requiere derivadas - ver módulo 6)
        
        # R4: Refuerzo de Ahorro Activo
        if perfil_usuario.get('ahorro_excedente', 0) > 0:
            alertas.append("💰 OPORTUNIDAD R4: Tienes ahorro excedente. Considera comparar tasas de inversión")
        
        return alertas
    
    @staticmethod
    def cuantificador_existencial(transacciones, condicion):
        """
        ∃ x: Existe al menos una transacción que cumple la condición
        Ejemplo: ¿Existe al menos un gasto recurrente?
        """
        return any(condicion(t) for t in transacciones)
    
    @staticmethod
    def cuantificador_universal(transacciones, condicion):
        """
        ∀ x: Todas las transacciones cumplen la condición
        """
        return all(condicion(t) for t in transacciones)

    # Contrareciproca sin implementar
    # @staticmethod
    # def contrarreciproca(implicacion_p_implica_q, negacion_q):
    #     """
    #     Contrarrecíproca: Si (P → Q) y ¬Q, entonces ¬P
    #     """
    #     if not negacion_q: # Si no Q es verdadero, entonces Q es falso
    #         return not implicacion_p_implica_q # y por lo tanto no P es verdadero
    #     return None
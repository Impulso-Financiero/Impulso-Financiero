import datetime
import statistics
import numpy as np

# Importaciones de las clases desde el paquete 'models'
from models.usuario import Usuario
from models.perfil_financiero import PerfilFinanciero
from models.presupuesto import Presupuesto # Nuevo
from models.categoria import Categoria
from models.ingreso import Ingreso
from models.gasto import Gasto
from models.ahorro import Ahorro
from models.alerta import Alerta
from models.reglas_logicas import ReglasLogicas
from models.inferencias import Inferencias
from models.estadistica import AnalisisEstadistico
from models.matrices import AlgebraLinealFinanciera # Nuevo
from models.derivadas import AnalisisDerivadas
from models.funciones import FuncionesMatematicas
from models.proyecciones import ProyeccionesFinancieras
from models.sistema_alertas_integrado import SistemaAlertasIntegrado
from utils.CONSTANTES import CATEGORIAS_INGRESOS_DISPONIBLES, CATEGORIAS_GASTOS_DISPONIBLES

def mostrar_menu_principal(nombre_usuario: str):
    """Muestra el menú principal personalizado para el usuario activo."""
    print(f"\n--- MENÚ PRINCIPAL de {nombre_usuario} ---")
    print("1. Gestionar Ingresos")
    print("2. Gestionar Gastos")
    print("3. Gestionar Ahorros")
    print("4. Gestionar Presupuestos")
    print("5. Ver Resumen Financiero y Alertas")
    print("6. Análisis y Recomendaciones Financieras Avanzadas")
    print("7. Proyecciones y Planes")
    print("8. Cerrar Sesión")

def gestionar_ingresos(perfil_usuario: PerfilFinanciero):
    """Gestión de ingresos."""
    while True:
        print("\n--- GESTIÓN DE INGRESOS ---")
        print("1. Agregar un nuevo ingreso")
        print("2. Ver todos los ingresos")
        print("3. Volver al menú principal")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            try:
                monto = float(input("Monto del ingreso: "))
                print("Categorías de ingresos disponibles:")
                for cat in CATEGORIAS_INGRESOS_DISPONIBLES:
                    print(f"ID: {cat.id_categoria}, Nombre: {cat.nombre}")
                cat_id = int(input("ID de la categoría: "))
                categoria = next((c for c in CATEGORIAS_INGRESOS_DISPONIBLES if c.id_categoria == cat_id), None)
                if categoria:
                    nuevo_ingreso = Ingreso(id_ingreso=len(perfil_usuario.ingresos_registrados) + 1, monto=monto, categoria=categoria, fecha=datetime.date.today(), tipo="Variable")
                    perfil_usuario.agregar_ingreso(nuevo_ingreso)
                    print("Ingreso agregado con éxito.")
                else:
                    print("Categoría no encontrada o inválida.")
            except ValueError:
                print("Entrada inválida. Asegúrate de ingresar un número para el monto y el ID.")
        elif opcion == "2":
            print("\n--- LISTA DE INGRESOS ---")
            if not perfil_usuario.ingresos_registrados:
                print("No hay ingresos registrados.")
            else:
                for ingreso in perfil_usuario.ingresos_registrados:
                    print(ingreso.obtener_detalle())
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def gestionar_gastos(perfil_usuario: PerfilFinanciero, usuario_activo: Usuario):
    print("DEBUG: Entrando en la función gestionar_gastos.")
    """Gestión de gastos."""
    while True:
        print("\n--- GESTIÓN DE GASTOS ---")
        print("1. Agregar un nuevo gasto")
        print("2. Ver todos los gastos")
        print("3. Volver al menú principal")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            try:
                monto = float(input("Monto del gasto: "))
                descripcion = input("Descripción del gasto: ")
                print("Categorías de gastos disponibles:")
                for cat in CATEGORIAS_GASTOS_DISPONIBLES:
                    print(f"ID: {cat.id_categoria}, Nombre: {cat.nombre}")
                cat_id = int(input("ID de la categoría: "))
                categoria = next((c for c in CATEGORIAS_GASTOS_DISPONIBLES if c.id_categoria == cat_id), None)
                if categoria:
                    fecha_gasto = datetime.date.today()
                    nuevo_gasto = Gasto(id_gasto=len(perfil_usuario.gastos_registrados) + 1, monto=monto, categoria=categoria, fecha=fecha_gasto, tipo="Variable", descripcion=descripcion)
                    perfil_usuario.agregar_gasto(nuevo_gasto)
                else:
                    print("Categoría no encontrada o inválida.")
            except ValueError:
                print("Entrada inválida. Asegúrate de ingresar un número para el monto y el ID.")
        elif opcion == "2":
            print("\n--- LISTA DE GASTOS ---")
            if not perfil_usuario.gastos_registrados:
                print("No hay gastos registrados.")
            else:
                for gasto in perfil_usuario.gastos_registrados:
                    print(gasto.obtener_detalle())
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def gestionar_ahorros(perfil_usuario: PerfilFinanciero):
    """Gestión de ahorros."""
    while True:
        print("\n--- GESTIÓN DE AHORROS ---")
        print("1. Ver ahorros existentes")
        print("2. Agregar monto a un ahorro")
        print("3. Retirar monto de un ahorro")
        print("4. Crear nuevo ahorro")
        print("5. Volver al menú principal")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            print("\n--- LISTA DE AHORROS ---")
            if not perfil_usuario.metas_ahorro:
                print("No hay ahorros registrados.")
            else:
                for ahorro in perfil_usuario.metas_ahorro:
                    print(ahorro.estado_ahorro())
        elif opcion == "2":
            try:
                ahorro_id = int(input("ID del ahorro al que agregar: "))
                monto = float(input("Monto a agregar: "))
                ahorro = next((a for a in perfil_usuario.metas_ahorro if a.id_ahorro == ahorro_id), None)
                if ahorro:
                    ahorro.agregar_monto(monto)
                else:
                    print("Ahorro no encontrado.")
            except ValueError:
                print("Entrada inválida. Asegúrate de ingresar números.")
        elif opcion == "3":
            try:
                ahorro_id = int(input("ID del ahorro del que retirar: "))
                monto = float(input("Monto a retirar: "))
                ahorro = next((a for a in perfil_usuario.metas_ahorro if a.id_ahorro == ahorro_id), None)
                if ahorro:
                    ahorro.retirar_monto(monto)
                else:
                    print("Ahorro no encontrado.")
            except ValueError:
                print("Entrada inválida. Asegúrate de ingresar números.")
        elif opcion == "4":
            try:
                meta = float(input("Meta de ahorro: "))
                tipo = input("Tipo de ahorro (ej. 'Viaje', 'Emergencia'): ")
                fecha_meta_str = input("Fecha de meta (DD-MM-AAAA): ")
                fecha_meta = datetime.datetime.strptime(fecha_meta_str, "%d-%m-%Y").date()
                nuevo_ahorro = Ahorro(id_ahorro=len(perfil_usuario.metas_ahorro)+1, monto_actual=0.0, meta=meta, tipo=tipo, fecha_inicio=datetime.date.today(), fecha_meta=fecha_meta)
                perfil_usuario.agregar_ahorro(nuevo_ahorro)
                print("Nuevo ahorro creado con éxito.")
            except (ValueError, IndexError):
                print("Error en los datos proporcionados.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def gestionar_presupuestos(perfil_usuario: PerfilFinanciero, usuario_activo: Usuario):
    """Gestión de presupuestos."""
    while True:
        print("\n--- GESTIÓN DE PRESUPUESTOS ---")
        print("1. Crear nuevo presupuesto mensual")
        print("2. Modificar presupuesto existente")
        print("3. Ver presupuestos existentes")
        print("4. Ver resumen de presupuesto mensual")
        print("5. Volver al menú principal")
        opcion = input("Elige una opción: ")

        if opcion == "1": # CREAR nuevo presupuesto
            try:
                mes = int(input("Mes (1-12) para el presupuesto: "))
                anio = int(input("Año para el presupuesto: "))
                monto_total = float(input("Monto total del presupuesto: "))
                
                limites = {}
                print("Define límites por categoría de gasto:")
                for cat in CATEGORIAS_GASTOS_DISPONIBLES:
                    limite_str = input(f"Límite para '{cat.nombre}' (dejar vacío para no limitar): ")
                    if limite_str:
                        limites[cat.nombre] = float(limite_str)

                clave = f"{mes}_{anio}"
                if clave in perfil_usuario.presupuestos:
                    print("Ya existe un presupuesto para esta fecha. Usa la opción 2 para modificarlo.")
                else:
                    nuevo_presupuesto = Presupuesto(id_presupuesto=len(perfil_usuario.presupuestos)+1, usuario=usuario_activo, monto_total=monto_total, mes=mes, anio=anio)
                    nuevo_presupuesto.crear_presupuesto(monto_total, limites)
                    perfil_usuario.agregar_presupuesto(nuevo_presupuesto)
            except ValueError:
                print("Entrada inválida. Asegúrate de ingresar números.")
        elif opcion == "2": # MODIFICAR presupuesto
            try:
                mes = int(input("Mes (1-12) del presupuesto a modificar: "))
                anio = int(input("Año del presupuesto a modificar: "))
                clave = f"{mes}_{anio}"
                if clave in perfil_usuario.presupuestos:
                    presupuesto = perfil_usuario.presupuestos[clave]
                    print(f"Modificando presupuesto para {mes}/{anio}. Monto actual: ${presupuesto.monto_total}")
                    nuevo_monto = input("Nuevo monto total (o Enter para mantener el actual): ")
                    if nuevo_monto:
                        presupuesto.monto_total = float(nuevo_monto)
                    
                    print("¿Deseas modificar límites por categoría?")
                    modificar_limites = input("(s/n): ")
                    if modificar_limites.lower() == 's':
                        for cat in CATEGORIAS_GASTOS_DISPONIBLES:
                            limite_actual = presupuesto.categorias.get(cat.nombre, {}).get('limite', 0.0)
                            nuevo_limite_str = input(f"Nuevo límite para '{cat.nombre}' (actual: ${limite_actual}) - (o Enter para no cambiar): ")
                            if nuevo_limite_str:
                                presupuesto.modificar_limite_categoria(cat.nombre, float(nuevo_limite_str))
                    print("Presupuesto modificado con éxito.")
                else:
                    print("No se encontró un presupuesto para esa fecha. Usa la opción 1 para crearlo.")
            except ValueError:
                print("Entrada inválida.")
        elif opcion == "3":
            print("\n--- LISTA DE PRESUPUESTOS ---")
            if not perfil_usuario.presupuestos:
                print("No hay presupuestos configurados.")
            else:
                for clave, presupuesto in perfil_usuario.presupuestos.items():
                    print(f"- {presupuesto}")
        elif opcion == "4":
            try:
                mes = int(input("Mes (1-12) del presupuesto a ver: "))
                anio = int(input("Año del presupuesto a ver: "))
                clave = f"{mes}_{anio}"
                if clave in perfil_usuario.presupuestos:
                    print(perfil_usuario.presupuestos[clave].resumen_presupuesto())
                else:
                    print("No se encontró un presupuesto para esa fecha.")
            except ValueError:
                print("Entrada inválida.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

def ver_resumen_y_alertas(perfil_usuario: PerfilFinanciero, usuario_activo: Usuario):
    """Muestra el resumen financiero y las alertas activas."""
    print("\n--- RESUMEN FINANCIERO Y ALERTAS ---")
    print(perfil_usuario.obtener_resumen_financiero())
    print(perfil_usuario.obtener_resumen_ahorro_y_recomendaciones())
    print("\n--- ALERTAS ACTIVAS ---")
    if not usuario_activo.alertas:
        print("No hay alertas pendientes.")
    else:
        for alerta in usuario_activo.alertas:
            if alerta.activo:
                print(alerta.obtener_detalle())

def analisis_y_recomendaciones_avanzadas(perfil_usuario: PerfilFinanciero, usuario_activo: Usuario):
    """Realiza análisis financiero y genera recomendaciones."""
    print("\n--- ANÁLISIS Y RECOMENDACIONES AVANZADAS ---")
    sistema_alertas = SistemaAlertasIntegrado()

    # Preparar datos para el análisis integrado
    transacciones_totales = []
    for t in perfil_usuario.ingresos_registrados:
        transacciones_totales.append({'monto': t.monto, 'categoria': t.categoria.nombre, 'tipo': 'ingreso'})
    for t in perfil_usuario.gastos_registrados:
        transacciones_totales.append({'monto': t.monto, 'categoria': t.categoria.nombre, 'tipo': 'gasto'})
    
    historial_saldos_para_analisis = [120000, 110000, 95000] # Ejemplo de historial
    historial_saldos_para_analisis.append(perfil_usuario.balance_actual)

    perfil_datos_para_reglas = perfil_usuario.obtener_datos_agregados_para_reglas(datetime.date.today().month, datetime.date.today().year)
    
    # Generar alertas integradas
    nuevas_alertas = sistema_alertas.analisis_completo(
        usuario=usuario_activo,
        transacciones=transacciones_totales,
        historial_saldos=historial_saldos_para_analisis
    )
    for alerta_obj in nuevas_alertas:
        alerta_obj.id_alerta = len(usuario_activo.alertas) + 1
        usuario_activo.alertas.append(alerta_obj)
    
    if nuevas_alertas:
        print(f"\nSe generaron {len(nuevas_alertas)} nuevas alertas:")
        for alerta in nuevas_alertas:
            alerta.enviar_notificacion()
    else:
        print("No se generaron nuevas alertas en este análisis.")

    # Estadísticas básicas
    if transacciones_totales:
        print("\n--- RESUMEN ESTADÍSTICO DE GASTOS ---")
        gastos_para_estadistica = [t for t in transacciones_totales if t['tipo'] == 'gasto']
        resumen_est = AnalisisEstadistico.resumen_financiero(gastos_para_estadistica)
        porcentajes = AnalisisEstadistico.porcentaje_por_categoria(gastos_para_estadistica)
        if resumen_est:
            print(f"Media de Gastos: ${resumen_est.get('media', 0):,.2f}")
            print(f"Desviación Estándar: ${resumen_est.get('desviacion_estandar', 0):,.2f}")
        if porcentajes:
            print("\nPorcentaje de Gastos por Categoría:")
            for cat, datos in porcentajes.items():
                print(f"- {cat}: {datos['porcentaje']:.2f}%")
    
    # Matrices financieras
    print("\n--- MATRICES FINANCIERAS ---")
    matrices = AlgebraLinealFinanciera()
    if perfil_usuario.gastos_registrados:
        # Prepara los datos para la matriz (debe ser una matriz numpy)
        # Aquí se necesita una lógica para convertir los gastos en una matriz numérica
        # Esto es un ejemplo, la lógica real depende de cómo quieras agrupar los datos
        # por categorías y meses
        print("Se necesitaría una lógica más completa para generar la matriz de gastos.")
        print("Mostrando solo un análisis básico por ahora.")
        matriz_dummy = np.array([[g.monto for g in perfil_usuario.gastos_registrados]])
        if matriz_dummy.size > 0:
            total_mensual_dummy = matrices.gasto_total_mensual(matriz_dummy)
            print(f"Total de gastos por mes (análisis matricial básico): {total_mensual_dummy}")

    # Tendencias y tasas de cambio
    print("\n--- ANÁLISIS DE TENDENCIAS (DERIVADAS) ---")
    derivadas = AnalisisDerivadas()
    tendencia_proyectada = derivadas.proyectar_tendencia(historial_saldos_para_analisis)
    if tendencia_proyectada:
        print(f"Proyección de Tendencia del Saldo: {tendencia_proyectada['mensaje']}")

def proyecciones_y_planes(perfil_usuario: PerfilFinanciero):
    """Calcula proyecciones y planes financieros."""
    while True:
        print("\n--- PROYECCIONES Y PLANES ---")
        print("1. Proyección de Ahorro Lineal")
        print("2. Proyección de Inversión (Interés Compuesto)")
        print("3. Amortización de Deudas")
        print("4. Impacto de la Inflación")
        print("5. Volver al menú principal")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                ahorro_mensual = float(input("Ingrese su ahorro mensual esperado: "))
                saldo_inicial = perfil_usuario.balance_actual
                meses_proyeccion = int(input("¿Cuántos meses desea proyectar?: "))
                
                _, proyeccion_ahorro = ProyeccionesFinancieras.sucesion_aritmetica_ahorro(
                    saldo_inicial,
                    ahorro_mensual,
                    meses_proyeccion
                )
                print("\nProyección Lineal de Ahorro:")
                
                for p in proyeccion_ahorro:
                    print(f"  Mes {p['mes']}: ${p['acumulado']:,.2f}")
            except ValueError:
                print("Entrada inválida.")
        elif opcion == "2":
            try:
                capital_inicial = float(input("Ingrese capital inicial para inversión: "))
                tasa_mensual_porcentaje = float(input("Ingrese tasa de interés mensual (ej: 3.2 para 3.2%): "))
                meses_inversion = int(input("Ingrese número de meses para inversión: "))
                
                # Se convierte el porcentaje a decimal antes de la llamada
                tasa_mensual_inversion = tasa_mensual_porcentaje / 100
                
                monto_final_inversion = ProyeccionesFinancieras.interes_compuesto(capital_inicial, tasa_mensual_inversion, meses_inversion)
                print(f"Monto final proyectado con interés compuesto: ${monto_final_inversion:,.2f}")
            except ValueError:
                print("Entrada inválida.")
        elif opcion == "3":
            try:
                deuda = float(input("Ingrese el monto total de la deuda: "))
                tasa_mensual_deuda_porcentaje = float(input("Ingrese la tasa de interés mensual de la deuda (ej: 1 para 1%): "))
                cuotas = int(input("Ingrese el número de cuotas: "))
                
                # Se convierte el porcentaje a decimal antes de la llamada
                tasa_mensual_deuda = tasa_mensual_deuda_porcentaje / 100
                
                cuota_mensual = ProyeccionesFinancieras.amortizacion_francesa(deuda, tasa_mensual_deuda, cuotas)
                print(f"Cuota mensual estimada para amortización (método francés): ${cuota_mensual:,.2f}")
            except ValueError:
                print("Entrada inválida.")
        elif opcion == "4":
            try:
                ahorro_actual_inflacion = float(input("Ingrese su ahorro actual: "))
                tasa_inflacion_anual_porcentaje = float(input("Ingrese la tasa de inflación anual (ej: 2.1 para 2.1%): "))
                meses_inflacion = int(input("Ingrese el número de meses a proyectar: "))
                
                # Se convierte la tasa a decimal antes de la llamada
                tasa_inflacion_anual = tasa_inflacion_anual_porcentaje / 100
                
                resultado_inflacion = ProyeccionesFinancieras.impacto_inflacion(ahorro_actual_inflacion, tasa_inflacion_anual, meses_inflacion)
                print(f"Poder adquisitivo en {meses_inflacion} meses: ${resultado_inflacion['poder_adquisitivo_final']:,.2f}")
                print(f"Pérdida de poder adquisitivo: ${resultado_inflacion['perdida_por_inflacion']:,.2f} ({resultado_inflacion['porcentaje_perdida']:.2f}%)")
            except ValueError:
                print("Entrada inválida.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def iniciar_menu_principal(usuario_activo: Usuario):
    """
    Función principal del menú, que recibe el objeto Usuario activo.
    """
    perfil_usuario = usuario_activo.perfil_financiero
    while True:
        mostrar_menu_principal(usuario_activo.nombre)
        opcion = input("Elige una opción: ")
        if opcion == "1":
            gestionar_ingresos(perfil_usuario)
        elif opcion == "2":
            gestionar_gastos(perfil_usuario, usuario_activo)
        elif opcion == "3":
            gestionar_ahorros(perfil_usuario)
        elif opcion == "4":
            gestionar_presupuestos(perfil_usuario, usuario_activo)
        elif opcion == "5":
            ver_resumen_y_alertas(perfil_usuario, usuario_activo)
        elif opcion == "6":
            analisis_y_recomendaciones_avanzadas(perfil_usuario, usuario_activo)
        elif opcion == "7":
            proyecciones_y_planes(perfil_usuario)
        elif opcion == "8":
            print("Cerrando sesión.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una de las opciones del menú.")

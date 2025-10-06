import datetime
# Importaciones de las clases desde el paquete 'models'
from models.usuario import Usuario
from models.perfil_financiero import PerfilFinanciero
from models.presupuesto import Presupuesto
from models.categoria import Categoria
from models.ingreso import Ingreso
from models.gasto import Gasto
from models.ahorro import Ahorro
from models.alerta import Alerta
from utils.CONSTANTES import CATEGORIAS_INGRESOS_DISPONIBLES, CATEGORIAS_GASTOS_DISPONIBLES


def mostrar_menu_principal(nombre_usuario: str):
    """Muestra el menú principal personalizado para el usuario activo."""
    print(f"\n--- MENÚ PRINCIPAL de {nombre_usuario} ---")
    print("1. Gestionar Ingresos")
    print("2. Gestionar Gastos")
    print("3. Gestionar Ahorros")
    print("4. Gestionar Presupuestos")
    print("5. Ver Resumen Financiero y Alertas")
    print("6. Cerrar Sesión")

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
                for cat in [c for c in CATEGORIAS_INGRESOS_DISPONIBLES if c.tipo == "Ingreso"]:
                    print(f"ID: {cat.id_categoria}, Nombre: {cat.nombre}")
                cat_id = int(input("ID de la categoría: "))
                categoria = next((c for c in CATEGORIAS_INGRESOS_DISPONIBLES if c.id_categoria == cat_id and c.tipo == "Ingreso"), None)
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
                for cat in [c for c in CATEGORIAS_GASTOS_DISPONIBLES if c.tipo == "Gasto"]:
                    print(f"ID: {cat.id_categoria}, Nombre: {cat.nombre}")
                cat_id = int(input("ID de la categoría: "))
                categoria = next((c for c in CATEGORIAS_GASTOS_DISPONIBLES if c.id_categoria == cat_id and c.tipo == "Gasto"), None)
                if categoria:
                    nuevo_gasto = Gasto(id_gasto=len(perfil_usuario.gastos_registrados) + 1, monto=monto, categoria=categoria, fecha=datetime.date.today(), tipo="Variable", descripcion=descripcion)
                    perfil_usuario.agregar_gasto(nuevo_gasto)
                    print("Gasto agregado con éxito.")
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
        print("1. Crear/Modificar presupuesto mensual")
        print("2. Ver presupuestos existentes")
        print("3. Ver resumen de presupuesto mensual")
        print("4. Volver al menú principal")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                mes = int(input("Mes (1-12) para el presupuesto: "))
                anio = int(input("Año para el presupuesto: "))
                monto_total = float(input("Monto total del presupuesto: "))
                
                limites = {}
                print("Define límites por categoría de gasto:")
                for cat in [c for c in CATEGORIAS_GASTOS_DISPONIBLES if c.tipo == "Gasto"]:
                    limite_str = input(f"Límite para '{cat.nombre}' (dejar vacío para no limitar): ")
                    if limite_str:
                        limites[cat.nombre] = float(limite_str)

                clave = f"{mes}_{anio}"
                if clave in perfil_usuario.presupuestos:
                    presupuesto = perfil_usuario.presupuestos[clave]
                    presupuesto.crear_presupuesto(monto_total, limites)
                else:
                    nuevo_presupuesto = Presupuesto(id_presupuesto=len(perfil_usuario.presupuestos)+1, usuario=usuario_activo, monto_total=monto_total, mes=mes, anio=anio)
                    nuevo_presupuesto.crear_presupuesto(monto_total, limites)
                    perfil_usuario.agregar_presupuesto(nuevo_presupuesto)
            except ValueError:
                print("Entrada inválida. Asegúrate de ingresar números.")
        elif opcion == "2":
            print("\n--- LISTA DE PRESUPUESTOS ---")
            if not perfil_usuario.presupuestos:
                print("No hay presupuestos configurados.")
            else:
                for clave, presupuesto in perfil_usuario.presupuestos.items():
                    print(f"- {presupuesto}")
        elif opcion == "3":
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
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def ver_resumen_y_alertas(perfil_usuario: PerfilFinanciero, usuario_activo: Usuario):
    """Muestra el resumen financiero y las alertas activas."""
    print(perfil_usuario.obtener_resumen_financiero())
    print("\n--- ALERTAS ACTIVAS ---")
    if not usuario_activo.alertas:
        print("No hay alertas pendientes.")
    else:
        for alerta in usuario_activo.alertas:
            if alerta.activo:
                print(alerta.obtener_detalle())

def iniciar_menu_principal(usuario_activo: Usuario):
    """
    Función principal del menú, que recibe el objeto Usuario activo.
    Esta es la función que se exportará a menu_autenticacion.py
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
            print("Cerrando sesión.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una de las opciones del menú.")

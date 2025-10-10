from models.usuario import Usuario
from models.perfil_financiero import PerfilFinanciero
from views.menu_principal import iniciar_menu_principal

# Simulación de la "base de datos"
usuarios_registrados = {}

def registrar_nuevo_usuario():
    print("\n--- REGISTRO DE USUARIO ---")
    nombre = input("Ingresa tu nombre: ")
    email = input("Ingresa tu email: ")
    password = input("Ingresa tu contraseña: ")
    
    if any(user.email == email for user in usuarios_registrados.values()):
        print("El email ya está registrado. Intenta con otro.")
        return

    new_id = len(usuarios_registrados) + 1
    nuevo_usuario = Usuario(id_usuario=new_id, nombre=nombre, email=email, password=password)
    nuevo_usuario.registrar_usuario(nombre, email, password)
    usuarios_registrados[new_id] = nuevo_usuario
    print(f"Usuario {nombre} registrado con éxito. ¡Ahora puedes iniciar sesión!")

def iniciar_sesion():
    print("\n--- INICIO DE SESIÓN ---")
    email = input("Email: ")
    password = input("Contraseña: ")

    for user in usuarios_registrados.values():
        if user.email == email and user.password == password:
            print(f"¡Bienvenido, {user.nombre}!")
            # VERIFICACIÓN CLAVE: Asegurarse de que el perfil financiero existe.
            if user.perfil_financiero is None:
                user.perfil_financiero = PerfilFinanciero(usuario=user)
                print("Se ha creado un nuevo perfil financiero para el usuario.")
            return user
    print("Email o contraseña incorrectos.")
    return None

def menu_autenticacion():
    while True:
        print("\n--- BIENVENIDO AL GESTOR FINANCIERO ---")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            registrar_nuevo_usuario()
        elif opcion == "2":
            usuario_logueado = iniciar_sesion()
            if usuario_logueado:
                iniciar_menu_principal(usuario_logueado)
        elif opcion == "3":
            print("Saliendo de la aplicación. ¡Hasta pronto!")
            return
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
            
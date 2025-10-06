import sys
from views.menu_autenticacion import menu_autenticacion

def main():
    while True:
        print("\n=== IMPULSO FINANCIERO ===")
        print("1. Iniciar sesión / Registrarse")
        print("0. Salir")

        opcion = input("Seleccioná una opción: ").strip()

        if opcion == "1":
            try:
                menu_autenticacion()
            except Exception as e:
                print(f"⚠️ Ocurrió un error inesperado: {e}")
        elif opcion == "0":
            print("👋 ¡Hasta luego!")
            sys.exit(0)
        else:
            print("❌ Opción inválida. Probá de nuevo.")

if __name__ == "__main__":
    main()
    
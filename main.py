# main.py - Punto de entrada del programa
from src.gt import auth
from src.gt import tareas
import getpass


def mostrar_menu_principal():
    print("\n--- Bienvenido a GestorT ---")
    print("1. Iniciar sesión")
    print("2. Crear cuenta")
    print("3. Salir")
    return input("Elige una opción: ")


def mostrar_menu_usuario(usuario):
    print(f"\n--- Menú de {usuario} ---")
    print("1. Crear tarea")
    print("2. Listar tareas")
    print("3. Editar tarea")
    print("4. Eliminar tarea")
    print("5. Marcar tarea como completada")
    print("6. Cambiar contraseña")
    print("7. Cerrar sesión")
    return input("Elige una opción: ")


def gestionar_tareas(usuario):
    while True:
        opcion = mostrar_menu_usuario(usuario)

        if opcion == "1":
            titulo = input("Título de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            if tareas.crear_tarea(usuario, titulo, descripcion):
                print("✅ Tarea creada exitosamente.")
            else:
                print("❌ Error al crear la tarea.")

        elif opcion == "2":
            lista = tareas.listar_tareas(usuario)
            if not lista:
                print("📭 No tienes tareas.")
            else:
                for i, tarea in enumerate(lista, start=1):
                    estado = "✅" if tarea["completada"] else "❌"
                    print(f"{i}. {tarea['titulo']} - {tarea['descripcion']} [{estado}]")

        elif opcion == "3":
            lista = tareas.listar_tareas(usuario)
            if not lista:
                print("📭 No tienes tareas para editar.")
                continue

            for i, tarea in enumerate(lista, start=1):
                print(f"{i}. {tarea['titulo']}")

            indice = int(input("Número de la tarea a editar: ")) - 1
            nuevo_titulo = input("Nuevo título: ")
            nueva_descripcion = input("Nueva descripción: ")

            if tareas.editar_tarea(usuario, indice, nuevo_titulo, nueva_descripcion):
                print("✅ Tarea editada correctamente.")
            else:
                print("❌ Error al editar la tarea.")

        elif opcion == "4":
            lista = tareas.listar_tareas(usuario)
            if not lista:
                print("📭 No tienes tareas para eliminar.")
                continue

            for i, tarea in enumerate(lista, start=1):
                print(f"{i}. {tarea['titulo']}")

            indice = int(input("Número de la tarea a eliminar: ")) - 1
            if tareas.eliminar_tarea(usuario, indice):
                print("✅ Tarea eliminada correctamente.")
            else:
                print("❌ Error al eliminar la tarea.")

        elif opcion == "5":
            lista = tareas.listar_tareas(usuario)
            if not lista:
                print("📭 No tienes tareas para marcar como completadas.")
                continue

            for i, tarea in enumerate(lista, start=1):
                print(f"{i}. {tarea['titulo']}")

            indice = int(input("Número de la tarea a marcar como completada: ")) - 1
            if tareas.marcar_completada(usuario, indice):
                print("✅ Tarea marcada como completada.")
            else:
                print("❌ Error al marcar la tarea.")

        elif opcion == "6":
            actual = input("Contraseña actual: ")
            nueva = input("Nueva contraseña: ")
            if auth.cambiar_contraseña(usuario, actual, nueva):
                print("✅ Contraseña cambiada exitosamente.")
            else:
                print("❌ La contraseña actual es incorrecta.")

        elif opcion == "7":
            print("👋 Sesión cerrada.")
            break
        else:
            print("⚠️ Opción inválida.")


def main():
    while True:
        opcion = mostrar_menu_principal()

        if opcion == "1":
            usuario = input("Usuario: ")
            contraseña = getpass.getpass("Contraseña: ")
            if auth.iniciar_sesion(usuario, contraseña):
                print(f"✅ Bienvenido {usuario}!")
                gestionar_tareas(usuario)
            else:
                print("❌ Usuario o contraseña incorrectos.")

        elif opcion == "2":
            usuario = input("Nuevo usuario: ")
            contraseña = getpass.getpass("Nueva contraseña: ")
            if auth.crear_cuenta(usuario, contraseña):
                print("✅ Cuenta creada exitosamente.")
            else:
                print("❌ El usuario ya existe.")

        elif opcion == "3":
            print("👋 Adiós!")
            break

        else:
            print("⚠️ Opción inválida.")


if __name__ == "__main__":
    main()

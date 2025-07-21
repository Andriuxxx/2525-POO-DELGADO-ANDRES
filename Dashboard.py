import os

# DASHBOARD POO – VERSION ADAPTADA

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def listar_tareas(tareas):
    print("\n📚 Lista de Tareas y Proyectos de POO:\n")
    for i, (nombre, ruta) in enumerate(tareas.items(), 1):
        print(f"{i}. {nombre} -> {ruta}")
    print("0. Volver al menú")


def ver_tarea(tareas):
    listar_tareas(tareas)
    opcion = input("\n🔎 Elige el número de la tarea para ver su código: ")

    if opcion.isdigit():
        opcion = int(opcion)
        if opcion == 0:
            return
        elif 1 <= opcion <= len(tareas):
            ruta = list(tareas.values())[opcion - 1]
            if os.path.exists(ruta):
                with open(ruta, 'r', encoding='utf-8') as archivo:
                    print(f"\n📄 Código de {ruta}:\n")
                    print(archivo.read())
            else:
                print("❌ El archivo no existe.")
        else:
            print("⚠ Opción inválida.")
    else:
        print("⚠ Ingresa solo números.")


def agregar_tarea(tareas):
    nombre = input("📝 Nombre descriptivo de la tarea: ")
    ruta = input("📂 Ruta relativa al archivo .py: ")

    if os.path.exists(ruta):
        tareas[nombre] = ruta
        print("✅ Tarea agregada correctamente.")
    else:
        print("❌ La ruta no existe. Verifica el nombre o la ubicación.")


def menu_principal():
    tareas = {
        "Ejemplo Técnicas de Programación (U1)": "UNIDAD 1/1.2. Tecnicas de Programacion/1.2.1. Ejemplo Tecnicas de Programacion.py",
        "Clases y Objetos (U2)": "UNIDAD 2/POO/2.1. Clases y Objetos.py",
        "Hilos y Multiprocesamiento (U3)": "UNIDAD 3/Hilos/3.1. Hilos y Multiprocesamiento.py"
    }

    while True:
        print("\n==== DASHBOARD DE PROYECTOS - POO 2025 ====")
        print("1. Ver lista de tareas y mostrar código")
        print("2. Agregar nueva tarea o proyecto")
        print("0. Salir")
        print("===========================================")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            ver_tarea(tareas)
        elif opcion == '2':
            agregar_tarea(tareas)
        elif opcion == '0':
            print("👋 Cerrando el Dashboard...")
            break
        else:
            print("⚠ Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    limpiar_pantalla()
    menu_principal()

import random
import math
from typing import List, Tuple

# Definir la lista de trabajadores
trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
    "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez",
    "Isabel Gómez", "Francisco Díaz", "Elena Fernández"
]

# Comenzar con la lista de sueldos con saldo cero
sueldos = [0] * len(trabajadores)

def asignar_sueldos_aleatorios() -> List[int]:
    """Asigna sueldos aleatorios a los trabajadores y los guarda en la lista sueldos.
    Los sueldos son números enteros entre 300,000 y 2,500,000."""
    sueldos = [random.randint(300000, 2500000) for _ in trabajadores]
    print("Sueldos asignados exitosamente.")
    return sueldos

def clasificar_sueldos(sueldos: List[int]) -> List[Tuple[str, int, str]]:
    """Clasifica los sueldos en 'Bajo', 'Medio' y 'Alto'
    y muestra el sueldo con su respectiva clasificación."""
    clasificaciones = [("Bajo" if s < 500000 else "Medio" if s < 1500000 else "Alto") for s in sueldos]
    resultado = list(zip(trabajadores, sueldos, clasificaciones))
    for trabajador, sueldo, clasificacion in resultado:
        print(f"{trabajador}: ${sueldo:,} - {clasificacion}")
    return resultado

def ver_estadisticas(sueldos: List[int]) -> None:
    """Mostrar estadísticas sobre los sueldos: el sueldo más alto, el sueldo más bajo,
    el promedio de sueldos y la media geométrica."""
    max_sueldo = max(sueldos)
    min_sueldo = min(sueldos)
    promedio_sueldo = sum(sueldos) / len(sueldos)
    try:
        media_geometrica = math.exp(sum(math.log(s) for s in sueldos if s > 0) / len(sueldos))
    except ValueError as e:
        print(f"Error al calcular la media geométrica: {e}")
        media_geometrica = float('nan')

    print(f"Sueldo más alto: ${max_sueldo:,}")
    print(f"Sueldo más bajo: ${min_sueldo:,}")
    print(f"Promedio de sueldos: ${promedio_sueldo:,}")
    print(f"Media geométrica: ${media_geometrica:,.2f}")

def reporte_sueldos(sueldos: List[int]) -> None:
    """Generar un reporte que detalle para cada trabajador el sueldo base,
    el descuento de salud, el descuento AFP y el sueldo líquido."""
    for trabajador, sueldo in zip(trabajadores, sueldos):
        descuento_salud = sueldo * 0.07
        descuento_afp = sueldo * 0.12
        sueldo_liquido = sueldo - descuento_salud - descuento_afp
        print(f"{trabajador}")
        print(f" Sueldo Base: ${sueldo:,}")
        print(f" Descuento Salud (7%): ${descuento_salud:,.2f}")
        print(f" Descuento AFP (12%): ${descuento_afp:,.2f}")
        print(f" Sueldo Líquido: ${sueldo_liquido:,.2f}")
        print()

def obtener_opcion_menu() -> int:
    """Solicitar al usuario que seleccione una opción del menú y validarla."""
    while True:
        try:
            opcion = int(input("Seleccione una opción (1-5): "))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("Por favor, seleccione una opción válida entre 1 y 5.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entre 1 y 5.")

def menu() -> None:
    """Mostrar el menú del programa y permite al usuario seleccionar una opción
    para desplazarse por la aplicación. Ejecuta la función correspondiente a la opción seleccionada."""
    sueldos = [0] * len(trabajadores)
    while True:
        print("\nMenu:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = obtener_opcion_menu()

        if opcion == 1:
            sueldos = asignar_sueldos_aleatorios()
        elif opcion == 2:
            clasificar_sueldos(sueldos)
        elif opcion == 3:
            ver_estadisticas(sueldos)
        elif opcion == 4:
            reporte_sueldos(sueldos)
        elif opcion == 5:
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    menu()

# calculadora.py

# Importamos el módulo sys para poder salir del programa cuando el usuario lo desee
import sys


# -------------------------
# FUNCIÓN: calcular_factorial
# -------------------------
def calcular_factorial(n):
    """Devuelve el factorial de un número entero positivo n."""
    if n < 0:
        # Si el número es negativo, lanzamos un error
        raise ValueError("El número debe ser positivo.")
    elif n == 0 or n == 1:
        # El factorial de 0 y 1 es siempre 1
        return 1
    else:
        # Calculamos el factorial multiplicando todos los enteros desde 1 hasta n
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado


# -------------------------
# FUNCIÓN: calcular_fibonacci
# -------------------------
def calcular_fibonacci(n):
    """Devuelve el número de Fibonacci en la posición n."""
    if n < 0:
        raise ValueError("El número debe ser positivo.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


# -------------------------
# FUNCIÓN: mostrar_menu
# -------------------------
def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n===== MENÚ DE OPCIONES =====")
    print("1. Calcular un valor de la Serie de Fibonacci")
    print("2. Calcular el Factorial de un número")
    print("3. Salir del programa")
    print("=============================")


# -------------------------
# PROGRAMA PRINCIPAL
# -------------------------
if __name__ == "__main__":
    while True:
        mostrar_menu()  # Mostramos las opciones
        opcion = input("Elige una opción (1-3): ")

        if opcion == "1":
            # Opción para calcular Fibonacci
            try:
                n = int(input("Introduce un número entero positivo: "))
                resultado = calcular_fibonacci(n)
                print(f"El número de Fibonacci en la posición {n} es: {resultado}")
            except ValueError as e:
                print("Error:", e)

        elif opcion == "2":
            # Opción para calcular Factorial
            try:
                n = int(input("Introduce un número entero positivo: "))
                resultado = calcular_factorial(n)
                print(f"El factorial de {n} es: {resultado}")
            except ValueError as e:
                print("Error:", e)

        elif opcion == "3":
            # Salir del programa
            print("Saliendo del programa... ¡Hasta luego!")
            sys.exit()

        else:
            # Opción inválida
            print("Opción no válida. Por favor, elige 1, 2 o 3.")

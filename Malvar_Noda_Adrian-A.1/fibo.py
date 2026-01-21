# fibo.py

# Definimos una función llamada fibonacci que recibe un número entero n.
def fibonacci(n):
    """Devuelve el número de Fibonacci en la posición n."""

    # Si el número es negativo, lanzamos un error porque la sucesión no está definida para negativos.
    if n < 0:
        raise ValueError("El número debe ser positivo")

    # Si n es 0, el valor de Fibonacci es 0 (caso base).
    elif n == 0:
        return 0

    # Si n es 1, el valor de Fibonacci es 1 (segundo caso base).
    elif n == 1:
        return 1

    # Si n es mayor o igual a 2, usamos un bucle para calcular la secuencia.
    else:
        a, b = 0, 1  # 'a' es el número anterior y 'b' el actual (iniciamos con F(0)=0 y F(1)=1)
        # Repetimos el cálculo desde la posición 2 hasta n (inclusive)
        for _ in range(2, n + 1):
            a, b = b, a + b  # Avanzamos la secuencia: el nuevo número es la suma de los dos anteriores
        return b  # Devolvemos el número que corresponde a la posición n


# Este bloque solo se ejecuta si el archivo se ejecuta directamente (no cuando se importa desde otro script)
if __name__ == "__main__":
    # Pedimos al usuario que introduzca la posición que quiere calcular
    limite = int(input("Introduce la posición hasta la que deseas calcular Fibonacci: "))

    # Mostramos un mensaje con la posición que se calculará
    print(f"La secuencia de Fibonacci hasta la posición {limite} es:")

    # Usamos un bucle for para mostrar todos los números desde F(0) hasta F(límite)
    for i in range(limite + 1):
        # Llamamos a la función fibonacci para cada número y mostramos el resultado
        print(f"F({i}) = {fibonacci(i)}")

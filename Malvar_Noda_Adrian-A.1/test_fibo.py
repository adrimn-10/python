# test_fibo.py

# Importamos la librería de pruebas de software incluida en Python
import unittest

# Importamos la función fibonacci desde el archivo fibo.py
from fibo import fibonacci


# Creamos una clase de prueba que hereda de unittest.TestCase
class TestFibonacci(unittest.TestCase):
    """Clase de pruebas para la función fibonacci."""

    # Definimos una función de prueba. Los métodos de prueba deben empezar por 'test_'
    def test_quinto_numero(self):
        """Comprobar que el quinto número de Fibonacci sea 3."""

        # Llamamos a la función fibonacci con el valor 4
        # (recordemos: F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(4)=3)
        result = fibonacci(4)

        # Comprobamos si el resultado devuelto por la función es igual a 3
        # Si no lo es, la prueba fallará
        self.assertEqual(result, 3)


# Este bloque indica que si ejecutamos directamente este archivo,
# Python debe ejecutar las pruebas definidas arriba.
if __name__ == '__main__':
    unittest.main()

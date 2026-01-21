# test_calculadora.py

import unittest
from calculadora import calcular_factorial, calcular_fibonacci


class TestCalculos(unittest.TestCase):
    """Clase de pruebas para las funciones de cálculo."""

    # -------------------------
    # PRUEBAS PARA FACTORIAL
    # -------------------------
    def test_factorial_base(self):
        """Comprobar casos base del factorial."""
        self.assertEqual(calcular_factorial(0), 1)
        self.assertEqual(calcular_factorial(1), 1)

    def test_factorial_valor(self):
        """Comprobar un caso normal de factorial."""
        self.assertEqual(calcular_factorial(5), 120)  # 5! = 120

    def test_factorial_error(self):
        """Comprobar que lanza error con número negativo."""
        with self.assertRaises(ValueError):
            calcular_factorial(-3)

    # -------------------------
    # PRUEBAS PARA FIBONACCI
    # -------------------------
    def test_fibonacci_base(self):
        """Comprobar casos base de Fibonacci."""
        self.assertEqual(calcular_fibonacci(0), 0)
        self.assertEqual(calcular_fibonacci(1), 1)

    def test_fibonacci_valor(self):
        """Comprobar un caso normal de Fibonacci."""
        self.assertEqual(calcular_fibonacci(6), 8)  # Serie: 0,1,1,2,3,5,8

    def test_fibonacci_error(self):
        """Comprobar que lanza error con número negativo."""
        with self.assertRaises(ValueError):
            calcular_fibonacci(-5)


if __name__ == '__main__':
    unittest.main()

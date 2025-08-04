import unittest
class TestEjemplos(unittest.TestCase):
    def test_in(self):
    	# Ok ya que 1 esta contenido en [1, 2, 3]
        self.assertIn(1, [1, 2, 3])

    def test_is(self):
        a = [1, 2, 3]
        b = a
        # Ok ya que son el mismo objeto
        self.assertIs(a, b)

    def test_excepcion(self):
    	# Dividir 0/0 da error, pero es lo esperado por el test
        with self.assertRaises(ZeroDivisionError):
            x = 0/0
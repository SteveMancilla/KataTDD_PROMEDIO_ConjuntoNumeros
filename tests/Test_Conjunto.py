import unittest
from src.logica.Conjunto import CalcularPromedioPonderado

class TestCalcularPromedioPonderado(unittest.TestCase):
    def test_promedio_ponderado(self):
        calcular = CalcularPromedioPonderado()
        #Entrada de datos
        Datos = ([])
        Peso = ([])
        resultado = calcular.PromedioPonderado()
        self.assertAlmostEqual(resultado, None, 1)

if __name__=='__main__':
    unittest.main()
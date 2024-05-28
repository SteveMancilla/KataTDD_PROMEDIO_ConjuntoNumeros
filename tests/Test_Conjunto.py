import unittest
from src.logica.Conjunto import CalcularPromedioPonderado

class TestCalcularPromedioPonderado(unittest.TestCase):
    def test_promedio_ponderado(self):
        calcular = CalcularPromedioPonderado()
        #Entrada de datos
        Datos = [10, 12, 14] 
        Pesos = [3, 4]
        resultado = calcular.PromedioPonderado(Datos,Pesos)
        self.assertAlmostEqual(resultado, 11.78, 2)

if __name__=='__main__':
    unittest.main()
import unittest
from src.logica.Conjunto import CalcularPromedioPonderado

class TestCalcularPromedioPonderado(unittest.TestCase):
    def test_promedio_ponderado(self):
        calcular = CalcularPromedioPonderado()
        #Entrada de datos
        datos = [10, 12, 14] 
        pesos = [3, 4, 2]
        resultado = calcular.PromedioPonderado(datos,pesos)
        self.assertAlmostEqual(resultado, 11.78, 2)
    
    def test_conjuntos_vacios(self):
        calcular = CalcularPromedioPonderado()
        datos = []
        pesos = []
        with self.assertRaises(ValueError):
            calcular.PromedioPonderado(datos, pesos)
    
    def test_longitudes_diferentes(self):
        calcular = CalcularPromedioPonderado()
        datos = [15, 15, 17]
        pesos = [3, 4, 2, 5, 9]
        
        with self.assertRaises(ValueError):
            calcular.PromedioPonderado(datos, pesos)

if __name__=='__main__':
    unittest.main()
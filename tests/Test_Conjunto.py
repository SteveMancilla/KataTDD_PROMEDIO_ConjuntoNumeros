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
        resultado = calcular.PromedioPonderado(datos, pesos)
        self.assertAlmostEqual(resultado,0,2)
        '''with self.assertRaises(ValueError):
            calcular.PromedioPonderado(datos, pesos)'''

if __name__=='__main__':
    unittest.main()
class CalcularPromedioPonderado:
    def PromedioPonderado(self, valores, pesos):
        if len(valores) != len(pesos):
            raise ValueError("Los valores y los pesos deben de tenre la misma longitud")
        
        suma_ponderada = sum(valores * pesos for valores, pesos in zip(valores, pesos))
        suma_pesos = sum(pesos)
        
        if suma_pesos == 0:
            raise ValueError("La suma de los pesos no debe de ser cero")
        
        promedio_ponderado = suma_ponderada/suma_pesos
        return promedio_ponderado
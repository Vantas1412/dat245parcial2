import numpy as np

class RedNeuronal:
    def __init__(self, tamano_entrada, tamano_oculta, tamano_salida, tasa_aprendizaje=0.2):
        self.tamano_entrada = tamano_entrada
        self.tamano_oculta = tamano_oculta
        self.tamano_salida = tamano_salida
        self.tasa_aprendizaje = tasa_aprendizaje
        
        # Inicialización de pesos y sesgos
        self.W1 = np.random.randn(tamano_entrada, tamano_oculta)
        self.b1 = np.zeros((1, tamano_oculta))
        self.W2 = np.random.randn(tamano_oculta, tamano_salida)
        self.b2 = np.zeros((1, tamano_salida))
        
    def funcion_activacion_escalon(self, x):
        return np.where(x >= 0, 1, 0)
    
    def hacia_adelante(self, X):
        # Capa oculta
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.funcion_activacion_escalon(self.z1)
        
        # Capa de salida
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.funcion_activacion_escalon(self.z2)
        
        return self.a2

# Ejemplo de uso
tamano_entrada = 4
tamano_oculta = 5
tamano_salida = 1

rn = RedNeuronal(tamano_entrada, tamano_oculta, tamano_salida, tasa_aprendizaje=0.2)

# Ejemplo de propagación hacia adelante
X_ejemplo = np.array([[1, 2, 3, 4]])
salida = rn.hacia_adelante(X_ejemplo)
print("Salida de la red neuronal:", salida)

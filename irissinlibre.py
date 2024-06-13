import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Codificación one-hot de las etiquetas
encoder = OneHotEncoder(sparse_output=False)
y = encoder.fit_transform(y.reshape(-1, 1))

# Dividir los datos en conjunto de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)
class RedNeuronal:
    def __init__(self, tamano_entrada, tamano_oculto, tamano_salida, tasa_aprendizaje=0.4):
        self.tamano_entrada = tamano_entrada
        self.tamano_oculto = tamano_oculto
        self.tamano_salida = tamano_salida
        self.tasa_aprendizaje = tasa_aprendizaje
        
        # Inicializar pesos
        self.W1 = np.random.randn(tamano_entrada, tamano_oculto)
        self.b1 = np.zeros((1, tamano_oculto))
        self.W2 = np.random.randn(tamano_oculto, tamano_salida)
        self.b2 = np.zeros((1, tamano_salida))
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def derivada_sigmoid(self, x):
        return x * (1 - x)
    
    def hacia_adelante(self, X):
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)
        return self.a2
    
    def hacia_atras(self, X, y, salida):
        error_salida = y - salida
        delta_salida = error_salida * self.derivada_sigmoid(salida)
        
        error_oculto = delta_salida.dot(self.W2.T)
        delta_oculto = error_oculto * self.derivada_sigmoid(self.a1)
        
        self.W2 += self.a1.T.dot(delta_salida) * self.tasa_aprendizaje
        self.b2 += np.sum(delta_salida, axis=0, keepdims=True) * self.tasa_aprendizaje
        self.W1 += X.T.dot(delta_oculto) * self.tasa_aprendizaje
        self.b1 += np.sum(delta_oculto, axis=0) * self.tasa_aprendizaje
    
    def entrenar(self, X, y, epocas=1000):
        for epoca in range(epocas):
            salida = self.hacia_adelante(X)
            self.hacia_atras(X, y, salida)
            if epoca % 50 == 0:
                perdida = np.mean(np.square(y - salida))
                print(f"Época {epoca} - Pérdida: {perdida}")

# Crear una instancia de la red neuronal
rn = RedNeuronal(tamano_entrada=4, tamano_oculto=5, tamano_salida=3, tasa_aprendizaje=0.4)

# Entrenar la red neuronal
rn.entrenar(X_entrenamiento, y_entrenamiento, epocas=1000)
def predecir(rn, X):
    salida = rn.hacia_adelante(X)
    return np.argmax(salida, axis=1)

y_pred_entrenamiento = predecir(rn, X_entrenamiento)
y_pred_prueba = predecir(rn, X_prueba)

y_entrenamiento_real = np.argmax(y_entrenamiento, axis=1)
y_prueba_real = np.argmax(y_prueba, axis=1)

precision_entrenamiento = np.mean(y_pred_entrenamiento == y_entrenamiento_real)
precision_prueba = np.mean(y_pred_prueba == y_prueba_real)

print(f"Precisión en entrenamiento: {precision_entrenamiento * 100:.2f}%")
print(f"Precisión en prueba: {precision_prueba * 100:.2f}%")

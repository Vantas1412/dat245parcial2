import numpy as np

# Función para calcular la distancia entre dos ciudades
def distancia(ciudad1, ciudad2):
    return np.linalg.norm(ciudad1 - ciudad2)

# Algoritmo de búsqueda del vecino más cercano
def vecino_mas_cercano(ciudades):
    num_ciudades = len(ciudades)
    no_visitadas = set(range(num_ciudades))
    ciudad_actual = np.random.choice(list(no_visitadas))
    no_visitadas.remove(ciudad_actual)
    recorrido = [ciudad_actual]
    
    while no_visitadas:
        ciudad_mas_cercana = min(no_visitadas, key=lambda ciudad: distancia(ciudades[ciudad_actual], ciudades[ciudad]))
        no_visitadas.remove(ciudad_mas_cercana)
        recorrido.append(ciudad_mas_cercana)
        ciudad_actual = ciudad_mas_cercana
    
    # Cerrar el ciclo volviendo a la primera ciudad
    recorrido.append(recorrido[0])
    return recorrido

# Ejemplo de uso
# Generar ciudades aleatorias
num_ciudades = 10
ciudades = np.random.rand(num_ciudades, 2)  # Coordenadas de las ciudades

# Aplicar el algoritmo de búsqueda del vecino más cercano
ruta = vecino_mas_cercano(ciudades)

print("Ruta encontrada:", ruta)

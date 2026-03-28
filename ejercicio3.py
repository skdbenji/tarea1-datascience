# ejercicio 3

estudiantes = [
{"nombre": "Ana", "notas": [6.5, 7.0, 5.8]},
{"nombre": "Luis", "notas": [4.2, 5.1, 6.0]},
{"nombre": "Sofía", "notas": [3.9, 4.0, 4.5]},
{"nombre": "Pedro", "notas": [5.5, 6.1, 5.9]},
{"nombre": "Valentina", "notas": [7.0, 6.8, 6.9]},
{"nombre": "Javier", "notas": [4.0, 4.2, 4.1]},
{"nombre": "Camila", "notas": [5.0, 5.5, 5.8]},
{"nombre": "Martín", "notas": [3.5, 4.0, 4.2]},
{"nombre": "Fernanda", "notas": [6.2, 6.5, 6.0]},
{"nombre": "Tomás", "notas": [4.8, 5.0, 5.2]},
{"nombre": "Josefa", "notas": [5.9, 6.0, 6.1]},
{"nombre": "Matías", "notas": [3.8, 4.1, 4.0]},
{"nombre": "Ignacio", "notas": [6.7, 6.9, 7.0]},
{"nombre": "Daniela", "notas": [5.2, 5.4, 5.6]},
{"nombre": "Sebastián", "notas": [4.3, 4.5, 4.7]},
{"nombre": "Gabriela", "notas": [6.0, 6.2, 6.1]},
{"nombre": "Felipe", "notas": [5.7, 5.8, 5.9]},
{"nombre": "Antonia", "notas": [4.9, 5.0, 5.1]},
{"nombre": "Vicente", "notas": [3.7, 4.0, 4.3]},
{"nombre": "Paula", "notas": [6.3, 6.4, 6.5]}
]

# 3a. frecuencias de notas

def aplanar_notas(estudiantes):
    return [nota for est in estudiantes for nota in est['notas']]
    
def frecuencia_de_notas(datos):
    frecuencia= {}
    for valor in datos:
        frecuencia[valor] = frecuencia.get(valor, 0) + 1
    return frecuencia

def moda(frecuencia):
    if not frecuencia:
        return None
    valor_moda = max(frecuencia, key = frecuencia.get)
    return (valor_moda, frecuencia[valor_moda])

# 3b. histogramaa de texto

def histograma(frecuencia, ancho_max = 25):
    if not frecuencia: return
    max_frecuencia = max(frecuencia.values())
    orden_de_notas = sorted(frecuencia.keys(), reverse = True)
    for nota in orden_de_notas:
        frecuencias = frecuencia[nota]
        larg_barra = int((frecuencias / max_frecuencia) * ancho_max)
        barra = '*' * larg_barra
        print(f"{nota:.1f} | {barra} ({frecuencias})")

# 3c.clasificacion en tramos

def clasificar_en_tramos(datos, tramos):
    resultados = {nombre: 0 for nombre in tramos.keys()}
    for valor in datos:
        for nombre, limites in tramos.items():
            if limites[0] <= valor <= limites[1]:
                resultados[nombre] += 1
    return resultados

# 3d. analisis de texto

texto = """
La ciencia de datos es un campo interdisciplinario que utiliza
métodos científicos y algoritmos para extraer conocimiento de
los datos. La estadística y la programación son herramientas
fundamentales para un científico de datos. Los datos pueden
ser estructurados o no estructurados. El análisis de datos
permite tomar decisiones basadas en evidencia.
"""
def limpiar_texto(texto):
    puntuacion = ".,:;()[]{}!?'\"\n"
    texto_limpio = texto.lower()
    for simbolo in puntuacion:
        texto_limpio = texto_limpio.replace(simbolo, "")
    return texto_limpio

def frecuencia_de_palabras(texto):
    texto_limpio = limpiar_texto(texto)
    palabras = texto_limpio.split()
    frecuencia = {}
    for palabra in palabras:
        frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

def top_n_palabras(frecuencia, n = 10):
    items_ordenados = sorted(frecuencia.items(), key = lambda item: item[1], reverse = True)
    return items_ordenados[:n]

def diversidad_lexica(texto_limpio):
    palabras = texto_limpio.split()
    return len(set(palabras)) / len(palabras)

# 3e. bigramas

def calcular_bigramas(texto_limpio):
    bigramas = {}
    for i in range(len(texto_limpio) - 1):
        bigrama = f"{texto_limpio[i]} {texto_limpio[i + 1]}"
        bigramas[bigrama] = bigramas.get(bigrama, 0) + 1
    return bigramas


if __name__ == "__main__":

    print("-- 3a. Frecuencia de notas --")
    notas_planas =aplanar_notas(estudiantes)
    frecuencia = frecuencia_de_notas(notas_planas)
    print(frecuencia)
    resultado_moda = moda(frecuencia)
    if resultado_moda:
        print(f"moda: {resultado_moda[0]:.1f} con frecuencia {resultado_moda[1]}")
    else:
        print("No hay moda")    

    print("\n-- 3b. Histograma de texto --")
    histograma(frecuencia)

    print("\n-- 3c. Clasificación en tramos --")
    tramos = {"1.0-3.9": (1.0, 3.9), "4.0-5.9": (4.0, 5.9), "6.0-7.0": (6.0, 7.0)}
    print(clasificar_en_tramos(notas_planas, tramos))

    print("\n-- 3d. Análisis de texto --")
    frecuencia_palabras = frecuencia_de_palabras(texto)
    print("frecuencia de palabras:", frecuencia_palabras)
    print("top 10 palabras:", top_n_palabras(frecuencia_palabras))
    texto_limpio = limpiar_texto(texto)
    print("diversidad lexica:", diversidad_lexica(texto_limpio))

    print("\n-- 3e. Bigramas --")
    bigramas = calcular_bigramas(texto_limpio)
    print("bigramas:", bigramas)


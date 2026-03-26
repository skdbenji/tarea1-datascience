notas = [4.8, 6.2, 5.5, 3.9, 7.0, 4.1, 5.8, 6.0, 3.5, 5.2, 6.8, 2.9, 4.0, 5.0,
        6.5, 4.3, 5.7, 3.2, 6.1, 4.6]
#EL PROFE USARA LISTAS CON LETRAS Y VACIAS 
#..................
def calcular_suma(datos):

    suma = 0
    iterador = 0
    for iterador in datos:
        suma = suma + iterador
    
    return suma

#.................
def calcular_largo(datos):
    iterador = 0
    contador_largo = 0
    for iterador in datos:
        contador_largo = 1 + contador_largo
    
    return contador_largo

#.....................
def calcular_promedio(datos):

    promedio = calcular_suma(datos) / calcular_largo(datos)

    return promedio

#................
def calcular_minimo(datos):
    iterador = 0 
    minimo = datos[0]
    for iterador in datos:
        if iterador < minimo:
            minimo = iterador
    
    return minimo


def calcular_maximo(datos):
    iterador = 0 
    maximo = datos[0]
    for iterador in datos:
        if iterador > maximo:
            maximo = iterador
    
    return maximo

def burbuja(datos):
    largo = calcular_largo(datos)
    for i in range(largo):
        for j in range(0, largo - i - 1):
            if datos[j] > datos[j + 1]:
                datos[j], datos[j + 1] = datos[j + 1], datos[j]
    return datos


resultado_suma = calcular_suma(notas)

print("La suma de las notas es: ", resultado_suma)


resultado_largo = calcular_largo(notas)

print("La cantidad de notas es: " , resultado_largo)


resultado_promedio = calcular_promedio(notas)

print("El resultado del promedio es: " , resultado_promedio)


resultado_minimo = calcular_minimo(notas)

print("La nota minima es: ",resultado_minimo)


resultado_maximo = calcular_maximo(notas)

print("La nota maxima es: ",resultado_maximo)


datos_ordenados = burbuja(notas)

print("Los datos ordenados: ",datos_ordenados)
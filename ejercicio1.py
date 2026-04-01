notas = [4.8, 6.2, 5.5, 3.9, 7.0, 4.1, 5.8, 6.0, 3.5, 5.2, 6.8, 2.9, 4.0, 5.0,
        6.5, 4.3, 5.7, 3.2, 6.1, 4.6]
grados_c = [0,15,25,30,100]
notas_malas = [4.5, 6.0, "a", 5.2]



ciudades = [
{"ciudad": "Santiago", "temperaturas": [30.2, 28.5, 25.1, 18.3, 12.7, 9.5, 8.8, 10.1, 14.6, 19.3, 24.8, 28.9]},
{"ciudad": "Valparaíso", "temperaturas": [22.1, 21.8, 20.5, 17.2, 14.3, 12.1, 11.5, 12.0, 13.8, 16.5, 19.2, 21.0]},
{"ciudad": "Concepción", "temperaturas": [20.5, 19.8, 17.2, 13.5, 10.8, 8.5, 7.9, 9.2, 11.5, 14.8, 17.5, 19.8]},
{"ciudad": "Temuco", "temperaturas": [22.3, 21.5, 18.0, 13.2, 9.5, 7.0, 6.5, 8.0, 10.5, 14.0, 17.8, 20.5]},
{"ciudad": "Punta Arenas", "temperaturas": [14.2, 13.5, 11.0, 7.5, 4.2, 2.0, 1.5, 3.0, 6.5, 9.8, 12.0, 13.8]},
]
#Funcion para validar si un dato es numerico
def es_numero(valor):
    return isinstance(valor, (int, float))


#Esta funcion se encarga de sumar los datos 
def calcular_suma(datos):

    suma = 0 #La variable suma, se almacena la suma
    iterador = 0 # Iterador para recorrer los datos

    #Bucle en donde se recorren los datos 
    for iterador in datos: 
        if not es_numero(iterador):
            print("Error: hay datos no numericos en la suma")
            return None
        suma = suma + iterador #se suman y se almacenan en la variable suma
    
    #retorna el valor de la suma
    return suma


#Esta funcion se encarga de calcular el largo del arreglo
def calcular_largo(datos):

    iterador = 0 #Iterador para recorrer lo datos
    contador_largo = 0 #Variable que almacenara el contador de cuantos datos hay

    #Bucle en donde se recorren los datos
    for iterador in datos:
        contador_largo = 1 + contador_largo  #se suma 1 cada vez que hay un dato en el arreglo
    
    #retorna el valor de cuantos datos hay
    return contador_largo


#Esta funcion calcula el promedio de los datos
def calcular_promedio(datos):

    promedio = calcular_suma(datos) / calcular_largo(datos) #promedio almacena el valor de la division que retornan estas dos funciones "calcular_suma" y "calcular_largo" 
    
    if promedio is None:
        return None

    #retorna el valor del promedio
    return promedio


#Calcula el con menos valor en los datos
def calcular_minimo(datos):
    iterador = 0 #Iterador para recorrer los datos

    if calcular_largo(datos) == 0:
        return None

    minimo = datos[0] # en minimo, almacena el primer valor

    #Bucle para recorer los datos
    for iterador in datos: 
        if not es_numero(iterador):
            print("Error: hay datos no numericos en minimo")
            return None
        if iterador < minimo: #compara si el dato es menor que "minimo"
            minimo = iterador #Si es asi, al valor minimo se le almacena el dato que cumple esta condicion
    
    #Retorna el valor minimo
    return minimo


#Calcula el con mas valor en los datos
def calcular_maximo(datos):
    iterador = 0 #Iterador para recorrer los datos

    if calcular_largo(datos) == 0:
        return None

    maximo = datos[0] # en maximo, almacena el primer valor

    #Bucle para recorrer los datos  
    for iterador in datos:
        if not es_numero(iterador):
            print("Error: hay datos no numericos en maximo")
            return None
        if iterador > maximo: #compara si el dato es mayor que "maximo"
            maximo = iterador #Si es asi, el valor maximo se le almacena el dato que cumple esta condicion
    
    #Retorna el valor maximo
    return maximo


#Ordena los datos usando el metodo burbuja
def burbuja(datos):

    iterador = 0

    #Validacion de datos
    for iterador in datos:
        if not es_numero(iterador):
            print("Error: hay datos no numericos en ordenamiento")
            return None

    largo = calcular_largo(datos) #Obtiene la cantidad de elementos en la lista

    datos_copia = datos[:] #Copia de la lista para no modificar la original

    #Bucle externo para controlar la cantidad de pasadas
    for i in range(largo):
        
        #Bucle interno para comparar elementos adyacentes
        for j in range(0, largo - i - 1):
            
            #Compara si el elemento actual es mayor que el siguiente
            if datos_copia[j] > datos_copia[j + 1]:
                
                #Si es asi, intercambia las posiciones de los elementos
                datos_copia[j], datos_copia[j + 1] = datos_copia[j + 1], datos_copia[j]
    
    #Retorna la lista ordenada
    return datos_copia


#Calcula la mediana de los datos
def calcular_mediana(datos):
    datos_ord = burbuja(datos) #Llama a la funcion burbuja para obtener los datos ordenados

    if datos_ord is None:
        return None

    cantidad_datos = calcular_largo(datos) #En cantidad_datos se le almacena la cantidad de datos llamando a la funcion "calcular_largo"

    if cantidad_datos % 2 == 0: # verifica si los datos son cantidades pares
        dato_mitad = cantidad_datos // 2 # saca la mitad de los datos
        mediana = (datos_ord[dato_mitad-1] + datos_ord[dato_mitad]) / 2 #calcula la mediana
    else: #caso contrario, impares
        mitad = cantidad_datos // 2 # saca la mitad de los datos
        mediana = datos_ord[mitad] # se va a la posicion de la mitad
    
    #Retorna el valor de la mediana
    return mediana 


#Calcula la desviacion estandar de los datos
def calcular_desviacion_estandar(datos):
    
    promedio = calcular_promedio(datos) #Calcula el promedio de los datos

    if promedio is None:
        return None

    iterador = 0 #Iterador para recorrer los datos
    suma = [] #Lista para almacenar las diferencias al cuadrado

    #Bucle para recorrer los datos
    for iterador in datos:
        if not es_numero(iterador):
            print("Error: hay datos no numericos en desviacion estandar")
            return None
        
        #Calcula (dato - promedio)^2 y lo guarda en la lista
        suma.append((iterador - promedio)**2)
    
    promedio_para_desviacion = calcular_promedio(suma) #Promedio de las diferencias al cuadrado

    if promedio_para_desviacion is None:
        return None

    desviacion_estandar = promedio_para_desviacion ** 0.5 #Raiz cuadrada del promedio
    return desviacion_estandar #Retorna la desviacion estandar


#Convierte una lista de grados Celsius a Fahrenheit
def celsius_a_fahrenheit(grados_c):

    nueva_lista_farenheit = [] #Lista para almacenar los datos convertidos
    iterador = 0 #Iterador para recorrer los datos

    #Bucle para recorrer los datos
    for iterador in grados_c:
        if not es_numero(iterador):
            print("Error: hay datos no numericos en conversion")
            return None
        
        #Convierte el valor de Celsius a Fahrenheit
        dato_farenheit = ((9/5) * iterador) + 32
        
        #Agrega el valor convertido a la nueva lista
        nueva_lista_farenheit.append(dato_farenheit)
    
    #Retorna la lista con los valores en Fahrenheit
    return nueva_lista_farenheit


#Imprime un reporte de temperaturas por ciudad
def imprimir_reporte(ciudades):

    #Bucle para recorrer cada ciudad en la lista
    for ciudad in ciudades:
        
        nombre = ciudad["ciudad"] #Obtiene el nombre de la ciudad
        temperaturas = ciudad["temperaturas"] #Obtiene la lista de temperaturas

        promedio = calcular_promedio(temperaturas) #Calcula el promedio
        minimo = calcular_minimo(temperaturas) #Calcula la temperatura minima
        maximo = calcular_maximo(temperaturas) #Calcula la temperatura maxima

        if promedio is None or minimo is None or maximo is None:
            print("Error en los datos de la ciudad:", nombre)
            print("-----------------------------------")
            continue

        print("Ciudad:", nombre) #Imprime el nombre de la ciudad
        print("Promedio anual:", round(promedio, 2)) #Imprime el promedio redondeado
        print("Temperatura mínima:", minimo) #Imprime la minima
        print("Temperatura máxima:", maximo) #Imprime la maxima
        print("-----------------------------------") #Separador


#LLAMADA DE TODAS LAS FUNCIONES 

#FUNCION SUMA 
resultado_suma = calcular_suma(notas)
print("La suma de las notas es: ", resultado_suma)

#FUNCION CALCULAR LARGO
resultado_largo = calcular_largo(notas)
print("La cantidad de notas es: " , resultado_largo)

#FUNCION CALCULAR PROMEDIO
resultado_promedio = calcular_promedio(notas)
print("El resultado del promedio es: " , resultado_promedio)

#FUNCION CALCULAR MINIMO
resultado_minimo = calcular_minimo(notas)
print("La nota minima es: ",resultado_minimo)

#FUNCIOM CALCULAR MAXIMO
resultado_maximo = calcular_maximo(notas)
print("La nota maxima es: ",resultado_maximo)

#FUNCION PARA ORDENAR DATOS
datos_ordenados = burbuja(notas)
print("Los datos ordenados: ",datos_ordenados)

#FUNCION CALCULAR MEDIANA
resultado_mediana = calcular_mediana(notas)
print("El resultado de la mediana es: ",resultado_mediana)

#FUNCION CALCULAR DESVIACION ESTANDAR
resultado_desviacion_estandar = calcular_desviacion_estandar(notas)
print("El resultado de la desviacion estandar es: ",resultado_desviacion_estandar)

#CONVERTIR CELSIUS A FAHRENHEIT
convertura = celsius_a_fahrenheit(grados_c)
print("La nueva lista de grados fahrenheit: ",convertura)

#IMPRIMIR REPORTES DE LAS CIUDADES
imprimir_reporte(ciudades)

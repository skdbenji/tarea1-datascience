estudiantes = [
    {"nombre": "Ana", "notas": [6.5, 7.0, 5.8]},
    {"nombre": "Luis", "notas": [4.2, 5.1, 6.0]},
    {"nombre": "Sofía", "notas": [3.9, 4.0, 4.5]},

]

#Calcula el promedio del estudiante
def promedio_estudiante(estudiantes):
    #Retorna el promedio. La suma de las notas, divididas la cantidad de notas de los estudiantes                            
    return sum(estudiantes["notas"]) / len(estudiantes["notas"])


#Lo clasifica dentro de las categorías dependiendo su promedio
def clasificar_rendimiento(estudiantes):
    prom = promedio_estudiante(estudiantes) #Llama a la funcion para calcular el promedio de los estudiantes
    if prom<4.0: #Si el estudiante tiene nota menor que 4.0, reprueba
        return "Reprueba"
    elif prom>=4.0 and prom<5.0: #Notas mayor o igual a 4.0 y menor que 5.0, suficiente
        return "Suficiente"
    elif prom>=5.0 and prom<6.0: #Notas mayor o igual a 5.0 y menor que 6.0, aprueba
        return "Aprobado"
    else: #Caso contrario, es destacado
        return "Destacado"

#Genera un reporte de los datos del alumno
def generar_reporte(lista_estudiantes):
    reporte_estudiantes=[]
    for estudiante in lista_estudiantes:
        promedio_est=promedio_estudiante(estudiante)
        rendimiento=clasificar_rendimiento(estudiante)
        nota_max=max(estudiante["notas"])
        nota_min=min(estudiante["notas"])
        rango_notas=nota_max - nota_min

        reporte_estudiantes.append({
            "nombre": estudiante["nombre"],
            "promedio": promedio_est,
            "rendimiento": rendimiento,
            "nota_maxima": nota_max,
            "nota_minima": nota_min,
            "rango_notas": rango_notas
        })
    return reporte_estudiantes

#Cuenta cuantos de cada, dependiendo de su estado
def contar_por_estado(reporte):
    conteo_estado={}
    for fila in reporte:
        rendimiento=fila["rendimiento"]
        if rendimiento not in conteo_estado:
            conteo_estado[rendimiento]=0
        conteo_estado[rendimiento]+=1
    return conteo_estado
#Los filtra en base a su estado
def filtrar_por_estado(reporte,estado):
    cantidad_filtrados=[]
    for fila in reporte:
        if fila["rendimiento"] == estado:
            cantidad_filtrados.append(fila)
    return cantidad_filtrados

def ordenar_reporte(reporte_estudiantes,clave="promedio",descendente=True):
    return sorted(reporte_estudiantes,key=lambda fila: fila[clave],reverse=descendente)

def buscar_estudiante(estudiantes, nombre):
    
    iterador = 0
    
    for iterador in estudiantes:
        nombre_estudiante = iterador["nombre"]

        if nombre_estudiante.lower() == nombre.lower():
            return iterador
    
    return None

#Busca estudiantes cuyo promedio esta dentro de un rango
def buscar_por_rango_promedio(reporte, minimo, maximo):
    """Estudiantes con promedio en [minimo, maximo]."""

    iterador = 0 #Iterador para recorrer los datos
    resultado = [] #Lista para almacenar los estudiantes que cumplen

    #Bucle para recorrer el reporte
    for iterador in reporte:
        
        promedio = iterador["promedio"] #Obtiene el promedio del estudiante
        
        #Verifica que el promedio este dentro del rango
        if promedio >= minimo and promedio <= maximo:
            
            resultado.append(iterador) #Agrega el estudiante a la lista
    
    #Retorna la lista de estudiantes que cumplen la condicion
    return resultado

#Calcula el con menos valor en los datos
def calcular_minimo(datos):
    minimo = datos[0]
    for iterador in datos:
        if iterador < minimo:
            minimo = iterador
    return minimo


#Calcula el con mas valor en los datos
def calcular_maximo(datos):
    maximo = datos[0]
    for iterador in datos:
        if iterador > maximo:
            maximo = iterador
    return maximo

#Esta funcion se encarga de sumar los datos 
def calcular_suma(datos):

    suma = 0
    iterador = 0

    for iterador in datos:
        suma = suma + iterador
    
    return suma


#Esta funcion se encarga de calcular el largo del arreglo
def calcular_largo(datos):

    iterador = 0
    contador_largo = 0

    for iterador in datos:
        contador_largo = contador_largo + 1
    
    return contador_largo


#Esta funcion calcula el promedio de los datos
def calcular_promedio(datos):

    promedio = calcular_suma(datos) / calcular_largo(datos)
    
    return promedio

#Identifica al estudiante mas consistente e inconsistente
def analizar_consistencia(estudiantes):

    iterador = 0 #Iterador para recorrer los datos

    mas_consistente = None
    mas_inconsistente = None

    menor_rango = None
    mayor_rango = None

    #Bucle para recorrer los estudiantes
    for iterador in estudiantes:

        notas = iterador["notas"] #Obtiene las notas del estudiante

        minimo = calcular_minimo(notas) #Nota minima
        maximo = calcular_maximo(notas) #Nota maxima

        rango = maximo - minimo #Diferencia entre max y min

        #Primer caso (inicializar)
        if menor_rango is None or rango < menor_rango:
            menor_rango = rango
            mas_consistente = iterador

        if mayor_rango is None or rango > mayor_rango:
            mayor_rango = rango
            mas_inconsistente = iterador

    return mas_consistente, mas_inconsistente

#Imprime el reporte en formato tabla
def imprimir_tabla(estudiantes):

    print("Nombre       Promedio   Min   Max   Rango")
    print("------------------------------------------------")

    iterador = 0

    for iterador in estudiantes:

        nombre = iterador["nombre"]
        notas = iterador["notas"]

        promedio = calcular_promedio(notas)
        minimo = calcular_minimo(notas)
        maximo = calcular_maximo(notas)

        rango = maximo - minimo

        print(nombre, "   ", round(promedio,2), "   ", minimo, "   ", maximo, "   ", rango)

reporte = generar_reporte(estudiantes)
#Prueba para generar el reporte
print("=== Reporte completo ===")
for fila in reporte:
    print(fila)

print("\n=== Conteo por rendimiento ===")
print(contar_por_estado(reporte))

print("\n=== Estudiantes destacados ===")
for fila in filtrar_por_estado(reporte, "Destacado"):
    print(fila)

print("\n=== Reporte ordenado por promedio ===")
for fila in ordenar_reporte(reporte):
    print(fila)


busqueda = buscar_estudiante(estudiantes,"ana")
print(busqueda)

busqueda_rango = buscar_por_rango_promedio(reporte,5.0, 6.0)
print("Estudiantes con promedio: ",busqueda_rango)


imprimir_tabla(estudiantes)

consistente, inconsistente = analizar_consistencia(estudiantes)

print("\nMas consistente:", consistente["nombre"])
print("Mas inconsistente:", inconsistente["nombre"])
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

#Calcula el promedio del estudiante                        
def promedio_estudiante(estudiantes):
    #Retorna el promedio. La suma de las notas, divididas la cantidad de notas de los estudiantes                            
    return sum(estudiantes["notas"]) / len(estudiantes["notas"])


#Lo clasifica dentro de las categorías dependiendo su promedio
def clasificar_rendimiento(promedio):
    """Retorna: Reprobado (<4.0), Suficiente (4.0-4.9),
    Aprobado (5.0-5.9), Destacado (>=6.0)."""
    if promedio < 4.0:
        return "Reprobado"
    elif promedio < 5.0:
        return "Suficiente"
    elif promedio < 6.0:
        return "Aprobado"
    else:
        return "Destacado"
 

#Genera un reporte de los datos del alumno
def generar_reporte(lista_estudiantes):
    """Retorna lista de dicts: nombre, promedio, estado, nota_max, nota_min, rango."""
    reporte = []
    for estudiante in lista_estudiantes:
        promedio = promedio_estudiante(estudiante)
        estado = clasificar_rendimiento(promedio)
        nota_max = calcular_maximo(estudiante["notas"])
        nota_min = calcular_minimo(estudiante["notas"])
        rango = nota_max - nota_min
 
        reporte.append({
            "nombre": estudiante["nombre"],
            "promedio": round(promedio, 2),
            "estado": estado,
            "nota_max": nota_max,
            "nota_min": nota_min,
            "rango": round(rango, 2)
        })
    return reporte

#Cuenta cuantos de cada, dependiendo de su estado
def contar_por_estado(reporte):
    """Dict con cantidad por estado."""
    conteo = {}
    for estudiante in reporte:
        estado = estudiante["estado"]
        if estado in conteo:
            conteo[estado] += 1
        else:
            conteo[estado] = 1
    return conteo
 
 
def filtrar_por_estado(reporte, estado):
    """Lista de estudiantes con el estado dado."""
    resultado = []
    for estudiante in reporte:
        if estudiante["estado"] == estado:
            resultado.append(estudiante)
    return resultado
    
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
    iterador = 0 
    resultado = [] #Lista para almacenar los estudiantes que cumplen
    #Bucle para recorrer el reporte
    for iterador in reporte:
        promedio = iterador["promedio"] 
        #Verifica que el promedio este dentro del rango
        if promedio >= minimo and promedio <= maximo:
            resultado.append(iterador) #Agrega el estudiante a la lista
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

        promedio = promedio_estudiante(notas)
        minimo = calcular_minimo(notas)
        maximo = calcular_maximo(notas)

        rango = maximo - minimo

        print(nombre, "   ", round(promedio,2), "   ", minimo, "   ", maximo, "   ", rango)

# 2a) Reporte de rendimiento
reporte = generar_reporte(estudiantes)
 
print("\n--- REPORTE COMPLETO (TABLA) ---")
imprimir_tabla(reporte)
 
# 2b) Conteo y filtrado
print("\n--- CONTEO POR ESTADO ---")
conteo = contar_por_estado(reporte)
for estado, cantidad in conteo.items():
    print(f"  {estado}: {cantidad}")
 
print("\n--- FILTRAR POR ESTADO: Destacado ---")
destacados = filtrar_por_estado(reporte, "Destacado")
for r in destacados:
    print(f"  {r['nombre']}: {r['promedio']}")
 
# 2c) Ordenamiento
print("\n--- REPORTE ORDENADO POR PROMEDIO (descendente) ---")
ordenado = ordenar_reporte(reporte)
for r in ordenado:
    print(f"  {r['nombre']}: {r['promedio']}")
 
# 2d) Búsqueda
print("\n--- BUSCAR ESTUDIANTE: 'ana' ---")
encontrado = buscar_estudiante(estudiantes, "ana")
print(f"  {encontrado}")
 
print("\n--- BUSCAR POR RANGO DE PROMEDIO (5.0 a 6.0) ---")
en_rango = buscar_por_rango_promedio(reporte, 5.0, 6.0)
for r in en_rango:
    print(f"  {r['nombre']}: {r['promedio']}")
 
# 2e) Consistencia
print("\n--- CONSISTENCIA ---")
consistente, inconsistente = analizar_consistencia(estudiantes)
print(f"  Mas consistente:   {consistente['nombre']}")
print(f"  Mas inconsistente: {inconsistente['nombre']}")


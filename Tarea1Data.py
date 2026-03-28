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
    for estudiante in estudiantes: 
        if estudiante["nombre"].lower() == nombre.lower():
            return estudiante
    return none

def buscar_por_rango_promedio(reporte, minimo, maximo):
    resultados = []
    for estudiante in reporte:
        if minimo <= estudiante["promedio"] <= maximo:
            resultados.append(estudiante)
    return resultados
    
def analizar_consistencia(reporte):
    mas_consistente = None
    mas_inconsistente = None

    for est in reporte:
        if mas_consistente is None or est["rango_notas"] < mas_consistente["rango_notas"]:
            mas_consistente = est

        if mas_inconsistente is None or est["rango_notas"] > mas_inconsistente["rango_notas"]:
            mas_inconsistente = est

    print("\n=== ANÁLISIS DE CONSISTENCIA ===")
    print(f"Más consistente: {mas_consistente['nombre']} (rango: {mas_consistente['rango_notas']})")
    print(f"Más inconsistente: {mas_inconsistente['nombre']} (rango: {mas_inconsistente['rango_notas']})")

    print("\n=== REPORTE COMPLETO ===")
    print(f"{'Nombre':<12} {'Prom':<6} {'Estado':<12} {'Max':<5} {'Min':<5} {'Rango':<6}")
    print("-" * 55)

    for est in reporte:
        print(f"{est['nombre']:<12} {est['promedio']:<6.2f} {est['rendimiento']:<12} "
              f"{est['nota_maxima']:<5} {est['nota_minima']:<5} {est['rango_notas']:<6.2f}")


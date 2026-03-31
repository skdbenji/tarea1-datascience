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
    return sum(estudiantes["notas"]) / len(estudiantes["notas"])
#Lo clasifica dentro de las categorías dependiendo su promedio
def clasificar_rendimiento(estudiantes):
    prom = promedio_estudiante(estudiantes)
    if prom<4.0:
        return "Reprueba"
    elif prom>=4.0 and prom<5.0:
        return "Suficiente"
    elif prom>=5.0 and prom<6.0:
        return "Aprobado"
    else:
        return "Destacado"
#Genera un reporte de los datos del alumno
def generar_reporte(lista_estudiantes):
    reporte_estudiantes=[]
    for estudiante in lista_estudiantes:
        promedioes=promedio_estudiante(estudiante)
        rendimiento=clasificar_rendimiento(estudiante)
        nota_max=max(estudiante["notas"])
        nota_min=min(estudiante["notas"])
        rango_notas=nota_max - nota_min

        reporte_estudiantes.append({
            "nombre": estudiante["nombre"],
            "promedio": promedioes,
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

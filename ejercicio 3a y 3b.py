def aplanar_notas(estudiantes):
    #aplanar notas
    todas_las_notas = []
    
    for estudiante in estudiantes:
        todas_las_notas.extend(estudiante["notas"])
    
    return todas_las_notas


def contar_frecuencias(datos):
    #contar notas y hacer el diccionario
    conteo_de_notas = {}
    
    for nota in notas:
        if nota in conteo_de_notas:
            conteo_de_notas[nota] += 1
        else:
            conteo_de_notas[nota] = 1
    
    return conteo_de_notas


def encontrar_moda(frecuencias):
    #encontrar y contatar la nota que mas se repite 
    nota_mas_comun = None
    apariciones_maximas = 0
    
    for nota, apariciones in conteo_de_notas.items():
        if apariciones > apariciones_maximas:
            apariciones_maximas = apariciones
            nota_mas_comun = nota
    
    return nota_mas_comun, apariciones_maximas



def generar_histograma(frecuencias, ancho_max=25):
    """Imprime un histograma horizontal"""
    
    # Encontrar la frecuencia máxima para escalar
    frecuencia_maxima = 0
    for valor in frecuencias:
        if frecuencias[valor] > frecuencia_maxima:
            frecuencia_maxima = frecuencias[valor]
    
    # Dibujar el histograma
    for valor in frecuencias:
        frecuencia = frecuencias[valor]
        
        # Calcular el largo proporcional de la barra
        largo_barra = int((frecuencia / frecuencia_maxima) * ancho_max)
        barra = "." * largo_barra
        
        print(f"{valor} | {barra} ({frecuencia})")
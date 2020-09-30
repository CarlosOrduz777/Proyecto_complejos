#Libreria de espacios vectoriales complejos
#Autor: Carlos Javier Orduz Trujillo
from math import sqrt


def suma_vectores_complejos(vector_1,vector_2):
    """Esta funcion recibe dos vectores de igual tamaño con numeros complejos,
    y los suma"""
    if len(vector_1) == len(vector_2):
        for i in range(len(vector_1)):
            vector_1[i] = vector_1[i] + vector_2[i]

    else:
        raise "El tamaño de los vectores deben ser iguales"
    return vector_1

def inverso_aditivo_vector_complejo(vector):
    """Esta funcion entrega el inverso aditivo de un vector Complejo"""
    for i in range(len(vector)):
        vector[i] = vector[i] * -1
    return vector
def multiplicacion_escalar_vector(complejo, vector):
    """Esta funcion recibe un escalar(numero Complejo) y un vector de numeros complejos
    y devuelve su multiplicacion escalar"""
    for i in range(len(vector)):
        vector[i] = vector[i] * complejo
    return vector
def adicion_matrices_complejas(matriz_1,matriz_2):
    """Funcion que dadas dos matrices de numeros complejos realiza su adicion"""
    if len(matriz_1)==len(matriz_2):
        for i in range(len(matriz_1)):
           matriz_1[i] = suma_vectores_complejos(matriz_1[i],matriz_2[i])
    else:
        raise "Las matrices deben ser del mismo tamaño"
    return matriz_1
def inverso_aditivo_matriz_compleja(matriz):
    """Esta funcion recibe una matriz compleja y devuelve su inverso aditivo"""
    for i in range(len(matriz)):
        matriz[i] = inverso_aditivo_vector_complejo(matriz[i])
    return matriz
    
def multiplicacion_escalar_matriz_compleja(complejo, matriz):
    """funcion que recibe un escalar y una matriz compleja y realiza la
    multiplicacion escalar"""
    for i in range(len(matriz)):
        matriz[i] = multiplicacion_escalar_vector(complejo,matriz[i])
    return matriz
def transpuesta_matriz_compleja(matriz):
    """Funcion que recibe una matriz compleja y devuelve su transpuesta"""
    transpuesta = []
    for i in range(len(matriz[0])):
        fila = []
        for j in range(len(matriz)):
            fila.append(matriz[j][i])
        transpuesta.append(fila)
    return transpuesta
def conjugada_matriz_compleja(matriz):
    """Funcion que recibe una matriz compleja y retorna su conjugada"""
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j]=matriz[i][j].conjugate()
    return matriz
def adjunta_matriz_compleja(matriz):
    """Funcion que recibe una matriz compleja y retorna su adjunta"""
    return conjugada_matriz_compleja(transpuesta_matriz_compleja(matriz))
def producto_matrices_complejas(matriz_1,matriz_2):
    """Funcion que recibe dos matrices complejas validas y retorna su producto"""
    print(len(matriz_1[0]),len(matriz_2))
    if len(matriz_1[0]) == len(matriz_2):
        resultado = [0] * len(matriz_1)
        for i in range(len(matriz_1)):
            resultado[i] = [0] * len(matriz_2[0])
        for i in range(len(matriz_1)):
            for j in range(len(matriz_2[0])):
                for k in range(len(matriz_2)):
                    resultado[i][j] += matriz_1[i][k] * matriz_2[k][j]
        return resultado
    else:
        raise "Operacion no permitida"
def accion_matriz_vector(matriz,vector):
    """Funcion que recibe una matriz compleja y un vector complejo
    y calcula la accion de la matriz sobre el vector"""
    if len(matriz[0]) == len(matriz) == len(vector):
        vector_resultante = []
        suma = 0
        for i in range(len(matriz)):
            for j in range(len(vector)):
                suma += vector[j][0]*matriz[i][j]
            vector_resultante.append(suma)
            suma = 0
        return vector_resultante
    else: raise "Operacion invalida"
def producto_interno_vectores(vectorA,vectorB):
    """Funcion que dados dos vectores complejos calcula su producto interno"""
    return producto_matrices_complejas(adjunta_matriz_compleja([vectorA]),transpuesta_matriz_compleja([vectorB]))[0]

def norma_vector(vector):
    """Funcion que dado un vector complejo calcula su norma"""
    return math.sqrt(producto_interno_vectores(vector,vector))
    

def distancia_vectores(vector_a,vector_b):
    """Funcion que dados dos vectores complejos calcula la distancia entre ellos"""
    return norma_vector(max(vector_a,vector_b)) - norma_vector(min(vector_a,vector_b))
def es_unitaria(matriz):
    """Funcion que retorna True si la matriz es unitaria, False en caso contrario"""
    if len(matriz) != len(matriz[0]): raise "Operacion Indefinida"
    identidad = matriz_identidad(len(matriz))
    return producto_matrices_complejas(matriz,adjunta_matriz_compleja(matriz)) == producto_matrices_complejas(adjunta_matriz_compleja(matriz),matriz) == identidad

def matriz_identidad(n):
    """Funcion que genera la matriz identidad de tamaño n * m"""
    identity = [[(0.0 )for j in range(n)] for i in range(n)]
    for i in range(n):
        identity[i][i] = 1.0
    return identity
        
def es_hermitiana(matriz):
    """Funcion que dada una matriz compleja, retorn True si lo es, False en caso contrario"""
    if len(matriz) != len(matriz[0]): raise "Operacion indefinida"
    return True if matriz == adjunta_matriz_compleja(matriz) else False
def producto_tensor(matriz_a,matriz_b):
    """Funcion que retorna el producto tensor de dos matrices complejas"""
    a,a_prima = len(mastriz_a),len(matriz_b[0])
    b,b_prima = len(matriz_b), len(matriz_b[0])
    producto_tensor =[[(0.0) for j in range(a_prima*b_prima)]for i in range(a*b)]
    for i in range(len(producto_tensor)):
        for j in range(len(producto_tensor[0])):
            try:
                producto_tensor[i][j] = matriz_a[i//b][j//a] * matriz_b[i%b][j%a]

            except IndexError:
                next
    return producto_tensor

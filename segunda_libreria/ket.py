import libreria_complejos_version_2 as lb
import math
def probabilidad(vector_estado,posicion):
    tamaño = 0
    for i in range(len(vector_estado)):
       tamaño = tamaño + modulo_complejo(vector_estado[i])
    tamaño = math.sqrt(tamaño)
    return (math.sqrt(modulo_complejo(vector_estado[posicion]))**2)/(tamaño**2)




def modulo_complejo(complejo):
    return complejo.real**2 + complejo.imag**2


def main():
    vector_estado = [[0],[1],[0],[0],[0],[0],[0],[0],[0],[0]]
    phi = [[1],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
    posicion = 7
    print(amplitud_transicion(vector_estado,phi))
def encontrar_mayor(vector_estado):
    mayor = {}
    mayores = 0
    for i in range(len(vector_estado)):
        calcula =probabilidad(vector_estado,i)
        if calcula >= mayores:
            mayores = calcula
            mayor[i] = mayores
    return mayor
            
def encontrar_menor(vector_estado):
    menor = {}
    menores = math.inf
    for i in range(len(vector_estado)):
        calcula = probabilidad(vector_estado,i)
        if calcula <= menores:
            menores = calcula
            menor[i] = menores
    return menor
def normalizar_vector(vector):
    resultado = []
    longitud = longitud_vector(vector)
    for i in range(len(vector)):
        resultado += [[vector[i][0]/longitud]]
    return resultado



def longitud_vector(vector_estado):
    tamaño = 0
    for i in range(len(vector_estado)):
       tamaño = tamaño + modulo_complejo(vector_estado[i][0])
    tamaño = math.sqrt(tamaño)
    return tamaño
def bra(vector):
    return lb.adjunta_matriz_compleja(vector)
def amplitud_transicion(vector_1,vector_2):
    print(vector_1,vector_2,"hola")
    return lb.producto_interno_vectores(vector_2,vector_1)
    

import libreria_complejos_version_2 as lb
import matplotlib.pyplot as plt

import math
def dinamica(matriz,vector_estado,clicks):
    print(len(matriz[0]),len(matriz),len(vector_estado))
    for i in range(clicks):
        vector_estado = lb.accion_matriz_vector(matriz,vector_estado)
    return vector_estado


def dinamica_doble_sistema(matriz_1,vector_1,matriz_2,vector_2,clicks):
    return dinamica(lb.producto_tensor(matriz_1,matriz_2),lb.producto_tensor(vector_1,vector_2),clicks)

def doble_rendija_probabilistico(matriz):
    vector = [([0])for i in range(len(matriz))]
    vector[0] = [1]
    matriz_resultado = lb.producto_matrices_complejas(matriz,matriz)
    vector_final = lb.accion_matriz_vector(matriz_resultado,vector)
    return matriz_resultado, vector_final
def doble_rendija_cuantico(matriz):
    copia_matriz = [[(matriz[i][j])for j in range(len(matriz[0]))]for i in range(len(matriz))]
    return copia_matriz


def modulo_complejo(numero_complejo):
    return abs(numero_complejo)
def graficar_probabilidades(arreglo):
    tick_label = [("estado("+str(i)+")")for i in range(len(arreglo))]
    left = [(i+1)for i in range(len(arreglo))]
    height = [(arreglo[i][0])for i in range(len(arreglo))]
    plt.bar(left,height,tick_label = tick_label,width=0.8,color = ["red","green"])
    #name x-axis
    plt.xlabel("Estados")
    #name y-axis
    plt.ylabel("Probabilidad")
    plt.show()
    
    
    
        
def main():
    matriz_1 = [[0,1/6,5/6],[1/3,0.5,1/6],[2/3,1/3,0]]
    matriz_2 = [[1/3,2/3],[2/3,1/3]]
    vector_1 = [[0.01],[0.9],[0.09]]
    vector_2 = [[0.05],[0.95]]
    #print(dinamica2(matriz_1,vector_1,matriz_2,vector_2,2))
    #print(lb.producto_tensor(vector_1,vector_2)[2][0])

    matriz = [[0,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],[1/2,0,0,0,0,0,0,0],[0,1/3,0,1,0,0,0,0],[0,1/3,0,0,1,0,0,0],[0,1/3,1/3,0,0,1,0,0],[0,0,1/3,0,0,0,1,0],[0,0,1/3,0,0,0,0,1]]
    matriz_resultado,vector_final = doble_rendija_cuantico(matriz)
    print(matriz_resultado)
    print()
    print(vector_final)
    
        

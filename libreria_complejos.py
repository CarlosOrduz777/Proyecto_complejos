#Libreria de Numeros Complejos
#Fecha: 4/08/2020
#Autor: Carlos Javier Orduz Trujillo

import math


def sumar_complejos(c1, c2):
    """Funcion que toma dos numeros complejos(como vectores) y retorna su suma
    ( list, list )---> list"""
    return [c1[0] + c2[0], c1[1] + c2[1]]
def producto_complejos(c1, c2):
    """Funcion que toma dos numeros complejos(como vectores) y retorna su producto
    ( list, list )---->list"""
    return [c1[0]*c2[0] - c1[1]*c2[1], c1[0]*c2[1] + c2[0]*c1[1]]
def resta_complejos(c1, c2):
    """Funcion que toma dos numeros complejos (como vectores) y retorna su resta
    ( list, list )---->list"""
    return [c1[0]-c2[0], c1[1]-c2[1]]
def division_complejos(c1, c2):
    """Funcion que toma dos numeroa complejos(como vectores) y retorna su division
    ( list, list )--->list"""
    try:
        return [(c1[0]*c2[0] + c1[1]*c2[1])/c2[0]**2 + c2[1]**2,(c2[0]*c1[1]-c1[0]*c2[1])/c2[0]**2 + c2[1]**2]
        
    except ZeroDivisionError:
        print("No puedes dividir por cero")
def modulo_complejo(c):
    """Funcion que toma un numero complejo(como un vector) y retorna su modulo o tamaño
    redondeado a 4 cifras
    ( list )--->float"""
    return round((c[0]**2 + c[1]**2)**0.5,4)
def conjugado(c):
    """Funcion que toma un numero complejo(como un vector) y retorna el conjugado del complejo
    ( list )--->list"""
    return [c[0], -c[1]]
def cartesiano_a_polar(c):
    """Funcion que toma un numero complejo(como vector) en representacion cartesiana
    y retorna la representacion polar y redondea su angulo a 4 cifras
    ( list )---->list"""
    return [modulo_complejo(c), round(math.atan2(c[1],c[0]),4)]
def polar_a_cartesiano(c):
    """Funcion que toma un numero complejo(como vector) en representacion polar
    y retorna la representacion cartesiana"""
    return [c[0]*math.cos(c[1]),c[0]*math.sin(c[1])]
    
    

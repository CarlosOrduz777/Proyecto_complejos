#Libreria de Numeros Complejos
#Fecha: 4/08/2020
#Autor: Carlos Javier Orduz Trujillo

from math import pi,atan,atan2,sin,cos,sqrt


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
        a_1=c1[0]
        b_1=c1[1]
        a_2=c2[0]
        b_2=c2[1]
        return [(a_1*a_2 + b_1*b_2)/(a_2**2 + b_2**2),(a_2*b_1 - a_1*b_2)/(a_2**2 + b_2**2)]
        
    except ZeroDivisionError:
        print("No puedes dividir por cero")
def modulo_complejo(c):
    """Funcion que toma un numero complejo(como un vector) y retorna su modulo o tamaño
    redondeado a 4 cifras
    ( list )--->float"""
    return round(sqrt((c[0]**2 + c[1]**2)),4)
def conjugado(c):
    """Funcion que toma un numero complejo(como un vector) y retorna el conjugado del complejo
    ( list )--->list"""
    return [c[0], -c[1]]
def cartesiano_a_polar(c):
    """Funcion que toma un numero complejo(como vector) en representacion cartesiana
    y retorna la representacion polar y redondea su angulo a 4 cifras
    ( list )---->list"""
    return [modulo_complejo(c), round(atan2(c[1],c[0]),4)]
def polar_a_cartesiano(c):
    """Funcion que toma un numero complejo(como vector) en representacion polar
    y retorna la representacion cartesiana aproximada"""
    return [c[0]*cos(c[1]),c[0]*sin(c[1])]

def fase_complejo(c):
    """Funcion que retorna la fase de un numero complejo, debe estar en
    representacion cartesiana"""
    return round(atan2(c[1],c[0]), 4)
    

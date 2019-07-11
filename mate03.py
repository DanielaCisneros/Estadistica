import numpy as np

datosIngresados = [88, 80, 76, 72, 68, 56]

datosOrdenados = []
repetido = []
unico = []

def ordenar():
   
    comparador = 0
    for element in datosIngresados:
        if element >= comparador:
            comparador = element
            datosOrdenados.append(element)
        else:
            datosOrdenados.insert(indice(element)-1, element) 
    return (datosOrdenados)                

def indice(elemento1):
    contador=0
    for dato in datosOrdenados: 
        contador = contador+1
        if elemento1 <= dato:  
            return (contador)

for dato in ordenar():
    dato

def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma

def mediana(Informacion):
    indice = len(Informacion)/2

    if(len(Informacion) % 2 == 0):
        resultado = (Informacion[int(indice - 1)] + Informacion[int(indice)])
        return resultado/2
    else:
        return Informacion[int(indice)]

print("Mediana = ",mediana(datosOrdenados))
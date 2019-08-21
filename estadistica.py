#estadistica completa
#libreria solo para tallos y hoja 
#graficos sin librerias

import numpy as np
import math

#variables
datosIngresados = []
cuartiles = []

#ingreso de datos
DatosTotales =int(input("Ingrese el numero de la cantidad de datos, nota: debe ser mayor a 3 datos: "))
for elemento in range(0,DatosTotales):
    dato =float(input("Ingrese el dato: "))
    datosIngresados.append(dato)

#metodo frecuencia total
def frecuenciasTotal(datos):
    total = len(datos)
    return total

#metodo amplitud 
def amplitud(datos, intervalo):
    rango = max(datos) - min(datos)
    amplitud = rango // intervalo
    return amplitud

#metodo intervalo
def intervalo(datos):
    intervalo = math.sqrt(len(datos))
    return round(intervalo)

#metodo cuartil
def hallarCuartil(datos, array):
    if(len(datos)>=4):
        for i in 1,2,3:
            cuartil = (i*len(datos))/4
            i = i+1
            array.append(datos[int(cuartil)])
        return array


#metodo media 
def hallarMedia(datos):
    total = 0
    for i in datos:
        total += i 
    return('media',total/len(datos))            


#metodo mediana
def mediana(l):
    if len(l) % 2 == 0:                                                                      
        n = len(l)                                                                           
        mediana = (l[n//2-1]+ l[n//2] )/2                                                      
    else:                                                                                    
        mediana =l[len(l)//2]                                                                 
                                                                                         
    return ('mediana:',mediana)

#moda metodo
def hallarModa(datos):
    repeticiones = 0

    for i in datos:
        n = datos.count(i)
        if n > repeticiones:
            repeticiones = n

    moda = [] #Arreglo donde se guardara el o los valores de mayor frecuencia 

    for i in datos:
        n = datos.count(i) # Devuelve el número de veces que x aparece enla lista.
        if n == repeticiones and i not in moda:
            moda.append(i)

    if len(moda) != len(datos):
        return ('Moda: ', moda)
    else:
        return ('No hay moda')

#ordenba datos 
def ordenamientoBurbuja(datosIngresados):
    for numPasada in range(len(datosIngresados)-1,0,-1):
        for i in range(numPasada):
            if datosIngresados[i]>datosIngresados[i+1]:
                temp = datosIngresados[i]
                datosIngresados[i] = datosIngresados[i+1]
                datosIngresados[i+1] = temp


#metodo tallos y hojas
def tallosHojas(d):
    l,t=np.sort(d),10
    O=range(int(l[0]-l[0]%t),int(l[-1]+11),t)
    I=np.searchsorted(l,O)
    for e,a,f in zip(I,I[1:],O): 
        print('%3d|'%(f/t),*(l[e:a]-f))


#histograma
def histograma(datos):
    x = (len(datosIngresados)*int(5))
    y = (len(datosIngresados)*int(5))

    for p in range(10):
        for i in range(len(datosIngresados)):
            for j in range(2):
                print("* ", end="")
            for j in range(7):
                print(" ", end="")
        print()
    
    for i in range(int(x)-10):
        print("-- ", end="")


#imprime datos ordenados                
ordenamientoBurbuja(datosIngresados)
print("ordenar",datosIngresados)
#imprime moda
print(hallarModa(datosIngresados))
#imprime mediana
print(mediana(datosIngresados))
#imprime cuartil
for i in hallarCuartil(datosIngresados,cuartiles):
    print('cuartil',i)
#imprime media
print(hallarMedia(datosIngresados))
#imprime intervalos
print('intervalos de',intervalo(datosIngresados))
#imprime amplitud
print('amplitud',amplitud(datosIngresados, intervalo(datosIngresados)))
#imprime frecuencia total
print('frecuencia total',frecuenciasTotal(datosIngresados))
#dibujar tallos y hojas
tallosHojas(datosIngresados)
#dibujar histograma
histograma(datosIngresados)

#diagrama de bigotes
print('        |') 
print('        |') 
print('        |') 
print( '-','-','-','-','-','-','-','-','-')
print('|','      |        |') 
print('|','      |        |') 
print('|','      |        |') 
print( '-','-','-','-',hallarCuartil(datosIngresados,cuartiles)[0],'-','-','-','-')
print('|','      |        |') 
print('|','      |        |') 
print('|','      |        |')  
print('|','      |        |') 
print('|','      |        |')  
print( '-','-','-','-',hallarCuartil(datosIngresados,cuartiles)[1],'-','-','-','-')
print('|','      |        |') 
print('|','      |        |') 
print('|','      |        |') 
print('|','      |        |') 
print('|','      |        |') 
print('|','      |        |') 
print( '-','-','-','-',hallarCuartil(datosIngresados,cuartiles)[2],'-','-','-','-')
print('|','      |        |') 
print('|','      |        |') 
print('|','      |        |')  
print( '-','-','-','-','-','-','-','-','-')
print('        |') 
print('        |') 
print('        |')
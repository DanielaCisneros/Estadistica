import numpy as np
import matplotlib.pyplot as plt

datosIngresados = []
datosOrdenados = []
repetido = []
unico = []

DatosTotales =int(input("Dígame la cantidad de datos: "))
for elemento in range(0,DatosTotales):
    dato =float(input("Ingrese el dato: "))
    datosIngresados.append(dato)

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

def mediana(Informacion):
    laSuma = 0
    for i in Informacion:
        laSuma = laSuma + i
    return laSuma

def moda(Informacion):
    for x in Informacion:
	    if x not in unico:
		    unico.append(x)
	    else:
		    if x not in repetido:
			    repetido.append(x)
    return repetido

def media(Informacion):
    indice = len(Informacion)
    if (indice % 2 == 0):
        resultado = (datosOrdenados[int(indice/2)] + datosOrdenados[int(indice/2)]+1)/2
        return resultado
    else:
        resultado = datosOrdenados[int(indice/2)]
        return resultado

def tallos(d):
    l,t=np.sort(d),10
    O=range(int(l[0]-l[0]%t),int(l[-1]+11),t)
    I=np.searchsorted(l,O)
    for e,a,f in zip(I,I[1:],O): 
        print('%3d|'%(f/t),*(l[e:a]-f))

tallos(datosOrdenados)        

print(datosOrdenados)
print("Mediana = ",mediana(datosOrdenados)/len(datosOrdenados))
print("Moda = ",moda(datosOrdenados))
print("Media = ",media(datosOrdenados))


plt.hist(datosOrdenados, bins=7)
plt.xlabel("Tendencia")
plt.ylabel("Frecuencia")
plt.title("Estadistia")
plt.show()

plt.boxplot(datosOrdenados)
plt.xlabel("Tendencia")
plt.ylabel("Frecuencia")
plt.title("Estadistia")

plt.show()





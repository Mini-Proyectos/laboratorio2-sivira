# TestBusquedas.py
# Este es un archivo de prueba muy sencillo, debe ser modificado 
# de acuerdo con el enunciado del laboratorio.

from Busquedas import LeerArchivo
from Busquedas import BusquedaLineal
from Busquedas import BusquedaBinaria
from Busquedas import InsertionSort

##Cargando el archivo
archivo = LeerArchivo('Archivo')

##Elemento a buscar
objetivo = 25

##Ejecutando la busqueda por busqueda lineal
resultadoLineal= BusquedaLineal(archivo, objetivo)

if resultadoLineal != None:
	print("Está en la posición: " + str(resultadoLineal)) 

##Ejecutando la busqueda por busqueda binaria de un arreglo no ordenado
resultadoBinario= BusquedaBinaria(archivo, objetivo)

if resultadoBinario != None:
	print("Está en la posición: " + str(resultadoBinario))

##Ejecutando la busqueda por busqueda binaria de un arreglo ordenado
resultadoBinario2= BusquedaBinaria(OrdenarInsert(archivo), objetivo)

if resultadoBinario2 != None:
	print("Está en la posición: " + str(resultadoBinario2))

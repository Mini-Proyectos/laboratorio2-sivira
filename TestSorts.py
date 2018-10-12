#Importamos las librerias y metodos necesarios
import sys
import random
import time

from Sorts import MergeSort
from Busquedas import InsertionSort

#Capturando las entradas del script
nombre = str(sys.argv[1])
cantidad = int(sys.argv[2])

#Generando el arreglo desordenado con elementos entre 0 y 100
A = [random.choice(range(0,101)) for i in range(0,cantidad)]

#Estableciendo el inicio y final del arreglo A
p = 0
r = len(A)-1

#Inicializando los valores de inicio, final y tiempoTotal del tiempo que tarda el algoritmo seleccionado
inicio = 0
final = 0
tiempoTotal = 0

#Verificamos que algoritmo debemos ejecutar y evaluar
#En cualquier caso, tomamos el tiempo de inicio y el tiempo de culminacion
if (nombre == 'InsertionSort'):

	inicio = time.time()
	InsertionSort(A,p,r)
	final = time.time()

elif(nombre == 'MergeSort'):

	inicio = time.time()
	MergeSort(A,p,r)
	final = time.time()

else:
	#Si el dato suministrado no es correcto, terminamos la ejecucion
	print('El algoritmo introducido no ha sido encontrado')
	sys.exit()

#Estas verificaciones se pueden hacer con try, except. Cuando se agregen man algoritmos se cambiara a la forma mencionada.


#Calculamos el tiempo que demoró el algoritmo
tiempoTotal = (final-inicio)

#Mostramos en pantalla el tiempo que le tomó al algoritmo resolver el problema
#Dependiendo del tiempo, se mostrara en segundos o milisegundos
if (tiempoTotal < 1):
	print('El algoritmo '+nombre+' Con '+str(cantidad)+' elementos demoró '+str(tiempoTotal*1000)+' milisegundos')
elif (tiempoTotal >= 1):
	print('El algoritmo '+nombre+' Con '+str(cantidad)+' elementos demoró '+str(tiempoTotal)+' segundos')


#Curioso:
#Con 1000000 MergeSort demoró 16 segundos.
#Aun sigo esperando que InsertionSort termine con el millon. Hasta ahora a demorado 30 min, apuesto a que tomará una hora o más.
#Es evidente la gran diferencia entre nlogn y n^2.


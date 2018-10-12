# Busquedas.py
# Autor: Ivette C. Martínez
# Modificado por: Carlos Sivira
# Descripcion: Implementacion de los algoritmos de busqueda lineal y BusquedaBinaria con ordenamiento por insercion

##Funcion que lee un archivo y retorna un arreglo
def LeerArchivo(archivo : str) -> [int]:
	arch = open(archivo,'r')
	arr = [int]

	for linea in arch:
		arr.append(int(linea))

	arch.close()

	return arr

##Busqueda Lineal##
def BusquedaLineal(arreglo, x):
	for i in range(len(arreglo)):
		if arreglo[i] == x:
			return i
	return None 

##Busqueda Binaria##
def BusquedaBinaria(A:[int], x:int) -> int:

	try:
		for i in range(1,len(A)):
			assert(A[i-1]<=A[i])
	except:
		print("El arreglo no esta ordenado")

	start = 0	
	end = len(A) - 1;

	while(start < end):
		mid = int((start + end) / 2)

		if (A[mid] == x) : return x

		elif (A[mid] <= x) : start = mid + 1

		else : end = mid - 1

	return start if A[start] == x else None

##Ordenamiento por inserción, ordena de forma creciente##
def InsertionSort(A:[int],p:int,r:int):
	for j in range(p+1,r+1):
		key = A[j]
		i = j-1

		while (i>=p and A[i] > key):
			A[i+1] = A[i]
			i = i-1

		A[i+1] = key
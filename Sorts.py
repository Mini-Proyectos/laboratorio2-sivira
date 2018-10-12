#Algoritmos de ordenamiento MergeSort
def MergeSort(A:[int],p:int,r:int):

	if (p < r):
		q = (p+r) // 2

		MergeSort(A,p,q)
		MergeSort(A,q+1,r)
		Merge(A,p,q,r)

#Parte combinatoria del algoritmo MergeSort
def Merge(A:[int],p:int,q:[int],r:[int]):
	n = q-p + 1
	m = r-q

	L = [0 for i in range(1,n+2)]
	R = [0 for i in range(1,m+2)]

	for i in range(1,n+1):
		L[i] = A[p+i-1] 

	for i in range(1,m+1):
		R[i] = A[q+i]

	L.append(float('inf'))
	R.append(float('inf'))

	i = 1
	j = 1

	for k in range(p,r+1):
		if (L[i] <= R[j]):
			A[k] = L[i]
			i = i+1
		else:
			A[k] = R[j]
			j = j+1
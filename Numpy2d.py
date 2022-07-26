import numpy as np

A = np.array([[11,12],[21,22],[31,32]])
#Tipo
print(type(A))
#Forma
print(A.shape)
#Tipo de dato
print(A.dtype)
print(A[1])

#Multiply
a = np.array([[11,12],[21,22]])
B = np.array([[1,0],[0,1]])
c = a * B
print(c)

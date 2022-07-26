import numpy as np
import matplotlib.pyplot as plt

#Create a list
a = [[11,12,13],[21,22,23],[31,32,33]]

A = np.array(a)
#Show the numpy array dimensions
print(A.ndim)

#Access the element on the first two rows of the 3 column as a follow
print(A[0:2,2])

#Access the element on the first row and first and second columns
print(A[0][0:2])

x = np.array([0,1,0,1,0])
z=np.array([1,0,1,0,1])
print(x*z)

a = np.array([0,1])
b = np.array([1,0])
print(np.dot(a,b))

a =np.array([1,1,1,1,1])
print(a+10)

import numpy as np

import matplotlib.pyplot as plt

y = np.array([1,2])
print(y)

#Numpy Array Multiplication
z = 2 *y
print(z)

#Create a numpy array
u = np.array([1,2])
print(u)
v = np.array([3,2])
print(v)

z = u *v
print(z)
print(np.dot(u,v))

u = np.array([1, 2, 3,-1])
print(u)
#Add the constant to array
u+1

#Create the numpy array in radians
x = np.array([0,np.pi/2, np.pi])
y = np.sin(x)
print(y)

print(np.linspace(-2 , 2, num=5))

x = np.linspace(0,2*np.pi,num=100)
y = np.sin(x)
#Plot the result
plt.plot(x,y)
plt.show()

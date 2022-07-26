import numpy as np

import matplotlib.pyplot as plt

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a,head_width=0.05,color ='r', head_length=0.1 )
    plt.text(*(a+0.1),'a')
    ax.arrow(0, 0, *b,head_width=0.05,color ='b', head_length=0.1)
    plt.text(*(b+0.1),'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)
    #plt.show()

a = np.array([1,1])
b = np.array([0, 1])
c = np.dot(a,b)
print("The dot product is:",c)
Plotvec2(a,b)

#A = '1234567'
#print(A[1::2])
#name = "Michael Jackson"
#print(name.find('el'))

#tuple1= ("A","B","C")
#print(tuple1[-1])

#A=((11,12),[21,22])
#print(A[0][1])

#print('1,2,3,4'.split(','))
a=[1,'a']
b=[2,1,'d']
#print(a+b)

v={'A','B','C'}
v.add('C')


#c=['1','2','3']
#for n in c:
 #   print(2*n)

def add(x,y):
    z=y+x
    return (y)

#print(add('1','1'))
A=[1,'a']
a={2,1,'d'}

a=A.append()
print(a.set())

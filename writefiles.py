#! /usr/bin/python

import os


exmp2 = 'C:\\Users\\danie\\Desktop\\Example1.txt'
#os.chmod(exmp2,777)
w = 'w'

Lines = ["This is line D \n", "This is line B\n", "This is line C"]

with open(exmp2, w) as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)



with open(exmp2, 'r') as test:
    print(test.read())

with open(exmp2,'a+') as test:
    print('Initial Location: {}'.format(test.tell()))

    data = test.read()
    if (not data): #empty strings return false in python
        print('Read nothing')
    else:
        print(test.read())
    
    test.seek(0,0) #move 9 bytes

    print('\nNew Location: {}'.format(test.tell()))
    data = test.read()
    if (not data):
        print('Read nothing')
    else:
        print(data)
    
    print("Location after read: {}".format(test.tell()))

    
with open(exmp2,'r') as readfile:
    with open('Example3.txt',w) as write:
        for line in readfile:
            write.write(line)


#Verify if the copy is successfully executed

with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())

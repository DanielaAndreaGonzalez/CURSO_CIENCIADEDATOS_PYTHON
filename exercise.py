#Run this prior to starting the exercise
from random import randint as rnd

memReg = 'C:\\Users\\danie\\Desktop\\members'
exReg = 'C:\\Users\\danie\\Desktop\\inactive'
fee = ('yes','no')

def genFiles(current,old):
    with open(current,'w+') as writefile:
        writefile.write('Membership no Date Joined Active \n')
        data = "{:^13} {:<11} {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015,2020))+'-' + str(rnd(1,12))+'-'+str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[rnd(0,1)]))

    with open(old,'w+') as writefile:
        writefile.write('Membership No Date Joined Active \n')
        data = '{:^13} {:<11} {:<6}\n'
        for rowno in range(3):
            date = str(rnd(2015,2020)) + '-' + str(rnd(1,12))+ '-'+ str(rnd(1,25))
            writefile.write(data.format(rnd(10000,99999),date,fee[1]))

genFiles(memReg,exReg)


def cleanFiles(currentMem,exMem):
    '''
    currentMen: file containg list of current members
    exMem: File containing list of old members

    Removes all rows from currentMem containing 'no' and appends thems to exMen 
    '''

    pass

#Code to help you see the files
#Leave as is
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)

headers = "Membership No Date joined Active \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())

with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())

def testMsg(passed):
    if passed:
        return 'test Passed'
    else:
        return 'Test Failed'

testWrite = "testWrite.txt"
testAppend = "testAppend.txt"
passed = True

genFiles(testWrite,testAppend)

with open(testWrite,'r') as file:
    ogAppend = file.readlines()

with open(testAppend,'r') as file:
    ogAppend = file.readlines()

try:
    cleanFiles(testWrite,testAppend)
except:
    print('Error')


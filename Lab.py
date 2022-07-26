#import urllib.request
#url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
url = 'C:\\Users\\danie\\Desktop\\Example1.txt'
filename = 'Example1.txt'
#urllib.request.urlretrieve(url, filename)

#Download example file

#Read the Example1.txt
example1 = "Example1.txt"
file1 = open(example1, 'r')

file1.name
file1.mode

fileContent = file1.read()
print(fileContent)

#with open(example1, "r") as file1:
 
 #   fileContent = file1.read()
  #  print(fileContent)

#Read certain amount of characters

#with open(example1,"r") as file1:
 #   print(file1.read(4))
  #  print(file1.read(4))
   # print(file1.read(7))
    #print(file1.read(15))

#Read one line
#with open(example1,"r") as file1:
 #   print("first line: " + file1.readline())

#We can use a loop to iterate 
#Iterate through the lines

'''with open(example1, "r") as file1:
    i = 0;
    for line in file1:
        print("Iteration", str(i), ": ", line)
        i = i+1
'''
#We can use the method readlines() to save the text file to a list

#REad all lines and save as a list

'''with open(example1,"r") as file1:
    FileasList = file1.readlines()

FileasList[0]'''

import requests 
import os 
from PIL import Image
from IPython.display import IFrame

url = 'https://www.ibm.com/'
r=requests.get(url)

r.status_code

print(r.request.headers)
print("request body: ",r.request.body)

#You can view the HTTP response header using the attributes headers. This returns 
#a python dictionary of HTTP response headers

header = r.headers
print('+++++\n',r.headers)

print(header['Date'])


print(header['Content-Type'])
print(r.encoding)

print(r.text[0:100])

url='https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png'
r = requests.get(url)
print(r.headers)

print(r.headers['Content-Type'])

path= os.path.join(os.getcwd(),'image.png')
print(path)

with open(path,'wb') as f:
    f.write(r.content)

Image.open(path)

#REPASO
#wget: comando para obtener contenido de la web

#Nos dan url
#url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
#path=os.path.join(os.getcwd(),'example.txt)
#r=requests.get(url)
#with open(path,'wb') as f:
#f.write(r.content)


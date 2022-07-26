import pandas as pd

#Read data from csv file

csv_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.csv'

df = pd.read_csv(csv_path)

#print first five rows of the dataframe
print(df.head())

#Read data from Excel File and print the first five rows

xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

df = pd.read_excel(xlsx_path)
df.head()

#Access to the column Lenght

#x = df[['Length']]
x = df['Length']
print(x)

y = type(df[['Artist']])
print(y)

#Access to multiple colums

y = df[['Artist','Length','Genre']]
print(y)

#Access the value on the first row and the first column

print(df.iloc[0,0])
#Acces the value on the second row and the first column
print(df.iloc[1,0])
#Access the value on the first row and the third column
print("-------------",df.iloc[0,2])

#Acces the column using the name
print(df.loc[0,'Artist'])

#Acces the column using the name
print(df.loc[1,'Artist'])

#Acces the column using the name
print("***********",df.loc[0,'Released'])
print(df.loc[0,'Released'])
print(df.loc[1,'Released'])
#Slicing the dataframe
print(df.iloc[0:2,0:3])

print(df.loc[0:2,'Artist':'Released'])

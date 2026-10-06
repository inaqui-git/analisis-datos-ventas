import pandas as pd

#1. cargar los datos desde el archivo csv
df= pd.read_csv("train.csv")

#2. Mostrar las primeras 5 filas para verificar que todo se leyo bien
print("\n---Primeras 5 filas del dataset---")
print(df.head())

#3. Ver informacion basica sobre las columnas y tipos de datos
print("\n--Informacion general---")
print(df.info())

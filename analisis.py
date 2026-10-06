import pandas as pd

#1. cargar los datos desde el archivo csv
df= pd.read_csv("train.csv")

#2. Mostrar las primeras 5 filas para verificar que todo se leyo bien
print("\n---Primeras 5 filas del dataset---")
print(df.head())

#3. Ver informacion basica sobre las columnas y tipos de datos
print("\n--Informacion general---")
print(df.info())

#4. Analiza especialmente estas dos columnas para comprobar sus posibles salidas y construir un ahipotesis en base a eso
print("\n---Analizamos los tipos de respuestas que hay en las columnas Ship Mode y Segment---")
print(df["Ship Mode"].unique())
print(df["Segment"].unique())

#5. Filtrar las filas en las que Postal Code es nulo
nulos_postal = df[df['Postal Code'].isnull()]
print("=== FILAS CON CÓDIGO POSTAL NULO ===")
print(nulos_postal[['City', 'State', 'Region', 'Postal Code']])

# 6. Convertir fechas a tipo datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%d/%m/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')

# 7. Convertir a tipo categoría
df['Ship Mode'] = df['Ship Mode'].astype('category')
df['Segment'] = df['Segment'].astype('category')

print("\n=== Tipos de datos corregidos ===")
print(df.dtypes)
"""
conteo_burlington= (df["City"]== "Burlington").sum()
print(conteo_burlington)
"""
# Te devuelve solo los valores de la Columna_B donde la Columna_A es igual a tu valor
resultados = df.loc[df['City'] == 'Burlington', 'Postal Code']
print("Los resultados son %d",resultados)

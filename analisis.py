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

# 8. Buscar filas de Burlington que SÍ tengan código postal asignado
burlington_con_cp = df[(df['City'] == 'Burlington') & (df["State"]== "Vermont") & (df['Postal Code'].notnull())]

print("=== CÓDIGOS POSTALES ENCONTRADOS PARA BURLINGTON ===")
print(burlington_con_cp[['City', 'State', 'Postal Code']].drop_duplicates())

#9. Como no encontramos valores en Postal Code en la ciudad de Burlington-Vermount. Hay que buscar el codigo postal por otro lado
# Encontre que el codigo postal de la zona este de Burlington es "05401"
# Imputar el código postal 05401 para los registros de Burlington, Vermont
df['Postal Code'] = df['Postal Code'].fillna('05401')

# Verificar que ya no queden valores nulos en Postal Code
print("=== VERIFICACIÓN DE NULOS EN POSTAL CODE ===")
print(f"Cantidad de nulos restantes: {df['Postal Code'].isnull().sum()}")

####################################################

import matplotlib.pyplot as plt

# Agrupar ventas por Categoria
ventas_categoria = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

# Crear el gráfico de barras
plt.figure(figsize=(8, 5))
ventas_categoria.plot(kind='bar', color='skyblue')
plt.title('Ventas Totales por Categoría de Producto')
plt.xlabel('Categoría')
plt.ylabel('Ventas ($)')
plt.tight_layout()

# Guardar la imagen en tu proyecto
plt.savefig('ventas_por_categoria.png')
print("=== GRÁFICO GUARDADO COMO ventas_por_categoria.png ===")
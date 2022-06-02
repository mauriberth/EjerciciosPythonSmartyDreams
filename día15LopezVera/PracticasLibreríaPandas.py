#Librería Pandas
# Importamos Pandas
from ast import increment_lineno
import pandas as pd

# Creamos una serie de números y hallamos su media
numeros=pd.Series([1,2,3,5,67,35,235,62])
numeros.mean()
# Hallamos la suma de dichos números
numeros.sum()
# Creamos una SERIE de tres colores diferentes
colores = pd.Series(['rojo','amarillo','verde'])
# Visualizamos la serie creada
colores
# Creamos una serie con tipos de autos, y la visualizamos
tipos_autos = pd.Series(['sedan','SUV','Pick Up'])
# Combinamos las series de tipos de autos y colores en un DATAFRAME
tabla_autors = pd.DataFrame({'Tipo de auto':tipos_autos,"Color":colores})
# Conectamos el cuaderno actual con nuestro Drive
from google.colab import drive
drive.mount('/content/drive')
# Importar "ventas-autos.csv" y convertirlo en un nuevo DATAFRAME
ventas_autos = pd.read_csv('/content/drive/MyDrive/ColabNotebooks/ventas-autos.csv')
# Exportar el Dataframe como un archivo CSV a mi carpeta "/content/drive/MyDrive/Colab Notebooks/pruebas/"
ventas_autos.to_csv('/content/drive/MyDrive/ColabNotebooks/pruebas/estearchivo.c5v')
# Analicemos los tipos de datos disponibles en el dataset de ventas autos
ventas_autos.dtypes
# Apliquemos estadística descriptiva (cantidad de valores, media, desviación estándar, valores mínimos y máximos, cuartiles) al dataset
ventas_autos.describe()
# Obtenemos información del dataset utilizando info()
ventas_autos.info()
# Listamos los nombres de las columnas de nuestro dataset
ventas_autos.columns
# Averiguamos el "largo" de nuestro dataset
len(ventas_autos)
# Mostramos las primeras 5 filas del dataset
ventas_autos.head()
# Mostramos las primeras 7 filas del dataset
ventas_autos.head(7)
# Mostramos las últimas 5 filas del dataset
ventas_autos.tail(5)
# Utilizamos .loc para seleccionar la fila de índice 3 del DataFrame
ventas_autos.loc[3]
# Utilizamos .iloc para seleccionar las filas 3, 7 y 9
ventas_autos.iloc([3,7,9])
# Seleccionar la columna "Kilometraje"
ventas_autos['Kilometraje']
# Encontrar el valor medio de la columnas "Kilometraje"
ventas_autos['Kilometraje'].mean()
# Seleccionar aquellas columnas que tengan valores superiores a 100,000 kilómetros en la columna Kilometraje
ventas_autos[ventas_autos['Kilometraje']>10000]
# Creamos una tabla cruzada de doble entrada entre Fabricante y cantidad de puertas
pd.crosstab(ventas_autos['Fabricante'], ventas_autos["Puertas"])
# Agrupamos las columnas por fabricante y buscandos el valor medio de las columnas numéricas
ventas_autos.groupby(['Fabricante']).mean()
# Importamos Matplotlib y creamos un gráfico con los valores de la columna Kilometraje
import matplotlib as plt
%matplotlib increment_lineno
ventas_autos["Kilometraje"].plot()
# Puede que un gráfico más apropiado en este caso sea un histograma?
ventas_autos["Kilometraje"].hist()
# Elimina la puntuación de la columna de precios
ventas_autos["Precio (USD)"] = ventas_autos["Precio (USD)"].str.replace("[\, \$\.]", "")
ventas_autos["Precio (USD)"] = ventas_autos["Precio (USD)"].astype(int)/100
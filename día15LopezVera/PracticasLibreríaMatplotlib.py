#Librería Matplotlib
# Importamos el módulo de Matplotlib como plt
import matplotlib.pyplot as plt
%matplotlib inline
# Creamos un gráfico utilizando plt.plot()
plt.plot()
# Graficomos una lista de números
a = [1,5,3,8,7, 15]
plt.plot(a)
# Creamos dos listas, x e y. Llenamos a la lista x de valores del 1 al 100. 
x = list(range(101))
# Los valores de y van a equivaler al cuadrado del respectivo valor en x con el mísmo índice
y = []
for numero in x:
y.append(numero**2)
# Graficamos ambas listas creadas
plt.plot(x,y)
# Creamos el gráfico utilizando plt.subplots()
fig, ax = plt.subplots()
ax.plot(x,y)
# Importar y preparar la librería
import matplotlib.pyplot as plt
%matplotlib inline
# Preparar los datos
x = list(range(101))
y = []
for numero in x:
y.append (numero**2)
# Preparamos el área del gráfico (fig) y el gráfico en sí (ax) utilizando plt.subplots()
fig, ax = plt.subplots ()
# Añadimos los datos al gráfico
ax.plot(x,y)
# Personalizamos el gráfico añadiendo título al gráfico y a los ejes x e y
ax.set(title= "Grafico de casos de CoVID-19 en Latam", xlabel= "dias", ylabel ="casos confirmados ")
# Guardamos nuestro gráfico empleando fig.savefig()
fig.savefig("/ejemplo -grafico-covid.png")
#creamos un nuveo set de datos utilizando la librería Numpy
import numpy as np
x_1 = np.linspace(0, 108, 20)
y_1 = x_1**2
# Creamos el gráfico de dispersión de x vs y
fig, ax = plt.subplots ()
ax.scatter(x_1, y_1)
# Visualizamos ahora la función seno, utilizando np.sin(X)
fig, ax = plt.subplots ()
x_2 = np.linspace (-10, 10, 100)
y_2 = np.sin(x_2)
ax.scatter (x_2, y_2)
# Creemos un diccionario con tres platos y su respectivo precio 
# Las claves del diccionario serán los nombres de las comidas, y los valores asociados, su precio.
comidas = {"lasagna": 350, "sopa": 150, "roast beef": 650}

# Crearemos un gráfico de barras donde el eje x está formado por las claves del diccionario,y el eje y contiene los valores.
fig, ax = plt.subplots ()
ax.bar(comidas.keys(),comidas.values())

# Añadimos los títulos correspondientes
ax.set(title="Precios de comidas", xlabel="Comidas", ylabel="Precios ")
# Probemos a continuación con un gráfico de barras horizontales
fig, ax = plt.subplots ()
ax.barh(list(comidas.keys () ) , list(comidas.values ()))
ax.set(title="Precios de comidas", ylabel="Comidas", xlabel="Precios")
# Creamos una distribución de 1000 valores aleatorios distribuidos normalmente
x = np.random.randn (1000)
# Creamos el histograma
fig, ax = plt.subplots ()
ax.hist(x)
# Creamos una figura con 4 subgráficos (2 por fila)
fig, ((axi, ax2), (ax3, ax4)) = plt.subplots (nrows=2, ncols=2, figsize=(10,5))
# Creamos la misma disposición de gráficos, con un tamaño de figura de 10x5
fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots (nrows=2, ncols=2, figsize=(10, 5))
# Para nuestro primer gráfico, tomamos el conjunto x_1, y_1, y generamos un gráfico de líneas
ax1.plot(x_1, x_2)
# Para nuestro segundo gráfico, tomamos el conjunto x_2, y_2, y generamos un gráfico de dispersión
ax2.scatter(x_2, y_2)
# Creamos un gráfico con los precios de tres comidas en la esquina inferior izquierda
ax3.bar(comidas.keys (), comidas.values ())
# El gráfico de la esquina inferior derecha será un histograma de valores aleatorios con distribución normal
ax4.hist (np.random.randn(1000))
# Verificamos estilos disponibles
plt.style.available
# Cambiamos el estilo predeterminado por "seaborn-whitegrid"
plt.style.use( 'seaborn-whitegrid')
# Copiamos los valores de los gráficos anteriores
# Creamos la misma disposición de gráficos, con un tamaño de figura de 10x5
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots (nrowS-2, ncols-2, figsize=(10, 5))

# Para nuestro primer gráfico, tomamos el conjunto x_1, y_1, y generamos un gráfico de líneas
ax1.plot(x_1, y_1, color="#fcba03")

# Para nuestro segundo gráfico, tomamos el conjunto x_2, y_2, y generamos un gráfico de dispersión
ax2.scatter (x_2, y_2, color="#fcba03")

# Creamos un gráfico con los precios de tres comidas en la esquina inferior izquierda
ax3.bar(comidas.keys (), comidas. values (), color="#03c6fc")

# El gráfico de la esquina inferior derecha será un histograma de valores aleatorios con distribución normal
ax4.hist(np.random.randn (10e0), color="#fce36b")
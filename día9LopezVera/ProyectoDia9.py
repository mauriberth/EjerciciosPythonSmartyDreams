print("Programa DevOps SmartyDreams 2022");
print("@author López Vera Mauricio Alberto");

#Importaciones de librerías para el proyecto
from pathlib import Path;
import math;
import time;
import re;
import datetime;
import os;

#Creación de la función que creará la pantalla visual en consola y realizará las impresiones de datos pertinentes
def visualizar():
    i = 0;
    print('-' * 39);
    print('Nombre Archivo\t\tNúmero de Serie');
    print('--------------\t\t---------------');
    for a in archvEnc:
        print(f'{a}\t\t{numEnc[i]}');
        i += 1;
    print('\nResultados finales: ');
    print(f'Total de números encotrados: {len(numEnc)}');
    fin = time.time();
    tiempoTotal = fin - comienzo;
    print(f'Tiempo de duración de la búsqueda: {math.ceil(tiempoTotal)} segundos');
    print(f'Fecha en la que se realizó la búsqueda: {fechaActual.day}/{fechaActual.month}/{fechaActual.year}');
    print('-' * 39);

#Creación de la función que buscará el número de serie.
def busqNum(archv, patron):
    este_archv = open(archv, 'r');
    txt = este_archv.read();
    if re.search(patron, txt):
        return re.search(patron, txt);
    else:
        return '';

#Creación de la función que creará las listas.
def CListas():
    for carpet, subcarpet, archv in os.walk(ruta):
        for a in archv:
            resultado = busqNum(Path(carpet,a), patronDeBusqueda);
            if resultado != '':
                numEnc.append((resultado.group()));
                archvEnc.append(a.title());

#inicialización.
comienzo = time.time(); 
ruta = 'C:\\Users\\momo-\\Desktop\\Mi_Gran_Directorio';
patronDeBusqueda = r'N\D{3}-\d{5}';
fechaActual = datetime.date.today();
numEnc = [];
archvEnc = [];

#Llamada a las funciones.
CListas();
visualizar();
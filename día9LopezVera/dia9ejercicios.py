print("Programa DevOps SmartyDreams 2022");
print("@author López Vera Mauricio Alberto");

#Importaciones de librerías
from collections import Counter;
from collections import defaultdict;
from collections import deque;
from datetime import date;
from datetime import datetime;
import math;
import re;


print("\nPráctica Módulo Collections 1:");
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7];
contador = Counter(lista);
print(contador);

print("\nPráctica Módulo Collections 2:");
mi_diccionario = defaultdict(lambda:"Valor no hallado");
mi_diccionario["edad"] = 44;
print(mi_diccionario['Mauricio']);

print("\nPráctica Módulo Collections 3:");
lista_ciudades= deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]);
lista_ciudades.appendleft('México'); #México fue un elemento agregado por la izquierda.
print("La lista es: ",lista_ciudades);
print("El último elemento agregado por la izquierda es: ",lista_ciudades[0]);

print("\nPráctica Módulo Datetime 1:");
mi_fecha = date(1999, 2, 3)
print("La fecha ingresada es: ",mi_fecha);

print("\nPráctica Módulo Datetime 2:");
hoy = date.today();
print("La fecha del día de hoy es: ",hoy);

print("\nPráctica Módulo Datetime 3:");
minutos = datetime.now().minute;
print(f'La hora actual lleva transcurridos {minutos} minutos.');

print("\nPráctica Módulo Math 1:");
resultado = math.log10(25)
print(f'El logaritmo de base 10 del número 25 es {resultado}');

print("\nPráctica Módulo Math 2:");
resultado = math.sqrt(math.pi);
print(f'La raíz cuadrada de pi(3.1415...) es {resultado}');

print("\nPráctica Módulo Math 3:");
resultado = math.factorial(7)
print(f'El factorial del 7 es {resultado}.');

print("\nPráctica Módulo RE 1:");
def verificar_email(email):
    patron = r'@\w+\.com';
    verificar = re.search(patron,email);
    if verificar:
        print("Ok");
    else:
        print("La dirección de email es incorrecta.");
verificar_email("momo-wwe2010hotmail.com"); #dará incorrecto debido a que falta el @ en el patrón.

print("\nPráctica Módulo RE 2:");
def verificar_saludo(frase):
    patron = r'^Hola';
    verificar = re.search(patron,frase);
    if verificar:
        print("¡Hola!, gracias por el saludo.");
    else:
        print("¡Te haz olvidado de saludar!");
verificar_saludo("Hola, mi nombre es Mauricio.");

print("\nPráctica Módulo RE 3:");
def verificar_cp(cp):
    patron = r'\w{2}\d{4}';
    verificar = re.search(patron,cp);
    if verificar:
        print("El código postal que ingresaste, es correcto.");
    else:
        print("El código postal ingresado no es correcto");
verificar_cp("XX1234");
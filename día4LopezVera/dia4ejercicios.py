from random import randint;
from random import *;


print("Programa DevOps SmartyDreams 2022");
print("@author López Vera Mauricio Alberto");

print("\nPráctica Operadores de comparación 1:");
n1 = 36;
n2 = 17;
mi_bool = n1 >= n2;
print(mi_bool);

print("\nPráctica Operadores de comparación 2:");
n1 = 25**0.5;
n2 = 5;
mi_bool = n1 == n2;
print(mi_bool);

print("\nPráctica Operadores de comparación 3:");
n1 = 64*3;
n2 = 24*8; 
mi_bool = n1 != n2;
print(mi_bool);

print("\nPráctica Operadores Lógicos 1:");
n1 = 36;
n2 = 72/2;
n3 = 48;
mi_bool = n1>n2 and n1<n3;
print(mi_bool);

print("\nPráctica Operadores Lógicos 2:");
n1 = 36;
n2 = 72/2;
n3 = 48;
mi_bool = n1>n2 or n1<n3;
print(mi_bool);

print("\nPráctica Operadores Lógicos 3:");
frase="Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan";
palabral="éxito";
palabra2="tecnología";
mi_bool = palabral not in frase and palabra2 not in frase;
print(mi_bool);

print("\nPráctica Control de Flujo 1:");
n1 = input("Ingresa un número: ");
n2 = input("Ingresa otro número: ");
if n1 > n2:
    print(f"{n1} es mayor que {n2}");
elif n2 > n1:
    print(f"{n2} es mayor que {n1}");
else:
    print(f"{n1} y {n2} son iguales");


print("\nPráctica Control de Flujo 2:");
edad = 16;
tiene_licencia = False;
if edad >= 18 and tiene_licencia:
    print("Puedes conducir.");
elif edad < 18:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia.");
else:
    print("No puedes conducir. Necesitas contar con una licencia.");

print("\nPráctica Control de Flujo 3:");
habla_ingles = True;
sabe_python = False;
 
if habla_ingles and sabe_python:
    print("Cumples con los requisitos para postularte.");
elif (not habla_ingles) and (not sabe_python):
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés.");
elif not habla_ingles:
    print("Para postularte, necesitas tener conocimientos de inglés.");
else:
    print("Para postularte, necesitas saber programar en Python.");

print("\nPráctica Loop For 1:");
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"];
for alumno in alumnos_clase:
    print(f"Hola {alumno}");

print("\nPráctica Loop For 2:");
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4];
suma_numeros = 0;
for numero in lista_numeros:
    suma_numeros = suma_numeros + numero;
print("La suma de los números es: ",suma_numeros);

print("\nPráctica Loop For 3:");
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4];
suma_pares = 0;
suma_impares = 0;
for n in lista_numeros:
    if n % 2 == 0:
        suma_pares = suma_pares + n;
    else:
        suma_impares = suma_impares + n;
print(f"La suma de los números pares es {suma_pares} y la de los impares es: {suma_impares} ");

print("\nPráctica While 1:");
n = 10;
while n >= 0:
    print(n);
    n -= 1;

print("\nPráctica While 2:");
n = 50;
while n >= 0:
    if n % 5 == 0:
        print(n);
        n -= 1;
    else:
        n -= 1;

print("\nPráctica While 3:");
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3];
for n in lista_numeros:
    if n >= 0:
        print(n);
    else:
        break;

print("\nPráctica Rango 1:");
mi_lista = list(range(2500,2586));
print(mi_lista);

print("\nPráctica Rango 2:");
mi_lista = list(range(3,301,3));
print(mi_lista);

print("\nPráctica Rango 3:");
suma_cuadrados = 0
for i in range(1,16):
    suma_cuadrados += i**2;
print("La suma de los cuadrados es: ", suma_cuadrados);

print("\nPráctica Enumerador  1:");
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"];
for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}');

print("\nPráctica Enumerador 2:");
lista_indices = list(enumerate("Python"));
print(lista_indices);

print("\nPráctica Enumerador 3:");
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"];
for i, nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(i);

print("\nPráctica Zip 1:");
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"];
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"];
for pais, capital in zip(paises, capitales):
    print(f"La capital de {pais} es {capital}");

print("\nPráctica Zip 2:");
marc = ["Nike", "Lenovo", "Nissan"];
produc = ["zapatillas", "notebook", "automóviles"];
mi_zip = zip(marc, produc);
print(mi_zip);

print("\nPráctica Zip 3:");
espaniol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]
numeros = list(zip(espaniol, portugues, ingles));
print(numeros);

print("\nPráctica Min y Max 1:");
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5];
valor_maximo = max(lista_numeros);
print("El valor máximo de la lista es: ", valor_maximo);

print("\nPráctica Min y Max 2:");
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango = max(lista_numeros) - min(lista_numeros)
print("La diferencia entre el valor máximo y mínimo de la lista es: ", rango);

print("\nPráctica Min y Max 3:");
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())
print(f'La edad mínima es {edad_minima} y el último nombre es {ultimo_nombre}');

print("\nPráctica Random 1:");
aleatorio = randint(1,10);
print("El aleatorio elegido es: ",aleatorio);

print("\nPráctica Random 2:");
aleatorio = random();
print("El aleatorio elegido es: ",aleatorio);

print("\nPráctica Random 3:");
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"];
sorteo = choice(nombres);
print(f'El ganador del sorteo elegido aleatoriamente es: {sorteo}');

print("\nPráctica Compresión de listas 1:");
valores = [1, 2, 3, 4, 5, 6, 9.5];
valores_cuadrado = [valor**2 for valor in valores];
print("Los valores de los cuadrados son: ",valores_cuadrado);

print("\nPráctica Compresión de listas 2:");
valores = [1, 2, 3, 4, 5, 6, 9.5];
valores_pares = [valor for valor in valores if valor%2 == 0];
print("Los valores de los pares contenidos en la lista son: ",valores_pares);

print("\nPráctica Compresión de listas 3:");
temperatura_fahrenheit = [32, 212, 275];
grados_celsius = [(temperatura-32)*(5/9) for temperatura in temperatura_fahrenheit];
print("Los valores para grados Celsius son: ",grados_celsius);

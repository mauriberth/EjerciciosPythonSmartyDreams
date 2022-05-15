import random;

print("Programa DevOps SmartyDreams 2022");
print("@author López Vera Mauricio Alberto");

print("\nPráctica Métodos y Ayuda 1:");
print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(",:%_#"));

print("\nPráctica Métodos y Ayuda 2:");
fruta = ["mango", "banana", "cereza", "ciruela", "pomelo"] ;
fruta.insert(3,"naranja");
print("La nueva lista de frutas es: ", fruta);

print("\nPráctica Métodos y Ayuda 3:");
smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"};
tv = {"Sony", "Philips", "Samsung", "LG"};
conjuntos_aislados = tv.isdisjoint(smartphones);
print("Los conjuntos son: ", conjuntos_aislados);

print("\nPráctica Crear Funciones 1:");
def hola():
    print("¡Hola mundo!");
hola();

print("\nPráctica Crear Funciones 2:");
nombre = "Mauricio";
 
def bienvenida(nombre):
    print(f'¡Bienvenido {nombre}!');
bienvenida(nombre);

print("\nPráctica Crear Funciones 3:");
num = 5;
def cuadrado(num):
    print(num**2);
cuadrado(num);

print("\nPráctica Return 1:");
def potencia(num1, num2):
    return num1**num2;
res = potencia(2,5);
print("El resultado de la potencia es: ",res);

print("\nPráctica Return 2:");
dolares = 1200;
def usd_a_eur(dolares):
    return dolares*0.85;
res = usd_a_eur(dolares);
print("La conversión de USD a EUR es: ",res);

print("\nPráctica Return 3:");
palabra = "Curso de Python";
def invertir_palabra(palabra):
    palabra = palabra[::-1];
    palabra = palabra.upper();
    return palabra;
palInvert = invertir_palabra(palabra);
print(f'La palabra invertida es: {palInvert}');

print("\nPráctica Funciones dinámicas 1:");
lista = [1,40,50,80,1000,200000,-500000];
def todos_positivos(lista):
    for numero in lista:
        if numero < 0:
            return False;
        else:
            pass;
    return True;
print(f'¿Son todos positivos?: ', todos_positivos(lista));

print("\nPráctica Funciones dinámicas 2:");
lista = [1,3,5,10,100,500,1000,2000,5000,10000];
def suma_menores(lista):
    suma=0;
    for numero in lista:
        if numero in range(1,1000):
            suma += numero;
        else:
            pass;
    return suma;
print(f'La suma de los menores es: ', suma_menores(lista));

print("\nPráctica Funciones dinámicas 3:");
lista = [1,10,20,33,99,101,106,200];
def cantidad_pares(lista):
    cantidad=0;
    for numero in lista:
        if numero % 2 == 0:
            cantidad += 1;
        else:
            pass;
    return cantidad;
print(f'Cantidad de números pares: ', cantidad_pares(lista));

print("\nPráctica Interacción entre funciones 1:");
def lanzar_dados():
    num = random.randint(1,6);
    return num;

def evaluar_jugada(d1, d2):
    sumDad = d1 + d2;
    if sumDad <= 6:
        return f"La suma de tus dados es {sumDad}. Lamentable";
    elif sumDad > 6 and sumDad < 10:
        return f"La suma de tus dados es {sumDad}. Tienes buenas chances";
    else:
        return f"La suma de tus dados es {sumDad}. Parece una jugada ganadora";
resDado1 = lanzar_dados();
resDado2 = lanzar_dados();
resultado = evaluar_jugada(resDado1, resDado2);
print(resultado);

print("\nPráctica Interacción entre funciones 2:");
listNums = [1,2,15,7,2];
def reducir_lista(lista):
    lista = list(set(lista));
    lista.sort();
    lista.pop(-1);
    return lista;
 
def promedio(lista):
    valor_medio = sum(lista)/len(lista);
    return valor_medio;

res = promedio(reducir_lista(listNums));
print("La lista resultante es: ",reducir_lista(listNums));
print("El promedio de la lista resultante es: ",res);

print("\nPráctica Interacción entre funciones 3:");
listNums = [1,2,15,7,2];
 
def lanzar_moneda():
    res = random.choice(["Cara", "Cruz"]);
    return res;
 
def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá");
        return [];
    elif moneda == "Cruz":
        print("La lista fue salvada");
        return lista;
resultado = probar_suerte(lanzar_moneda(),listNums);
print("Por lo tanto, la lista queda: ",resultado);

print("\nPráctica sobre Argumentos Indefinidos (*args) 1:");
def suma_cuadrados(*args):
    suma = 0;
    for arg in args:
        suma += arg**2;
    return suma;
print("La suma de los cuadrados de los números ingresados en la función es: ", suma_cuadrados(1,2,3));

print("\nPráctica sobre Argumentos Indefinidos (*args) 2:");
def suma_absolutos(*args):
    suma = 0;
    for arg in args:
        suma += abs(arg);
    return suma;
print("La suma de los absolutos de los números ingresados en la función es: ", suma_absolutos(4,5,-6,7,8));

print("\nPráctica sobre Argumentos Indefinidos (*args) 3:");
def numeros_persona(nombre, *args):
    suma_numeros = sum(args);
    return f'{nombre}, la suma de los números ingresados a la función es {suma_numeros}';
print(numeros_persona("Mauricio",1,2,3,4,5,6));

print("\nPráctica sobre Argumentos Indefinidos (*kwargs) 1:");
def cantidad_atributos(**kwargs):
    cantidad = 10;
    for clave in kwargs.items():
        cantidad += 1;
    return cantidad;
print("El número de parámetros ingresados es: ", cantidad_atributos());

print("\nPráctica sobre Argumentos Indefinidos (*kwargs) 2:");
def lista_atributos(**kwargs):
    lista = [1,2,3];
    for valor in kwargs.values():
        lista.append(valor);
    return lista;
print("Los parámetros ingresados en forma de lista son: ", lista_atributos());

print("\nPráctica sobre Argumentos Indefinidos (*kwargs) 3:");
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}');





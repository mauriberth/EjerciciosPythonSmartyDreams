from ast import List


print("Programa DevOps SmartyDreams 2022");
print("@author López Vera Mauricio Alberto");

print("\nPráctica Método Index() 1:");
palabra = "ordenador";
print("\nEl caracter que ocupa la posición 5 es: ", palabra[5])

print("\nPráctica Método Index() 2:");
fra = "En toria, la teoria y la practica son los mismos. En la practica, no lo son";
resultado = fra.index("p");
print("El índice de la primera aparición es: ",resultado);

print("\nPráctica Método Index() 3:");
fra = "En toria, la teoria y la practica son los mismos. En la practica, no lo son";
resultado = fra.rindex("p");
print("El índice de la última aparición es: ",resultado);

print("\nPráctica Substrings 1: ");
fra = "Controlar la complejidad es la esencia de la programacion";
print("La palabra extraída con slicing es: ",fra[0:9]);

print("\nPráctica Substrings 2: ");
fra = "Nunca confies en un ordenador que no puedas lanzar por una ventana";
print("Los caracteres extraídos son: ",fra[9:len(fra):3]); #En el caso de la función, estamos diciendo que comienza en el noveno caracter, termina hasta la longitud de la frase y tomará de 3 en 3.

print("\nPráctica Substrings 3: ");
fra = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
resultado = list(fra);
resultado.reverse();
print(resultado);

print("\nPráctica Métodos de String 1: ");
fra = "Especialmente en las comunicaciones electronicas, la escritura enteramente en mayusculas equivale a gritar.";
print("El texto en mayúscula es: ",fra.upper());

print("\nPráctica Métodos de String 2: ");
list = ['La', 'legibilidad', 'cuenta.'];
resultado = ' '.join(list);
print("El string resultante de la unión de la lista es: ",resultado);

print("\nPráctica Métodos de String 3: ");
fra = "Si la implementacion es dificil de explicar, puede que sea una mala idea.";
remp1 = fra.replace('dificil','fácil');
remp2 = remp1.replace('mala','buena');
print("La nueva frase es: ",remp2);

print("\nPráctica Propiedades de String 1: ");
print(' Repetición \t' * 15);

print("\nPráctica Propiedades de String 2: ");
haiku = """Tierra mojada
    mis recuerdos de viaje,
    entre las  lluvias""";
palabra = "agua";
print(f'La palabra {palabra} ¿se encuentra en el haiku?: ',palabra in haiku);

print("\nPráctica Propiedades de String 3: ");
palabra = "electroencefalografista";
res = len(palabra);
print(f'El largo de la palabra {palabra} es: ',res);

print("\nPráctica Listas 1: ");
mi_lista = ['Hola Mundo', 'SmartyDreams', 2022, 45+2, False];
print("La lista creada es: ", mi_lista);

print("\nPráctica Listas 2: ");
list = ['avion', 'auto', 'barco', 'bicicleta'];
print("La lista original es: ", list);
list.append('motocicleta');
print("\nLa lista con el nuevo elemento es: ", list);

print("\nPráctica Listas 3: ");
frutas = ['manzana', 'banana', 'mango', 'cereza', 'sandia'];
print(f"La lista original es: {frutas}");
eliminado = frutas.pop(3);
print(f"La lista resultante es: {frutas} , se le eliminó el tercer elemento: {eliminado}");

print("\nPráctica Diccionarios 1: ");
mi_dic = {
    'nombre': 'Karen',
    'apellido': 'Jurgens',
    'edad': 35,
    'ocupacion': 'periodista'
}
print(mi_dic);

print("\nPráctica Diccionarios 2: ");
mi_dic = {
    "valores_1": {'v1': 3, 'v2': 6},"puntos": {'points1': 9, 'points2': [10, 300, 15]}
}
print("El segundo item del diccionario es: ",mi_dic['puntos']['points2'][1]) #posición 1 porque comienza desde 0 el diccionario.

print("\nPráctica Diccionarios 3: ");
mi_dic = {
    'nombre': 'Karen',
    'apellido': 'Jurgens',
    'edad': 35,
    'ocupacion': 'periodista'
}
mi_dic['pais'] = 'Argentina'
print(mi_dic);

print("\nPráctica Tuples 1: ");
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 1, 3, 2, 2, 1, 3, 2);
print("El número 2 se repite un total de: ",mi_tupla.count(2), " veces en la tupla.");

#print("\nPráctica Tuples 2: ");
#mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2);
#mi_lista = list(mi_tupla);
#print(mi_lista);

print("\nPráctica Tuples 3: ");
mi_tupla = (1,2,3,4);
a = mi_tupla[0];
b = mi_tupla[1];
c = mi_tupla[2];
d = mi_tupla[3];
print(a, b, c, d);

print("\nPráctica Sets 1: ");
s1 = {1, 2, 'tres', 'cuatro'};
s2 = {'tres', 4, 5};
set3 = s1.union(s2);
print(set3);

print("\nPráctica Sets 2: ");
sorteo = {'Camila', 'Margarita', 'Axel', 'Jorge', 'Miguel'};
winner = sorteo.pop();
print("El ganador del sorteo es: ",winner);

print("\nPráctica Sets 3: ");
sorteo = {'Camila', 'Margarita', 'Axel', 'Jorge', 'Miguel'}
sorteo.add('Damián');
print("Los participantes del sorteo son: ", sorteo);

print("\nPráctica Booleanos 1: ");
prueba = 50 >= 25;
print("El resultado de la prueba es: ", prueba);

print("\nPráctica Booleanos 2: ");
print("El resultado es: ",(17834 / 34) > (87 * 56));

print("\nPráctica Booleanos 3: ");
print("El resultado es: ",(25 ** 0.5) == 5);



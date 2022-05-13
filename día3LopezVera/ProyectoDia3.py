print("Programa DevOps SmartyDreams 2022");
print("@author López Vera Mauricio Alberto");

#Crear un programa que le pida al usuario que ingrese un texto.
# Posteriormente, el programa le pedirá al usuario que ingrese tres letras a su elección.
# el código hará 5 tipos de analisis:
# 1.- ¿Cuántas veces aparece cada una de las letras que eligió?
# 2.- ¿Cuántas palabras hay a lo largo de todo el texto?
# 3.- ¿Cuál es la primera letra del texto y cuál es la ultima?
# 4.- Mostrar cómo quedaría el texto si invirtiera el orden de las palabras?
# 5.- ¿La palabra python se encuentra dentro del texto?

print("Hola. ¡Bienvenido al analizador de texto! \n");
print("Comenzaremos poco a poco. Primeramente, ingresa un texto.\n");
texto = input('Ingresa el texto ahora: ').lower();
print("¡Bien!, lo he recibido. \n");
l1 = input('Ingresa la primera letra: ').lower();
l2 = input('Ingresa la segunda letra: ').lower();
l3 = input('Ingresa la tercera letra: ').lower();
print("¡Bien!, he recibido las tres letras. \n");
print("Ahora, comenzemos con el análisis de lo ingresado. \n");
print("Procederé a decirte cuántas veces aparecen en el texto las letras que me ingresaste y cuántas palabras tiene el texto.\n");
print(f'Dentro del texto, la letra {l1} aparece {texto.count(l1)} veces.');
print(f'Dentro del texto, la letra {l2} aparece {texto.count(l2)} veces.');
print(f'Dentro del texto, la letra {l3} aparece {texto.count(l3)} veces.');
descomPalabras = texto.split();
print(f'El texto tiene un total de {len(descomPalabras)} palabras.');

ultima = descomPalabras[len(descomPalabras) - 1];
ultima2 = len(ultima);
print(f'El texto inicia con la letra {descomPalabras[0].__getitem__(0).upper()} y termina con la letra {ultima[ultima2-1:]}');

#result = texto;
#result.reverse();
#result = ' '.join(list);
#print("El string resultante de la unión de la lista al revés es: ",result);

if 'python' in texto:
    print('La palabra Python aparece en el texto.')

else:
    print('La palabra Python NO aparece en el texto.')

print("\n ANALIZADOR FINALIZADO. Gracias por usar.");







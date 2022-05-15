from random import choice

print("Programa DevOps SmartyDreams 2022");
print("@author López Vera Mauricio Alberto");

#Elige una palabra secreta y mostrarle al usuario una serie de guiones que representan en número de letras que tiene la palabra.
#El jugador en cada turno debe elegir una letra y si la letra elegida se encuentra en la palabra oculta, debe mostrarse en su posición.
#Si el jugador dice una letra que no se encuentra en la palabra oculta, pierde una vida.
#Si se agotan las vidas antes de que el jugador adivine la palabra, pierde. De lo contrario, gana.

palabras = ['upiicsa', 'politecnico', 'smartydreams', 'computadora'];
letrasBien = [];
letrasMal = [];
intentos = 6;
aciertos = 0;
juego_terminado = False;


def palabraEleg(lista_palabras):
    palEleg = choice(lista_palabras);
    uniqueLet = len(set(palEleg));
    return palEleg, uniqueLet;

def solicitudLetter():
    seleccionLetra = '';
    es_valida = False;
    abecedario = 'abcdefghijklmnñopqrstuvwxyz';
    while not es_valida:
        seleccionLetra = input("Teclea una letra: ");
        if seleccionLetra in abecedario and len(seleccionLetra) == 1:
            es_valida = True;
        else:
            print("Esa no es una lectra correcta.");
    return seleccionLetra;

def mostrar_nuevo_tablero(palEleg):
    ListOcult = [];
    for l in palEleg:
        if l in letrasBien:
            ListOcult.append(l);
        else:
            ListOcult.append('-');
    print(' '.join(ListOcult));


def chequear_letra(seleccionLetra, palabra_oculta, vidas, coincidencias):
    fin = False;
    if seleccionLetra in palabra_oculta:
        letrasBien.append(seleccionLetra);
        coincidencias += 1;
    else:
        letrasMal.append(seleccionLetra);
        vidas -= 1;
    if vidas == 0:
        fin = perder();
    elif coincidencias == uniqueLet:
        fin = ganar(palabra_oculta);
    return vidas, fin, coincidencias;

def perder():
    print("**** GAME OVER **** Sin vidas.");
    print("La palabra oculta era: " + palabra);
    return True;

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta);
    print("¡Muchísimas felicidades, la palabra es correcta!");
    return True;
palabra, uniqueLet = palabraEleg(palabras);

while not juego_terminado:
    print('\n' + '*' * 20 + '\n');
    mostrar_nuevo_tablero(palabra);
    print('\n');
    print('Letras incorrectas: ' + '-'.join(letrasMal));
    print(f'Vidas: {intentos}');
    print('\n' + '*' * 20 + '\n');
    letra = solicitudLetter();
    intentos, terminado, aciertos = chequear_letra(letra,palabra,intentos,aciertos);
    juego_terminado = terminado;
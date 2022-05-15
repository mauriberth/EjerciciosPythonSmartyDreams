print("Programa DevOps SmartyDreams 2022");
print("@author López Vera Mauricio Alberto");

#Preguntar al usuario su nombre y posteriormente comentarle que se ha elegido un número entre el 1 y el 100.
#Se tienen 8 intentos para adivinar.
#Si el usuario dijo un número menor al que ha pensado el programa hay que decirle que ha elegido un número incorrecto y que es menor.
#Si el usuario dijo un número mayor al que ha pensado el programa hay que decirle que ha elegido un número incorrecto y que es mayor.
#Si el usuario eligió el número correcto, se le indicará que ha ganado.
from random import randint

intentos = 0;
estimado = 0;
numSecret = randint(1,100);
nombre = input("Dime tu nombre: ");

print(f"{nombre}, Este programa ha pensado un número entre 1 y 100\nÚnicamente tienes 8 intentos para adivinar.");

while intentos < 8:
    estimado = int(input("¿Cuál es el número?: "));
    intentos += 1;

    if estimado < numSecret:
        print("El número pensado es mas alto");
    elif estimado > numSecret:
        print("El número pensado es mas bajo");
    else:
        print(f"{nombre}, has adivinado en {intentos} intentos. ¡Muchísimas felicidades!");
        break;

if estimado != numSecret:
    print(f"Ya no quedan intentos disponibles. El numero secreto era {numSecret}");
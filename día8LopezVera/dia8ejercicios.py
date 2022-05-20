print("Programa DevOps SmartyDreams 2022");
print("@author López Vera Mauricio Alberto");

print("\nPráctica Manejo de Errores 1:");
def suma(num1,num2):
    try:
        print(num1+num2);
    except:
        print("Se ha presentado un error desconocido e inesperado.");
suma(1,'a'); #aquí forzamos el error al pasarle como parámetro un string.

print("\nPráctica Manejo de Errores 2:");
def cociente(num1,num2):
    try:
        print(num1/num2);
    except TypeError:
        print("No estás ingresando valores numéricos.");
    except ZeroDivisionError:
        print("No debes poner un 0 como denominador puesto que es indefinida la operación.");
cociente(20,0);

print("\nPráctica Manejo de Errores 3:");
def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo);
    except FileNotFoundError:
        print("El archivo no fue encontrado");
    except:
        print("Error desconocido");
    else:
        print("Abriendo exitosamente");
    finally:
        print("Finalizando ejecución");
abrir_archivo('archivo.txt');

print("\nPráctica Generadores 1:");
def secuencia_infinita():
    num = 0;
    while True:
        num += 1;
        yield num;
generador = secuencia_infinita();

print("\nPráctica Generadores 2:");
def Mult7():
    num = 1;
    while True:
        yield 7*num;
        num += 1;
generador = Mult7();

print("\nPráctica Generadores 3:");
def mensaje():
    x = "Te quedan 3 vidas";
    yield x;
    x = "Te quedan 2 vidas";
    yield x;
    x = "Te queda 1 vida";
    yield x;
    x = "Game Over";
    yield x;
perder_vida = mensaje();
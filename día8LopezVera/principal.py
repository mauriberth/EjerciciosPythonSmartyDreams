import numeros
print("Programa DevOps SmartyDreams 2022");
print("@author López Vera Mauricio Alberto");

def preguntar():

    print("¡Bienvenido a Farmacias Guadalajara.")

    while True:
        print("P.- Perfumería\nF.- Farmacia\nC.- Cosméticos")
        try:
            mi_rubro = input("Elija el área: ").upper()
            ["P", "F", "C"].index(mi_rubro)
        except ValueError:
            print("La opción ingresada es incorrecta. Ingrese nuevamente.")
        else:
            break

    numeros.decorador(mi_rubro)


def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input("¿Desea sacar un nuevo turno? (S/N): ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Opción ingresada es inválida.")
        else:
            if otro_turno == "N":
                print("¡Muchas gracias por tu visita. Vuelve pronto.")
                break
inicio()

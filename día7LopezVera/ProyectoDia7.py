print("Programa DevOps SmartyDreams 2022");
print("@author López Vera Mauricio Alberto");

class Persona:

    def __init__(self, nom, apell):
        self.nom = nom
        self.apell = apell


class Cliente(Persona):
    def __init__(self, nom, apell, NoCuenta, balance = 0):
        super().__init__(nom, apell)
        self.NoCuenta = NoCuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nom} {self.apell}\nBalance de la cuenta {self.NoCuenta}: ${self.balance}"

    def depositar(self, montoDepositado):
        self.balance += montoDepositado
        print("El dinero fue depositado correctamente.")

    def retirar(self, montoRet):
        if self.balance >= montoRet:
            self.balance -= montoRet
            print("El retiro fue realizado correctamente.")
        else:
            print("No se tienen los fondos suficientes para retirar el dinero.")


def crear_cliente():
    nombreCliente = input("Ingrese su nombre: ")
    apellidoCliente = input("Ingrese su apellido: ")
    NoCuenta = input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombreCliente, apellidoCliente, NoCuenta)
    return cliente


def inicio():
    newClient = crear_cliente()
    print(newClient)
    opcion = 0

    while opcion != 'S':
        print('Elija una de las siguientes opciones que tenemos para usted: Depositar (D), Retirar (R) o Salir del programa (S)')
        opcion = input()

        if opcion == 'D':
            montoADepositar = int(input("¿Cuál es el monto de dinero a depositar?: "))
            newClient.depositar(montoADepositar)
        elif opcion == 'R':
            montoARetirar = int(input("¿Cuál es el monto de dinero a retirar?: "))
            newClient.retirar(montoARetirar)
        print(newClient)

    print("Gracias por utilizar la aplicación bancaria SmartyBank. Buen día.")
inicio()
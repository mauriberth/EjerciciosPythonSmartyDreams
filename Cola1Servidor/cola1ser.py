import math

#Declaración de variables

z= 0
bandera= 0
bandera2= 0
hllegada= 0
tInicio= 0
tSalServ= 0
tECola= 0
tSistema= 0
TME= 0
TMS = 0

valoresX=[]
valoresY = []

aleatoriosLlegadas = [
    0.5391, 0.9335, 0.5353, 0.2892, 0.9926, 0.0676, 0.03, 0.2427, 0.0235, 0.6536
]

aleatoriosServicio = [
    0.03, 0.8952, 0.0683, 0.21, 0.4945, 0.9373, 0.3972, 0.8293, 0.9448, 0.9935
]

#Codificación de la lógica del programa
#Primer servicio
print("Aleatorio X: \t Valor de X: \t Aleatorio Y: \t Valor de Y:")
for i in range(len(aleatoriosLlegadas)):
    bandera = -3*math.log(aleatoriosLlegadas[i])
    valoresX.append(bandera)
    bandera2 = 2*aleatoriosServicio[i] + 3
    valoresY.append(bandera2)
    print("%.4f \t\t\t %.2f \t\t\t %.4f \t\t\t %.2f"% (aleatoriosLlegadas[i], valoresX[i], aleatoriosServicio[i], valoresY[i]))

print("\n\nCliente \t\t Tiempo Llegadas: \t Hora Llegada: \t T.Inicio Serv: \t Tiempo del Serv: \t T. Salida Serv: \t T.Espera Cola: \t T.Sistema")
hllegada = hllegada + valoresX[0]
tInicio = hllegada
tSalServ = tInicio + valoresY[0]
tECola = tInicio - hllegada
TME = TME + tECola
tSistema = tSalServ - tInicio
TMS = TMS + tSistema
print("%d \t\t\t %.2f \t\t\t %.2f \t\t\t %.2f \t\t\t %.2f \t\t\t %.2f \t\t\t %.2f \t\t\t %.2f" % (z+1, valoresX[0], hllegada, tInicio, valoresY[0], tSalServ, tECola, tSistema))

#Servicios subsecuentes
for i in range(9):
    z = i + 1
    hllegada = hllegada + valoresX[z]
    tInicio = tSalServ
    tSalServ = tInicio + valoresY[z]
    tECola = tInicio - hllegada
    if tECola < 0:
        tECola = 0
    TME = TME + tECola
    tSistema = tSalServ - tInicio
    TMS = TMS + tSistema
    print("%d \t\t\t %.2f \t\t\t %.2f \t\t\t %.2f \t\t\t %.2f \t\t\t %.2f \t\t\t %.2f \t\t\t %.2f" % (z+1, valoresX[z], hllegada, tInicio, valoresY[z], tSalServ, tECola, tSistema))

#Impresión de resultados

print("\n\n\n ----- CALCULO DE TME y TMS -----")
print(" El tiempo medio de espera es: %.2f" % (TME/10))
print(" El tiempo medio en el sistema es: %.2f" % (TMS/10))
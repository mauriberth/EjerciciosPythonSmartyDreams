print("Programa DevOps SmartyDreams 2022");
print("@author López Vera Mauricio Alberto");

nombre = print(input('¿Cuál es tu nombre?: '));
venta = print(float(input('Cuánto has vendido en este mes?: ')));
base = 13;
comision = venta * base / 100;
print(f'Estimado/a {nombre}, tu venta este mes fue de {venta} y, por lo tanto, te corresponden el', round(comision,4),' de comisión. ¡Felicidades!');
print("Programa DevOps SmartyDreams 2022");
print("@author López Vera Mauricio Alberto");

print("\nPráctica con variables 1:");
nombre = 'Tony Soprano';
edad = 51;
print(f"El nombre ingresado es {nombre} y su edad es {edad}");

print("\nPráctica con variables 2:");
nombre= 'Julia';
apellido = 'Roberts';
nomComp = nombre + " " + apellido;
print(nomComp);

print("\nPráctica con variables 3:");
curso = 'Python';
print("El curso que estás tomado es " + curso);

print("\nPráctica Formatear Cadenas 1:");
nom_asociado = 'Jesse Pinkman';
num_asociado = 399058;
print(f'Estimado/a {nom_asociado}, su número de asociado es: {num_asociado}');

print("\nPráctica Formatear Cadenas 2:");
newPuntos = 350;
TotalPuntos = 1225;
print(f'Usted ha ganado {newPuntos} puntos; su nuevo saldo de puntos es: {TotalPuntos}');

print("\nPráctica Formatear Cadenas 3:");
newPuntos = 350;
PuntosAnt = 800;
print(f'Usted ha ganado {newPuntos} puntos; su nuevo saldo de puntos es: {PuntosAnt + newPuntos}');

print("\nPráctica Redondeo 1:");
n1 = 10;
n2 = 3;
print(f'La división de {n1}/{n2} es igual a = ', round(n1/n2,2));

print("\nPráctica Redondeo 2:");
num = 10.676767
print(f'El redondeo de {num} es igual a = ', str(round(num)));

print(f'La raíz cuadrada del 5 es: ', round(5**1/2,4));
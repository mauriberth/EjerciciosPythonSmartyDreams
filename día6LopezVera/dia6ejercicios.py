from pathlib import Path

print("Programa DevOps SmartyDreams 2022");
print("@author López Vera Mauricio Alberto");

print("\nPráctica Abrir y Manipular Archivos 1:");
archivo = open('texto.txt');
print(archivo.read());

print("\nPráctica Abrir y Manipular Archivos 2:");
mi_archivo = open("texto.txt");
print(mi_archivo.readline());

print("\nPráctica Abrir y Manipular Archivos 3:");
archivo = open("texto.txt");
lineas = archivo.readlines();
print(lineas[1]);

print("\nPráctica Crear y Escribir Archivos 1");
archivo = open("mi_archivo.txt", "w");
archivo.write("Nuevo texto ingresado.");
archivo.close();
archivo = open("mi_archivo.txt", "r");
print(archivo.read());

print("\nPráctica Crear y Escribir Archivos 2");
archivo = open("mi_archivo.txt","a");
archivo.write("\nInicio de sesión.");
archivo.close();
archivo = open("mi_archivo.txt", "r");
print(archivo.read());

print("\nPráctica Crear y Escribir Archivos 3");
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"];
registro = open("registro.txt","a");
for item in registro_ultima_sesion:
    registro.writelines(item +'\t');
registro.close();
registro = open("registro.txt","r");
print(registro.read());

print("\nPráctica Path 1");
ruta_base = Path.home()
print("La ruta es: ",ruta_base);

print("\nPráctica Path 2");
ruta = Path("Curso Python","Día 6","practicas_path.py");
print("La ruta es: ",ruta);

print("\nPráctica Path 3");
ruta = Path(Path.home(), "Curso Python","Día 6","practicas_path.py")
print("La ruta es: ",ruta);

print("\nPráctica Archivos y Funciones 1");
def abrir_leer(archivo):
    archivo = open(archivo);
    return archivo.read();
print(abrir_leer("texto.txt"));

print("\nPráctica Archivos y Funciones 2");
def sobrescribir(archivo):
    archivo_sobrescribir = open(archivo, "w")
    archivo_sobrescribir.write("Se ha eliminado correctamente el contenido del archivo.")
print(sobrescribir("texto.txt"));

print("\nPráctica Archivos y Funciones 3");
def registro_error(archivo):
    mi_archivo = open(archivo, "a");
    mi_archivo.write("se ha registrado un error de ejecución");
    mi_archivo.close();
print(registro_error("texto.txt"));
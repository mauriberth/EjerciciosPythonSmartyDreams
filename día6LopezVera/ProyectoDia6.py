import os
from pathlib import Path
from os import system

print("Programa DevOps SmartyDreams 2022");
print("@author López Vera Mauricio Alberto");

rutaCreada = Path(Path.home(), "Recetas");
def ContRecet(ruta):
    cont = 0;
    for txt in Path(ruta).glob("**/*.txt"):
        cont += 1;
    return cont;

def eleccionCateg(lista):
    eleccion = 'x';
    while not eleccion.isnumeric() or int(eleccion) not in range(1, len(lista) + 1):
        eleccion = input("\nElije una categoria: ");
    return lista[int(eleccion) - 1];

def eleccionRecet(lista):
    recetaElegida = 'x';
    while not recetaElegida.isnumeric() or int(recetaElegida) not in range(1, len(lista) + 1):
        recetaElegida = input("\nElije una receta: ");
    return lista[int(recetaElegida) - 1];

def vistaCateg(ruta):
    print("Categorias:");
    RCategorias = Path(ruta);
    LCategorias = [];
    cont = 1;

    for carpeta in RCategorias.iterdir():
        strCarpeta = str(carpeta.name);
        print(f"\n{cont}.- {strCarpeta}");
        LCategorias.append(carpeta);
        cont += 1;
    return LCategorias;

def vistaRecetas(ruta):
    print("Recetas:");
    recetasRuta = Path(ruta);
    LRecetas = [];
    cont = 1;

    for receta in recetasRuta.glob('*.txt'):
        StringReceta = str(receta.name);
        print(f"\n{cont}.- {StringReceta}");
        LRecetas.append(receta);
        cont += 1;
    return LRecetas;

def obtenerReceta(receta):
    print(Path.read_text(receta));

def nuevaReceta(ruta):
    validarReceta = False;
    while not validarReceta:
        print("Ingrese el nombre de la nueva receta: ");
        recetaNom = input() + '.txt';
        print("Ingresa la receta: ");
        desgloseRecet = input();
        crearNewRuta = Path(ruta, recetaNom);
        if not os.path.exists(crearNewRuta):
            Path.write_text(crearNewRuta, desgloseRecet);
            print(f"La receta {recetaNom} fue creada satisfactoriamente.");
            validarReceta = True;
        else:
            print("La receta ingresada ya existe. Ingresa un nuevo nombre.");

def nuevaCateg(ruta):
    validarReceta = False;
    while not validarReceta:
        print("Ingrese la nueva categoría: ");
        nomCateg = input();
        crearNewRuta = Path(ruta, nomCateg);

        if not os.path.exists(crearNewRuta):
            Path.mkdir(crearNewRuta);
            print(f"La categoría {nomCateg} fue creada satisfactoriamente.");
            validarReceta = True;
        else:
            print("La categoría ingresada ya existe. Ingresa un nuevo nombre.");

def DeleteRecet(receta):
    Path(receta).unlink();
    print(f"La receta {receta.name} fue eliminada satisfactoriamente.");

def DeleteCateg(categoria):
    Path(categoria).rmdir();
    print(F"La categoria {categoria.name} fue eliminada satisfactoriamente.");

def regresarIndex():
    opcRegresar = 'x';
    while opcRegresar.lower() != 's':
        opcRegresar = input("\nPresione S para volver al menu: ");
finP = False;

def index():
    print(f"Las recetas se encuentran en {rutaCreada}");
    print(f"Total recetas existentes: {ContRecet(rutaCreada)}");
    opc = 'x';
    while not opc.isnumeric() or int(opc) not in range(1,7):
        print("Elige una opcion.");
        print('\n1.- Leer receta.');
        print('\n2.- Crear receta.');
        print('\n3.- Crear categoria.');
        print('\n4.- Eliminar receta.');
        print('\n5.- Eliminar categoria.');
        print('\n6.- Salir del programa.');
        print("\nTeclea tu opción: ", );
        opc = input();
    return int(opc);

while not finP:
    menuOpciones = index();
    if menuOpciones == 1:
        bibCateg = vistaCateg(rutaCreada);
        categElegida = eleccionCateg(bibCateg);
        bibRecet = vistaRecetas(categElegida);
        recetElegida = eleccionRecet(bibRecet);
        obtenerReceta(recetElegida);
        regresarIndex();
    elif menuOpciones == 2:
        bibCateg = vistaCateg(rutaCreada);
        categElegida = eleccionCateg(bibCateg);
        nuevaReceta(categElegida);
        regresarIndex();
    elif menuOpciones == 3:
        nuevaCateg(rutaCreada);
        regresarIndex();
    elif menuOpciones == 4:
        bibCateg = vistaCateg(rutaCreada);
        categElegida = eleccionCateg(bibCateg);
        bibRecet = vistaRecetas(categElegida);
        recetElegida = eleccionRecet(bibRecet);
        DeleteRecet(recetElegida);
        regresarIndex();
    elif menuOpciones == 5:
        bibCateg = vistaCateg(rutaCreada);
        categElegida = eleccionCateg(bibCateg);
        DeleteCateg(categElegida);
        regresarIndex();
    elif menuOpciones == 6:
        finP = True;
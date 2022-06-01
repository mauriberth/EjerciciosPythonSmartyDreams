print("Programa DevOps SmartyDreams 2022");
print("@author López Vera Mauricio Alberto");
#Reconocimiento facial.

#Importación de librerías
from cv2 import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

#Creación de la BD
ruta = 'Empleados'
imgBiblio = []
empNom = []
empList = os.listdir(ruta)

for nombre in empList:
    imgActual = cv2.imread(f'{ruta}/{nombre}')
    imgBiblio.append(imgActual)
    empNom.append(os.path.splitext(nombre)[0])

print(empNom)

#Codificación de imagenes
def imgCodificacion(imagenes):
    listCodificImg = []
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        codificado = fr.face_encodings(imagen)[0]
        listCodificImg.append(codificado)
    return listCodificImg


#Registro de ingresos
def RegistroIng(persona):
    f = open('registro.csv', 'r+')
    DatList = f.readlines()
    regNombres = []
    for linea in DatList:
        ing = linea.split(',')
        regNombres.append(ing[0])

    if persona not in regNombres:
        now = datetime.now()
        string_now = now.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_now}')

empListCodificada = imgCodificacion(imgBiblio)

#Tomar fotografía
foto = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Reconocer la imagen
exito, imagen = foto.read()

if not exito:
    print("No se ha podido realizar la foto.")
else:
    fotoFace = fr.face_locations(imagen)
    fotoFaceCodific = fr.face_encodings(imagen, fotoFace)
    for caracodif, caraubic in zip(fotoFaceCodific, fotoFace):
        coincid = fr.compare_faces(empListCodificada, caracodif)
        distanc = fr.face_distance(empListCodificada, caracodif)
        print(distanc)
        i_coincid = numpy.argmin(distanc)
        if distanc[i_coincid] > 0.6:
            print("Su rostro no coincide con ningún empleado registrado.")
        else:
            nombre = empNom[i_coincid]
            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 2555, 255), 2)
            RegistroIng(nombre)
            cv2.imshow('Imagen web', imagen)
            cv2.waitKey(0)
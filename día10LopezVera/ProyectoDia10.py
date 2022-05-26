#Importaciones de librerías para el proyecto
import pygame
import random
import math
from pygame import mixer

# Inicializador de pygame
pygame.init()

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Despliegue del titulo y del icono del juego
pygame.display.set_caption("¡Llegaron los marcianos Cha Cha Chá!")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load('fondo.jpg')

# Música source
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Jugador
IMGJug = pygame.image.load("cohete.png")
jugador1 = 368
jugador2 = 500
jugador1_cambio = 0

# Enemigo
IMGEnemigo = []
enemigo1 = []
enemigo2 = []
enemigo1_cambio = []
enemigo2_cambio = []
totalEnemigos = 8

for e in range(totalEnemigos):
    IMGEnemigo.append(pygame.image.load("enemigo.png"))
    enemigo1.append(random.randint(0, 736))
    enemigo2.append(random.randint(50, 200))
    enemigo1_cambio.append(0.5)
    enemigo2_cambio.append(50)

# Bala
IMGBala = pygame.image.load("bala.png")
b1 = 0
b2 = 500
b1_cambio = 0
b2_cambio = 3
verBala = False

# Puntos
puntaje = 0
fuente = pygame.font.Font('fastest.ttf', 32)
texto1 = 10
texto2 = 10

# Final del juego
finalFont = pygame.font.Font('fastest.ttf', 40)


def texto_final():
    mi_finalFont = finalFont.render("El juego ha terminado. Gracias por jugar", True, (255, 255, 255))
    pantalla.blit(mi_finalFont, (60, 200))


# Ver puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Jugador F
def jugador(x, y):
    pantalla.blit(IMGJug, (x, y))


# Enemigo F
def enemigo(x, y, ene):
    pantalla.blit(IMGEnemigo[ene], (x, y))


# Disparar
def disparar_bala(x, y):
    global verBala
    verBala = True
    pantalla.blit(IMGBala, (x + 16, y + 10))


# Colisiones
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# Loop 
se_ejecuta = True
while se_ejecuta:

    # Fondo
    pantalla.blit(fondo, (0, 0))

    # Iteraración de eventos
    for evento in pygame.event.get():

        # Cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        #Presionar telca
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador1_cambio = -1
            if evento.key == pygame.K_RIGHT:
                jugador1_cambio = 1
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                if not verBala:
                    b1 = jugador1
                    disparar_bala(b1, b2)

        # Soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador1_cambio = 0

    # Cambiar ubic de jug
    jugador1 += jugador1_cambio

    # jugador dentro de pantalla
    if jugador1 <= 0:
        jugador1 = 0
    elif jugador1 >= 736:
        jugador1 = 736

    # Cambiar ubic de enemigo
    for e in range(totalEnemigos):

        # Fin 
        if enemigo2[e] > 500:
            for k in range(totalEnemigos):
                enemigo2[k] = 1000
            texto_final()
            break

        enemigo1[e] += enemigo1_cambio[e]

    # enemigo dentro de pantalla
        if enemigo1[e] <= 0:
            enemigo1_cambio[e] = 1
            enemigo2[e] += enemigo2_cambio[e]
        elif enemigo1[e] >= 736:
            enemigo1_cambio[e] = -1
            enemigo2[e] += enemigo2_cambio[e]

        # colision
        colision = hay_colision(enemigo1[e], enemigo2[e], b1, b2)
        if colision:
            sonido_colision = mixer.Sound('golpe.mp3')
            sonido_colision.play()
            b2 = 500
            verBala = False
            puntaje += 1
            enemigo1[e] = random.randint(0, 736)
            enemigo2[e] = random.randint(50, 200)

        enemigo(enemigo1[e], enemigo2[e], e)

    # Mover bala
    if b2 <= -64:
        b2 = 500
        verBala = False

    if verBala:
        disparar_bala(b1, b2)
        b2 -= b2_cambio


    jugador(jugador1, jugador2)

    mostrar_puntaje(texto1, texto2)

    # Refresh
    pygame.display.update()
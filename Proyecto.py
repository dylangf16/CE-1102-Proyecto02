import pygame
import os
import random

from pygame.constants import KEYDOWN, K_ESCAPE, K_RETURN, MOUSEBUTTONDOWN
from pygame.time import Clock
pygame.font.init()
pygame.init()


#Globales -----------------------------------------------------------------------
#Todo lo relacionado con la pantalla --------------------------------------------
WIDTH, HEIGHT = 1280, 720 #Tamaño de la pantalla
ANCHO_pantalla, LARGO_pantalla = 1920, 1080 #Tamaño de las imágenes
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #Creación de la pantalla base
pygame.display.set_caption("Beyond the Stars") #Nombre arriba de la ventana
FPS = 75
BORDER = pygame.Rect(WIDTH,0,0,HEIGHT) #Creación del marco de la pantalla 
run = False
run2 = True
clock = pygame.time.Clock()

#Todo lo relacionado con las mecánicas del juego ----------------------------------
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 94, 100
Ancho_asteroide , Largo_asteroide = 90,95
variable_tamaño = random.randint(-7,7)

#Todo lo relacionado con el movimiento de nave y asteroides ----------------------
VELOCIDAD = 5
x_speed, y_speed = 5,4
x2_speed, y2_speed = 5,4
x3_speed, y3_speed = 5,4
x4_speed, y4_speed = 5,4
x5_speed, y5_speed = 5,4
x6_speed, y6_speed = 5,4
x7_speed, y7_speed = 5,4
x8_speed, y8_speed = 5,4

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 50)

#Todo lo relacionado con el jugador------------------------------
vida_jugador = 3
puntaje = 0
puntaje_obtenido = 0
nombre_usuario = ''
volver = ''
lista_nombres_completados = []


#Apartado de imágenes -----------------------------------------------------------------------
título = pygame.transform.scale(pygame.image.load(os.path.join('assets2', 'imagenes', 'Título.png')), (1148, 198))
título2 = pygame.transform.scale(pygame.image.load(os.path.join('assets2', 'imagenes', 'ranking.png')), (1148, 198))
foto_Dylan = pygame.transform.scale(pygame.image.load(os.path.join('assets2', 'imagenes', 'yo.JPG')), (202, 294))
foto_Gabriel = pygame.transform.scale(pygame.image.load(os.path.join('assets2', 'imagenes', 'Pana.jpeg')), (202, 294))
fondo1 = pygame.transform.scale(pygame.image.load(os.path.join('assets2', 'imagenes', 'Fondo_nivel_1.jpg')), (ANCHO_pantalla, LARGO_pantalla))
fondo2 = pygame.transform.scale(pygame.image.load(os.path.join('assets2', 'imagenes', 'Fondo_nivel_2.jpg')), (ANCHO_pantalla, LARGO_pantalla))
fondo3 = pygame.transform.scale(pygame.image.load(os.path.join('assets2', 'imagenes', 'Fondo_nivel_3.jpg')), (ANCHO_pantalla, LARGO_pantalla))
fondo_about = pygame.transform.scale(pygame.image.load(os.path.join('assets2', 'imagenes', 'Fondo_about.jpg')), (ANCHO_pantalla, LARGO_pantalla))
fondo_ranking = pygame.transform.scale(pygame.image.load(os.path.join('assets2', 'imagenes', 'Fondo_ranking.jpg')), (ANCHO_pantalla, LARGO_pantalla))
fondo_principal = pygame.transform.scale(pygame.image.load(os.path.join('assets2', 'imagenes', 'Fondo_principal.jpg')), (ANCHO_pantalla, LARGO_pantalla))

Nave_imagen = pygame.image.load(os.path.join('assets2', 'imagenes', 'Spaceship.png')) #Llamada de la imágen
Nave_completa = pygame.transform.rotate(pygame.transform.scale(Nave_imagen, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
asteroide1 = pygame.image.load(os.path.join('assets2', 'imagenes', 'asteroide_1.png')) #Llamada de la imágen
asteroide_1_completo = pygame.transform.rotate(pygame.transform.scale(asteroide1, (Ancho_asteroide + variable_tamaño, Largo_asteroide + variable_tamaño)), 0)
asteroide2 = pygame.image.load(os.path.join('assets2', 'imagenes', 'asteroide_2.png')) #Llamada de la imágen
asteroide_2_completo = pygame.transform.rotate(pygame.transform.scale(asteroide2, (Ancho_asteroide + variable_tamaño, Largo_asteroide + variable_tamaño)), 0)
asteroide3 = pygame.image.load(os.path.join('assets2', 'imagenes', 'asteroide_3.png')) #Llamada de la imágen
asteroide_3_completo = pygame.transform.rotate(pygame.transform.scale(asteroide3, (Ancho_asteroide + variable_tamaño, Largo_asteroide + variable_tamaño)), 0)
asteroide4 = pygame.image.load(os.path.join('assets2', 'imagenes', 'asteroide_4.png')) #Llamada de la imágen
asteroide_4_completo = pygame.transform.rotate(pygame.transform.scale(asteroide4, (Ancho_asteroide + variable_tamaño, Largo_asteroide + variable_tamaño)), 0)


#Apartado de Ranking ==============================================================================================================================
#Transformar de txt de nombres a lista ------------------------------------
def conseguir_nombres(lista_nombres):
    with open('Ranking_Nombres.txt') as nombres_txt:
        lines = nombres_txt.readlines()
        lista_nombres = lines
        return sort_nombres(lista_nombres, 0)

#Acomoda los nombres con respecto a la posición del jugador
def sort_nombres(lista_nombres, conteo):
    global lista_nombres_completados, posicion, nombre_usuario, lista_nombres_completados
    posicion = int(posicion)
    if posicion > 10:
        return 0
    if posicion > conteo + 1:
        conteo += 1
        lista_nombres_completados.append(lista_nombres[0])
        return sort_nombres(lista_nombres[1:], conteo)
    else:
        nombre_usuario += '\n'
        lista_nombres_completados.append(nombre_usuario.replace('\r', ''))
        tamaño = int(len(lista_nombres) - 1)
        lista_nombres_completados = lista_nombres_completados + lista_nombres[0:tamaño]
        return sobreescribir_txt(lista_nombres_completados)

#Reescribe los los nombres al txt 
def sobreescribir_txt(lista):
    with open('Ranking_Nombres.txt', 'w') as nombres_txt:
        nombres_txt.write(lista[0])
        nombres_txt.write(lista[1])
        nombres_txt.write(lista[2])
        nombres_txt.write(lista[3])
        nombres_txt.write(lista[4])
        nombres_txt.write(lista[5])
        nombres_txt.write(lista[6])
        nombres_txt.write(lista[7])
        nombres_txt.write(lista[8])
        nombres_txt.write(lista[9])
        return 0
    
#Transformar de txt a lista ------------------------------------
def cont(conteo, lista, seek):
    global posicion
    MiArchi1= open('Ranking.txt', 'r+')
    posicion = 1
    if conteo < 10:
        MiArchi1.seek(seek)
        num = MiArchi1.readline()
        lista.append(int(num))
        conteo += 1
        seek += 5
        return cont(conteo, lista, seek)
    else:
        MiArchi1.close()
        return insert_sort(lista)


#Ordenar de menor a mayor la lista -------------------------------------
def insert_sort(Lista):
    return insert_sort_aux(Lista,1,len(Lista))

def insert_sort_aux(Lista,i,n):
    if i == n:
        return aux_invierta(Lista,[])
    Aux = Lista[i]
    j = incluye_orden(Lista,i,Aux)
    Lista[j] = Aux
    return insert_sort_aux(Lista,i+1,n)

def incluye_orden(Lista,j,Aux):
    if j <= 0 or Lista[j-1]<=Aux:
        return j
    Lista[j] = Lista[j-1]
    return incluye_orden(Lista,j-1,Aux)


#Invertir lista ------------------------------------------
def aux_invierta(lista,lista_final):
    if lista != []:
        num = lista[-1]
        lista_final.append(num)
        return aux_invierta(lista[:-1],lista_final)
    else:
        return comparar(lista_final,[])
    

#Comparar la lista con el puntaje obtenido --------------------------
def comparar(lista,lista_completa):
    global posicion, puntaje_obtenido, volver
    puntaje_obtenido = int(puntaje_obtenido)
    if lista == []:
        volver =  WINNER_FONT.render('volverás a la pantalla de forma automática', 1, (255,255,255))
        return 0
    if puntaje_obtenido < lista[0]:
        num_mayor = lista[0]
        posicion += 1
        lista_completa.append(num_mayor)
        return comparar(lista[1:],lista_completa)
    else:
        lista_completa.append(puntaje_obtenido)
        tamaño = int(len(lista) - 1)
        lista_completa = lista_completa + lista[0:tamaño]
        return nueva_lista(lista_completa,0,0)


#Agregar nuevos elementos a la lista completa ----------
def nueva_lista(lista,num,seek):
    global posicion, volver
    MiArchi1= open('Ranking.txt', 'r+')
    if lista == []:
        MiArchi1.close()
        conseguir_nombres([])
        posicion = str(posicion)
        volver =  WINNER_FONT.render('Felicidades! Quedaste en la posición: '+ posicion, 1, (255,255,255))
        return 0
    else:
        MiArchi1.seek(seek)
        num = lista[0]
        num = str(num) + '\n'
        MiArchi1.write(num)
        seek += 5
        return nueva_lista(lista[1:],0,seek)



#creación aleatoria de posiciones de los asteroides
def posición_x():
    nueva_x = random.randint(150,1100)
    return nueva_x

def posición_y():
    nueva_y = random.randint(0,600)
    return nueva_y

#movimiento de la nave
def nave_movimiento(keys_pressed,nave):
    if keys_pressed[pygame.K_LEFT] and nave.x - VELOCIDAD > 0: #Movimiento a la izquierda con limites de bordes
        nave.x -= VELOCIDAD
    if keys_pressed[pygame.K_RIGHT] and nave.x + VELOCIDAD + nave.width < BORDER.x:  #Movimiento a la derecha con limites de bordes
        nave.x += VELOCIDAD
    if keys_pressed[pygame.K_UP] and nave.y - VELOCIDAD > 0:  #Movimiento para arriba con limites de bordes
        nave.y -= VELOCIDAD
    if keys_pressed[pygame.K_DOWN] and nave.y + VELOCIDAD + nave.height < HEIGHT + 5:  #Movimiento para abajo con limites de bordes
        nave.y += VELOCIDAD

#carga texto al finalizar el nivel
def draw_winner(text,mensaje_final):
    global volver, puntaje_obtenido
    cont(0, [], 0)
    draw_text = WINNER_FONT.render(text + mensaje_final, 1, (255,255,255))
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))
    WIN.blit(volver, (300,450))
    pygame.display.update()
    pygame.time.wait(7000)
    return pantalla_principal()

def siguiente(text,mensaje_final):
    draw_text = WINNER_FONT.render(text, 1, (255,255,255))
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() / 2, HEIGHT/2 - draw_text.get_height()/2))
    draw_puntaje = WINNER_FONT.render(mensaje_final, 1, (255,255,255))
    WIN.blit(draw_puntaje, (500,450))
    pygame.display.update()
    pygame.time.wait(7000)


#Apartado Pantalla 1 ===========================================================================================================================================

#Cargar y actualizar impagenes de pantalla 1
def cargar_imágenes_1(tiempo_transcurrido, vidas_jugador_txt, puntaje_txt, nave, asteroide1, asteroide2, asteroide3, asteroide4, asteroides, asteroides2, asteroides3, asteroides4):
    #Aquí se agregan todas las imágenes constanemente a la pantalla
    WIN.blit(fondo1,(0,0)) #x, y
    WIN.blit(Nave_completa, (nave.x, nave.y)) #x, y
    WIN.blit(tiempo_transcurrido, (925,0,)) #x, y
    WIN.blit(vidas_jugador_txt, (0, 0)) #x, y
    WIN.blit(puntaje_txt, (475, 0)) #x, y

    #Botón nivel fácil ----------------------------------------------------------------------
    button_principal = pygame.Rect(475, 625, 250, 50) #x, y, width, lenght
    pygame.draw.rect(WIN,(133, 19, 240),button_principal)
    principal_txt = HEALTH_FONT.render("Pantalla Principal", 1, (250,250,250))
    WIN.blit(principal_txt, (480, 635)) #x, y 
    
    #Carga los asteroides mientras no hayan colisionado con la nave (si el asteroide no está en la lista, es eliminado)
    for asteroide1 in asteroides:
        WIN.blit(asteroide_1_completo, (asteroide1.x,asteroide1.y))
    for asteroide2 in asteroides2:
        WIN.blit(asteroide_2_completo, (asteroide2.x,asteroide2.y))
    for asteroide3 in asteroides3:
        WIN.blit(asteroide_3_completo, (asteroide3.x,asteroide3.y))
    for asteroide4 in asteroides4:
        WIN.blit(asteroide_4_completo, (asteroide4.x,asteroide4.y))

    pygame.display.update()

#Funciones que detecta colisiones y el movimiento de los asteroides
def colisiones(nave,asteroide1,asteroide2,asteroide3,asteroide4, asteroides, asteroides2,asteroides3,asteroides4):
    global vida_jugador, y_speed, x_speed, x2_speed, y2_speed, x3_speed, y3_speed, x4_speed, y4_speed

    for asteroide1 in asteroides:
        asteroide1.x += x_speed #movimiento en x
        asteroide1.y += y_speed #movimiento en y
        if nave.colliderect(asteroide1): #detecta colisión con la nave
            vida_jugador = int(vida_jugador)
            vida_jugador -=1
            asteroides.remove(asteroide1)   
        if asteroide1.right >= WIDTH or asteroide1.left <= 0: #detecta colisión con los bordes laterales
            x_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
        if asteroide1.bottom >= HEIGHT or asteroide1.top <= 0: #detecta colisión con el borde superior e inferior
            y_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)

    for asteroide2 in asteroides2:
        asteroide2.x += x2_speed #movimiento en x
        asteroide2.y += y2_speed #movimiento en y
        if nave.colliderect(asteroide2): #detecta colisión con la nave
            vida_jugador = int(vida_jugador) 
            vida_jugador -=1
            asteroides2.remove(asteroide2)
        if asteroide2.right >= WIDTH or asteroide2.left <= 0: #detecta colisión con los bordes laterales
            x2_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
        if asteroide2.bottom >= HEIGHT or asteroide2.top <= 0: #detecta colisión con el borde superior e inferior
            y2_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)

    for asteroide3 in asteroides3:
        asteroide3.x += x3_speed #movimiento en x
        asteroide3.y += y3_speed #movimiento en y
        if nave.colliderect(asteroide3): #detecta colisión con la nave
            vida_jugador = int(vida_jugador)
            vida_jugador -=1
            asteroides3.remove(asteroide3)
        if asteroide3.right >= WIDTH or asteroide3.left <= 0: #detecta colisión con los bordes laterales
            x3_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
        if asteroide3.bottom >= HEIGHT or asteroide3.top <= 0: #detecta colisión con el borde superior e inferior
            y3_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)

    for asteroide4 in asteroides4:
        asteroide4.x += x4_speed #movimiento en x
        asteroide4.y += y4_speed #movimiento en y
        if nave.colliderect(asteroide4): #detecta colisión con la nave
            vida_jugador = int(vida_jugador)
            vida_jugador -=1
            asteroides4.remove(asteroide4)
        if asteroide4.right >= WIDTH or asteroide4.left <= 0: #detecta colisión con los bordes laterales
            x4_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
        if asteroide4.bottom >= HEIGHT or asteroide4.top <= 0: #detecta colisión con el borde superior e inferior
            y4_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
            
#Pantalla 1
def pantalla_juego_1():
    '''
    #=============================================================================================================
    Pantalla de juego 1
    Instituto Tecnológico de Costa Rica
    Ingenieria en Computadores
    Taller de Programación
    CE-1102
    Autores: Dylan Garbanzo Fallas, Gabriel Núñez Morales
    Versión: 1.1
    Versión de python: 3.9.1
    Entradas: pantalla de inicio
    Salida: pantalla de inicio, pantalla de juego 2
    Restricciones: no se presentan restricciones
    '''
    global vida_jugador, puntaje, nombre_usuario, puntaje_obtenido
    #Variables para reseteo de datos cada vez que carga el nivel
    vida_jugador = 3
    vida_jugador = str(vida_jugador)
    t0 = 0
    t1 = 0
    puntaje = 0

    nave = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    pygame.mixer.music.load(os.path.join('assets2', 'sonidos', 'música_nivel_1.mp3'))
    pygame.mixer.music.play(-1)

    #Apartado de asterodies de listas de asteroides y los asteroides
    asteroides= []
    asteroide1 = pygame.Rect(posición_x(), posición_y(), Ancho_asteroide, Largo_asteroide)
    asteroides.append(asteroide1)

    asteroides2= []
    asteroide2 = pygame.Rect(posición_x(), posición_y(), Ancho_asteroide, Largo_asteroide)
    asteroides2.append(asteroide2)

    asteroides3= []
    asteroide3 = pygame.Rect(posición_x(), posición_y(), Ancho_asteroide, Largo_asteroide)
    asteroides3.append(asteroide3)

    asteroides4= []
    asteroide4 = pygame.Rect(posición_x(), posición_y(), Ancho_asteroide, Largo_asteroide)
    asteroides4.append(asteroide4)

    button_principal = pygame.Rect(475, 625, 250, 50) #x, y, width, lenght
    pygame.draw.rect(WIN,(133, 19, 240),button_principal) 
    

    clock = pygame.time.Clock()
    run = True
    click = False
    while run:
        #Contador
        t0 = t0 + 0.02
        t1 = int(t0)

        #Posición del mouse
        mx,my = pygame.mouse.get_pos()
        clock.tick(FPS)

        #Mensajes con información de la partida jugada
        segundos = str(t1)
        tiempo_transcurrido = HEALTH_FONT.render('Tiempo transcurrido: ' + segundos,0,(255,255,255))
        
        vida_jugador = str(vida_jugador)
        vidas_jugador_txt = HEALTH_FONT.render('Vida de '+ nombre_usuario + ': ' + vida_jugador, 0, (250,250,250))

        #Conversiones para poder cargar el puntaje
        t1 = int(t0)
        puntaje = t1 * 1
        puntaje = str(puntaje)
        mensaje_final = 'Puntaje obtenido: '+ puntaje
        puntaje_txt = HEALTH_FONT.render(mensaje_final, 0, (250,250,250))

        #detección de eventos a lo largo de la partida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            #segunda opción para salir de la partida
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                    pantalla_principal()

            #detección de click
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            #detección de colisión entre el botón y el cursero del mouse
            if button_principal.collidepoint((mx,my)):
                if click:
                    return pantalla_principal()

        #condición de finalización
        if int(vida_jugador) <= 0:
            puntaje = int(puntaje)
            puntaje_obtenido = int(puntaje_obtenido)
            puntaje_obtenido += puntaje
            winner_text = 'Fin del juego :( '
            draw_winner(winner_text, mensaje_final)

        if t1 == 60:
            puntaje = int(puntaje)
            puntaje_obtenido = int(puntaje_obtenido)
            puntaje_obtenido += puntaje
            puntaje = str(puntaje_obtenido)
            mensaje_final = 'Puntaje obtenido: '+ puntaje
            winner_text = 'Nivel 1 completado, cargando siguiente nivel '
            run = False
            siguiente(winner_text, mensaje_final)
            return pantalla_juego_2()

        
        colisiones(nave,asteroide1,asteroide2,asteroide3,asteroide4, asteroides, asteroides2,asteroides3,asteroides4)
        keys_pressed = pygame.key.get_pressed()
        nave_movimiento(keys_pressed,nave)
        cargar_imágenes_1(tiempo_transcurrido, vidas_jugador_txt, puntaje_txt, nave, asteroide1, asteroide2, asteroide3, asteroide4, asteroides, asteroides2, asteroides3, asteroides4)
        
    
        
    pantalla_juego_1()



#Apartado Pantalla 2 ===========================================================================================================================================
def cargar_imágenes_2(tiempo_transcurrido, vidas_jugador_txt, puntaje_txt, nave, asteroide1, asteroide2, asteroide3, asteroide4, asteroide5, asteroide6, asteroides, asteroides2, asteroides3, asteroides4, asteroides5, asteroides6):
    #Aquí se agregan todas las imágenes constanemente a la pantalla
    WIN.blit(fondo2,(0,0)) #x, y
    WIN.blit(Nave_completa, (nave.x, nave.y)) #x, y
    WIN.blit(tiempo_transcurrido, (925,0,)) #x, y
    WIN.blit(vidas_jugador_txt, (0, 0)) #x, y
    WIN.blit(puntaje_txt, (475, 0)) #x, y

    #Botón nivel fácil ----------------------------------------------------------------------
    button_principal = pygame.Rect(475, 625, 250, 50) #x, y, width, lenght
    pygame.draw.rect(WIN,(133, 19, 240),button_principal)
    principal_txt = HEALTH_FONT.render("Pantalla Principal", 1, (250,250,250))
    WIN.blit(principal_txt, (480, 635)) #x, y 
    
    #Carga los asteroides mientras no hayan colisionado con la nave (si el asteroide no está en la lista, es eliminado)
    for asteroide1 in asteroides:
        WIN.blit(asteroide_1_completo, (asteroide1.x,asteroide1.y))
    for asteroide2 in asteroides2:
        WIN.blit(asteroide_2_completo, (asteroide2.x,asteroide2.y))
    for asteroide3 in asteroides3:
        WIN.blit(asteroide_3_completo, (asteroide3.x,asteroide3.y))
    for asteroide4 in asteroides4:
        WIN.blit(asteroide_4_completo, (asteroide4.x,asteroide4.y))
    for asteroide5 in asteroides5:
        WIN.blit(asteroide_1_completo, (asteroide5.x,asteroide5.y))
    for asteroide6 in asteroides6:
        WIN.blit(asteroide_2_completo, (asteroide6.x,asteroide6.y))

    pygame.display.update()

#Funciones que detecta colisiones y el movimiento de los asteroides
def colisiones_2(nave, asteroide1, asteroide2, asteroide3, asteroide4, asteroide5, asteroide6, asteroides, asteroides2, asteroides3, asteroides4, asteroides5, asteroides6):
    global vida_jugador, y_speed, x_speed, x2_speed, y2_speed, x3_speed, y3_speed, x4_speed, y4_speed, x5_speed, y5_speed, x6_speed, y6_speed

    for asteroide1 in asteroides:
        asteroide1.x += x_speed #movimiento en x
        asteroide1.y += y_speed #movimiento en y
        if nave.colliderect(asteroide1): #detecta colisión con la nave
            vida_jugador = int(vida_jugador)
            vida_jugador -=1
            asteroides.remove(asteroide1)   
        if asteroide1.right >= WIDTH or asteroide1.left <= 0: #detecta colisión con los bordes laterales
            x_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
        if asteroide1.bottom >= HEIGHT or asteroide1.top <= 0: #detecta colisión con el borde superior e inferior
            y_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)

    for asteroide2 in asteroides2:
        asteroide2.x += x2_speed #movimiento en x
        asteroide2.y += y2_speed #movimiento en y
        if nave.colliderect(asteroide2): #detecta colisión con la nave
            vida_jugador = int(vida_jugador) 
            vida_jugador -=1
            asteroides2.remove(asteroide2)
        if asteroide2.right >= WIDTH or asteroide2.left <= 0: #detecta colisión con los bordes laterales
            x2_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
        if asteroide2.bottom >= HEIGHT or asteroide2.top <= 0: #detecta colisión con el borde superior e inferior
            y2_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)

    for asteroide3 in asteroides3:
        asteroide3.x += x3_speed #movimiento en x
        asteroide3.y += y3_speed #movimiento en y
        if nave.colliderect(asteroide3): #detecta colisión con la nave
            vida_jugador = int(vida_jugador)
            vida_jugador -=1
            asteroides3.remove(asteroide3)
        if asteroide3.right >= WIDTH or asteroide3.left <= 0: #detecta colisión con los bordes laterales
            x3_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
        if asteroide3.bottom >= HEIGHT or asteroide3.top <= 0: #detecta colisión con el borde superior e inferior
            y3_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)

    for asteroide4 in asteroides4:
        asteroide4.x += x4_speed #movimiento en x
        asteroide4.y += y4_speed #movimiento en y
        if nave.colliderect(asteroide4): #detecta colisión con la nave
            vida_jugador = int(vida_jugador)
            vida_jugador -=1
            asteroides4.remove(asteroide4)
        if asteroide4.right >= WIDTH or asteroide4.left <= 0: #detecta colisión con los bordes laterales
            x4_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
        if asteroide4.bottom >= HEIGHT or asteroide4.top <= 0: #detecta colisión con el borde superior e inferior
            y4_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)

    for asteroide5 in asteroides5:
        asteroide5.x += x5_speed #movimiento en x
        asteroide5.y += y5_speed #movimiento en y
        if nave.colliderect(asteroide5): #detecta colisión con la nave
            vida_jugador = int(vida_jugador)
            vida_jugador -=1
            asteroides5.remove(asteroide5)
        if asteroide5.right >= WIDTH or asteroide5.left <= 0: #detecta colisión con los bordes laterales
            x5_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
        if asteroide5.bottom >= HEIGHT or asteroide5.top <= 0: #detecta colisión con el borde superior e inferior
            y5_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)

    for asteroide6 in asteroides6:
        asteroide6.x += x6_speed #movimiento en x
        asteroide6.y += y6_speed #movimiento en y
        if nave.colliderect(asteroide6): #detecta colisión con la nave
            vida_jugador = int(vida_jugador)
            vida_jugador -=1
            asteroides6.remove(asteroide6)
        if asteroide6.right >= WIDTH or asteroide6.left <= 0: #detecta colisión con los bordes laterales
            x6_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
        if asteroide6.bottom >= HEIGHT or asteroide6.top <= 0: #detecta colisión con el borde superior e inferior
            y6_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
            
#Pantalla 2
def pantalla_juego_2():
    '''
    #=============================================================================================================
    Pantalla de juego 2
    Instituto Tecnológico de Costa Rica
    Ingenieria en Computadores
    Taller de Programación
    CE-1102
    Autores: Dylan Garbanzo Fallas, Gabriel Núñez Morales
    Versión: 1.1
    Versión de python: 3.9.1
    Entradas: pantalla de inicio, pantalla de juego 1
    Salida: pantalla de inicio, pantalla de juego 3
    Restricciones: no se presentan restricciones
    '''
    global vida_jugador, puntaje, nombre_usuario, puntaje_obtenido
    #Variables para reseteo de datos cada vez que carga el nivel
    vida_jugador = 3
    vida_jugador = str(vida_jugador)
    t0 = 0
    t1 = 0
    puntaje = 0

    nave = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    pygame.mixer.music.load(os.path.join('assets2', 'sonidos', 'música_nivel_2.mp3'))
    pygame.mixer.music.play(-1)

    #Apartado de asterodies de listas de asteroides y los asteroides
    asteroides= []
    asteroide1 = pygame.Rect(posición_x(), posición_y(), Ancho_asteroide, Largo_asteroide)
    asteroides.append(asteroide1)

    asteroides2= []
    asteroide2 = pygame.Rect(posición_x(), posición_y(), Ancho_asteroide, Largo_asteroide)
    asteroides2.append(asteroide2)

    asteroides3= []
    asteroide3 = pygame.Rect(posición_x(), posición_y(), Ancho_asteroide, Largo_asteroide)
    asteroides3.append(asteroide3)

    asteroides4= []
    asteroide4 = pygame.Rect(posición_x(), posición_y(), Ancho_asteroide, Largo_asteroide)
    asteroides4.append(asteroide4)

    asteroides5= []
    asteroide5 = pygame.Rect(posición_x(), posición_y(), Ancho_asteroide, Largo_asteroide)
    asteroides5.append(asteroide5)

    asteroides6= []
    asteroide6 = pygame.Rect(posición_x(), posición_y(), Ancho_asteroide, Largo_asteroide)
    asteroides6.append(asteroide6)

    button_principal = pygame.Rect(475, 625, 250, 50) #x, y, width, lenght
    pygame.draw.rect(WIN,(133, 19, 240),button_principal) 
    

    clock = pygame.time.Clock()
    run = True
    click = False
    while run:
        #Contador
        t0 = t0 + 0.02
        t1 = int(t0)

        #Posición del mouse
        mx,my = pygame.mouse.get_pos()
        clock.tick(FPS)

        #Mensajes con información de la partida jugada
        segundos = str(t1)
        tiempo_transcurrido = HEALTH_FONT.render('Tiempo transcurrido: ' + segundos,0,(255,255,255))
        
        vida_jugador = str(vida_jugador)
        vidas_jugador_txt = HEALTH_FONT.render('Vida de '+ nombre_usuario + ': ' + vida_jugador, 0, (250,250,250))

        #Conversiones para poder cargar el puntaje
        t1 = int(t0)
        puntaje = t1 * 2
        puntaje = str(puntaje)
        puntaje_obtenido = str(puntaje_obtenido)
        if puntaje_obtenido != '0':
            mensaje_final = 'Puntaje obtenido: '+ puntaje_obtenido + ' + ' + puntaje
        else:
            mensaje_final = 'Puntaje obtenido: '+ puntaje
        puntaje_txt = HEALTH_FONT.render(mensaje_final, 0, (250,250,250))

        #detección de eventos a lo largo de la partida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            #segunda opción para salir de la partida
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                    pantalla_principal()

            #detección de click
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            #detección de colisión entre el botón y el cursero del mouse
            if button_principal.collidepoint((mx,my)):
                if click:
                    return pantalla_principal()

        #condición de finalización
        if int(vida_jugador) <= 0:
            puntaje = int(puntaje)
            puntaje_obtenido = int(puntaje_obtenido)
            puntaje_obtenido += puntaje
            puntaje = str(puntaje_obtenido)
            mensaje_final = 'Puntaje obtenido: '+ puntaje
            winner_text = 'Fin del juego :( '
            draw_winner(winner_text, mensaje_final)

        if t1 == 60:
            puntaje = int(puntaje)
            puntaje_obtenido = int(puntaje_obtenido)
            puntaje_obtenido += puntaje
            puntaje = str(puntaje_obtenido)
            mensaje_final = 'Puntaje obtenido: '+ puntaje
            winner_text = 'Nivel 2 completado, cargando siguiente nivel '
            run = False
            siguiente(winner_text, mensaje_final)
            return pantalla_juego_3()
    

        
        colisiones_2(nave, asteroide1, asteroide2, asteroide3, asteroide4, asteroide5, asteroide6, asteroides, asteroides2, asteroides3, asteroides4, asteroides5, asteroides6)
        keys_pressed = pygame.key.get_pressed()
        nave_movimiento(keys_pressed,nave)
        cargar_imágenes_2(tiempo_transcurrido, vidas_jugador_txt, puntaje_txt, nave, asteroide1, asteroide2, asteroide3, asteroide4, asteroide5, asteroide6, asteroides, asteroides2, asteroides3, asteroides4, asteroides5, asteroides6)
        
    
        
    pantalla_juego_1()



#Apartado Pantalla 3 ===========================================================================================================================================
def cargar_imágenes_3(tiempo_transcurrido, vidas_jugador_txt, puntaje_txt, nave, asteroide1, asteroide2, asteroide3, asteroide4, asteroide5, asteroide6, asteroide7, asteroide8, asteroides, asteroides2, asteroides3, asteroides4, asteroides5, asteroides6, asteroides7, asteroides8):
    #Aquí se agregan todas las imágenes constanemente a la pantalla
    WIN.blit(fondo3,(0,0)) #x, y
    WIN.blit(Nave_completa, (nave.x, nave.y)) #x, y
    WIN.blit(tiempo_transcurrido, (925,0,)) #x, y
    WIN.blit(vidas_jugador_txt, (0, 0)) #x, y
    WIN.blit(puntaje_txt, (475, 0)) #x, y

    #Botón nivel fácil ----------------------------------------------------------------------
    button_principal = pygame.Rect(475, 625, 250, 50) #x, y, width, lenght
    pygame.draw.rect(WIN,(133, 19, 240),button_principal)
    principal_txt = HEALTH_FONT.render("Pantalla Principal", 1, (250,250,250))
    WIN.blit(principal_txt, (480, 635)) #x, y 
    
    #Carga los asteroides mientras no hayan colisionado con la nave (si el asteroide no está en la lista, es eliminado)
    for asteroide1 in asteroides:
        WIN.blit(asteroide_1_completo, (asteroide1.x,asteroide1.y))
    for asteroide2 in asteroides2:
        WIN.blit(asteroide_2_completo, (asteroide2.x,asteroide2.y))
    for asteroide3 in asteroides3:
        WIN.blit(asteroide_3_completo, (asteroide3.x,asteroide3.y))
    for asteroide4 in asteroides4:
        WIN.blit(asteroide_4_completo, (asteroide4.x,asteroide4.y))
    for asteroide5 in asteroides5:
        WIN.blit(asteroide_1_completo, (asteroide5.x,asteroide5.y))
    for asteroide6 in asteroides6:
        WIN.blit(asteroide_2_completo, (asteroide6.x,asteroide6.y))
    for asteroide7 in asteroides7:
        WIN.blit(asteroide_3_completo, (asteroide7.x,asteroide7.y))
    for asteroide8 in asteroides8:
        WIN.blit(asteroide_4_completo, (asteroide8.x,asteroide8.y))


    pygame.display.update()

#Funciones que detecta colisiones y el movimiento de los asteroides
def colisiones_3(nave, asteroide1, asteroide2, asteroide3, asteroide4, asteroide5, asteroide6, asteroide7, asteroide8, asteroides, asteroides2, asteroides3, asteroides4, asteroides5, asteroides6, asteroides7, asteroides8):
    global vida_jugador, y_speed, x_speed, x2_speed, y2_speed, x3_speed, y3_speed, x4_speed, y4_speed, x5_speed, y5_speed, x6_speed, y6_speed, x7_speed, y7_speed, x8_speed, y8_speed

    for asteroide1 in asteroides:
        asteroide1.x += x_speed #movimiento en x
        asteroide1.y += y_speed #movimiento en y
        if nave.colliderect(asteroide1): #detecta colisión con la nave
            vida_jugador = int(vida_jugador)
            vida_jugador -=1
            asteroides.remove(asteroide1)   
        if asteroide1.right >= WIDTH or asteroide1.left <= 0: #detecta colisión con los bordes laterales
            x_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
        if asteroide1.bottom >= HEIGHT or asteroide1.top <= 0: #detecta colisión con el borde superior e inferior
            y_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)

    for asteroide2 in asteroides2:
        asteroide2.x += x2_speed #movimiento en x
        asteroide2.y += y2_speed #movimiento en y
        if nave.colliderect(asteroide2): #detecta colisión con la nave
            vida_jugador = int(vida_jugador) 
            vida_jugador -=1
            asteroides2.remove(asteroide2)
        if asteroide2.right >= WIDTH or asteroide2.left <= 0: #detecta colisión con los bordes laterales
            x2_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
        if asteroide2.bottom >= HEIGHT or asteroide2.top <= 0: #detecta colisión con el borde superior e inferior
            y2_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)

    for asteroide3 in asteroides3:
        asteroide3.x += x3_speed #movimiento en x
        asteroide3.y += y3_speed #movimiento en y
        if nave.colliderect(asteroide3): #detecta colisión con la nave
            vida_jugador = int(vida_jugador)
            vida_jugador -=1
            asteroides3.remove(asteroide3)
        if asteroide3.right >= WIDTH or asteroide3.left <= 0: #detecta colisión con los bordes laterales
            x3_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
        if asteroide3.bottom >= HEIGHT or asteroide3.top <= 0: #detecta colisión con el borde superior e inferior
            y3_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)

    for asteroide4 in asteroides4:
        asteroide4.x += x4_speed #movimiento en x
        asteroide4.y += y4_speed #movimiento en y
        if nave.colliderect(asteroide4): #detecta colisión con la nave
            vida_jugador = int(vida_jugador)
            vida_jugador -=1
            asteroides4.remove(asteroide4)
        if asteroide4.right >= WIDTH or asteroide4.left <= 0: #detecta colisión con los bordes laterales
            x4_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
        if asteroide4.bottom >= HEIGHT or asteroide4.top <= 0: #detecta colisión con el borde superior e inferior
            y4_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)

    for asteroide5 in asteroides5:
        asteroide5.x += x5_speed #movimiento en x
        asteroide5.y += y5_speed #movimiento en y
        if nave.colliderect(asteroide5): #detecta colisión con la nave
            vida_jugador = int(vida_jugador)
            vida_jugador -=1
            asteroides5.remove(asteroide5)
        if asteroide5.right >= WIDTH or asteroide5.left <= 0: #detecta colisión con los bordes laterales
            x5_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
        if asteroide5.bottom >= HEIGHT or asteroide5.top <= 0: #detecta colisión con el borde superior e inferior
            y5_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)

    for asteroide6 in asteroides6:
        asteroide6.x += x6_speed #movimiento en x
        asteroide6.y += y6_speed #movimiento en y
        if nave.colliderect(asteroide6): #detecta colisión con la nave
            vida_jugador = int(vida_jugador)
            vida_jugador -=1
            asteroides6.remove(asteroide6)
        if asteroide6.right >= WIDTH or asteroide6.left <= 0: #detecta colisión con los bordes laterales
            x6_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
        if asteroide6.bottom >= HEIGHT or asteroide6.top <= 0: #detecta colisión con el borde superior e inferior
            y6_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
    
    for asteroide7 in asteroides7:
        asteroide7.x += x7_speed #movimiento en x
        asteroide7.y += y7_speed #movimiento en y
        if nave.colliderect(asteroide7): #detecta colisión con la nave
            vida_jugador = int(vida_jugador)
            vida_jugador -=1
            asteroides7.remove(asteroide7)
        if asteroide7.right >= WIDTH or asteroide7.left <= 0: #detecta colisión con los bordes laterales
            x7_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
        if asteroide7.bottom >= HEIGHT or asteroide7.top <= 0: #detecta colisión con el borde superior e inferior
            y7_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)

    for asteroide8 in asteroides8:
        asteroide8.x += x8_speed #movimiento en x
        asteroide8.y += y8_speed #movimiento en y
        if nave.colliderect(asteroide8): #detecta colisión con la nave
            vida_jugador = int(vida_jugador)
            vida_jugador -=1
            asteroides8.remove(asteroide8)
        if asteroide8.right >= WIDTH or asteroide8.left <= 0: #detecta colisión con los bordes laterales
            x8_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
        if asteroide8.bottom >= HEIGHT or asteroide8.top <= 0: #detecta colisión con el borde superior e inferior
            y8_speed *= -1
            impacto_sonido = pygame.mixer.Sound(os.path.join('assets2', 'sonidos', 'impacto1.mp3'))
            impacto_sonido.play()
            impacto_sonido.set_volume(0.3)
            
#Pantalla 3
def pantalla_juego_3():
    '''
    #=============================================================================================================
    Pantalla de juego 3
    Instituto Tecnológico de Costa Rica
    Ingenieria en Computadores
    Taller de Programación
    CE-1102
    Autores: Dylan Garbanzo Fallas, Gabriel Núñez Morales
    Versión: 1.1
    Versión de python: 3.9.1
    Entradas: pantalla de inicio, pantalla de juego 2
    Salida: pantalla de inicio
    Restricciones: no se presentan restricciones
    '''
    global vida_jugador, puntaje, nombre_usuario, puntaje_obtenido
    #Variables para reseteo de datos cada vez que carga el nivel
    vida_jugador = 3
    vida_jugador = str(vida_jugador)
    t0 = 0
    t1 = 0
    puntaje = 0

    nave = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    pygame.mixer.music.load(os.path.join('assets2', 'sonidos', 'música_nivel_3.mp3'))
    pygame.mixer.music.play(-1)

    #Apartado de asterodies de listas de asteroides y los asteroides
    asteroides= []
    asteroide1 = pygame.Rect(posición_x(), posición_y(), Ancho_asteroide, Largo_asteroide)
    asteroides.append(asteroide1)

    asteroides2= []
    asteroide2 = pygame.Rect(posición_x(), posición_y(), Ancho_asteroide, Largo_asteroide)
    asteroides2.append(asteroide2)

    asteroides3= []
    asteroide3 = pygame.Rect(posición_x(), posición_y(), Ancho_asteroide, Largo_asteroide)
    asteroides3.append(asteroide3)

    asteroides4= []
    asteroide4 = pygame.Rect(posición_x(), posición_y(), Ancho_asteroide, Largo_asteroide)
    asteroides4.append(asteroide4)

    asteroides5= []
    asteroide5 = pygame.Rect(posición_x(), posición_y(), Ancho_asteroide, Largo_asteroide)
    asteroides5.append(asteroide5)

    asteroides6= []
    asteroide6 = pygame.Rect(posición_x(), posición_y(), Ancho_asteroide, Largo_asteroide)
    asteroides6.append(asteroide6)

    asteroides7= []
    asteroide7 = pygame.Rect(posición_x(), posición_y(), Ancho_asteroide, Largo_asteroide)
    asteroides7.append(asteroide7)

    asteroides8= []
    asteroide8 = pygame.Rect(posición_x(), posición_y(), Ancho_asteroide, Largo_asteroide)
    asteroides8.append(asteroide8)

    button_principal = pygame.Rect(475, 625, 250, 50) #x, y, width, lenght
    pygame.draw.rect(WIN,(133, 19, 240),button_principal) 
    

    clock = pygame.time.Clock()
    run = True
    click = False
    while run:
        #Contador
        t0 = t0 + 0.02
        t1 = int(t0)

        #Posición del mouse
        mx,my = pygame.mouse.get_pos()
        clock.tick(FPS)

        #Mensajes con información de la partida jugada
        segundos = str(t1)
        tiempo_transcurrido = HEALTH_FONT.render('Tiempo transcurrido: ' + segundos,0,(255,255,255))
        
        vida_jugador = str(vida_jugador)
        vidas_jugador_txt = HEALTH_FONT.render('Vida de '+ nombre_usuario + ': ' + vida_jugador, 0, (250,250,250))

        #Conversiones para poder cargar el puntaje
        t1 = int(t0)
        puntaje = t1 * 5
        puntaje = str(puntaje)
        puntaje_obtenido = str(puntaje_obtenido)
        if puntaje_obtenido != '0':
            mensaje_final = 'Puntaje obtenido: '+ puntaje_obtenido + ' + ' + puntaje
        else:
            mensaje_final = 'Puntaje obtenido: '+ puntaje
        puntaje_txt = HEALTH_FONT.render(mensaje_final, 0, (250,250,250))

        #detección de eventos a lo largo de la partida
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            #segunda opción para salir de la partida
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                    pantalla_principal()

            #detección de click
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            #detección de colisión entre el botón y el cursero del mouse
            if button_principal.collidepoint((mx,my)):
                if click:
                    return pantalla_principal()

        #condición de finalización
        if int(vida_jugador) <= 0:
            puntaje = int(puntaje)
            puntaje_obtenido = int(puntaje_obtenido)
            puntaje_obtenido += puntaje
            puntaje = str(puntaje_obtenido)
            mensaje_final = 'Puntaje obtenido: '+ puntaje
            winner_text = 'Fin del juego :( '
            draw_winner(winner_text, mensaje_final)

        if t1 == 60:
            puntaje = int(puntaje)
            puntaje_obtenido = int(puntaje_obtenido)
            puntaje_obtenido += puntaje
            puntaje = str(puntaje_obtenido)
            mensaje_final = 'Puntaje obtenido: '+ puntaje
            winner_text = 'Fin del juego! '
            run = False
            draw_winner(winner_text, mensaje_final)

        
        colisiones_3(nave, asteroide1, asteroide2, asteroide3, asteroide4, asteroide5, asteroide6, asteroide7, asteroide8, asteroides, asteroides2, asteroides3, asteroides4, asteroides5, asteroides6, asteroides7, asteroides8)
        keys_pressed = pygame.key.get_pressed()
        nave_movimiento(keys_pressed,nave)
        cargar_imágenes_3(tiempo_transcurrido, vidas_jugador_txt, puntaje_txt, nave, asteroide1, asteroide2, asteroide3, asteroide4, asteroide5, asteroide6, asteroide7, asteroide8, asteroides, asteroides2, asteroides3, asteroides4, asteroides5, asteroides6, asteroides7, asteroides8)
        
    
        
    pantalla_juego_1()



def pantalla_principal():
    '''
    #=============================================================================================================
    Pantalla Principal
    Instituto Tecnológico de Costa Rica
    Ingenieria en Computadores
    Taller de Programación
    CE-1102
    Autores: Dylan Garbanzo Fallas, Gabriel Núñez Morales
    Versión: 1.1
    Versión de python: 3.9.1
    Entradas: pantalla about, ranking, pantalla_juego 1,2 y 3
    Salida: pantalla about, ranking, pantalla_juego 1,2 y 3
    Restricciones: no se presentan restricciones
    '''
    global puntaje, nombre_usuario, run, run2, segundos, puntaje_obtenido
    puntaje = 0
    WIN.blit(fondo_principal,(0,0))#x,y
    WIN.blit(título,(75,0))#x,y
    pygame.mixer.music.load(os.path.join('assets2', 'sonidos', 'música_menu.mp3'))
    pygame.mixer.music.play(-1)
    print(puntaje_obtenido)
    puntaje_obtenido = puntaje

    input_rect = pygame.Rect(450, 500, 0, 32)
    color_active = pygame.Color(45, 180, 237)
    color_passive = pygame.Color(20, 74, 156)
    color = color_passive
    active = False


    while run2 == True:
        mx,my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if nombre_usuario != '':
                        run = True
                        run2 = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(mx,my):
                    active = True
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE:
                        nombre_usuario = nombre_usuario [:-1]
                    else:
                        if len(nombre_usuario) <= 28:
                            nombre_usuario += event.unicode
                        else:
                            nombre_usuario = nombre_usuario
        if active:
            color = color_active
        else:
            color = color_passive 

        WIN.blit(fondo_principal,(0,0))#x,y
        WIN.blit(título,(75,0))#x,y
        pygame.draw.rect(WIN, color, input_rect, 2)
        text_surface = HEALTH_FONT.render(nombre_usuario, True, (255,255,255))
        WIN.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(300, text_surface.get_width()+10)
        escribe_nombre = HEALTH_FONT.render('Escribe tu nombre para continuar', True, (255,255,255))
        WIN.blit(escribe_nombre, (365, 360))

        pygame.display.update()
                    

    click = False
    while run == True:
        nombre_usuario.replace('\r', '')
        WIN.blit(fondo_principal,(0,0))#x,y
        WIN.blit(título,(75,0))#x,y
        mx,my = pygame.mouse.get_pos()

        #Botón nivel fácil ----------------------------------------------------------------------
        button_nivel_1 = pygame.Rect(75, 350, 250, 50) #x, y, width, lenght
        pygame.draw.rect(WIN,(133, 19, 240),button_nivel_1)
        nivel1_txt = HEALTH_FONT.render("Nivel 1", 1, (250,250,250))
        WIN.blit(nivel1_txt, (150, 360)) #x, y 

        #Botón nivel intermedio ------------------------------------------------------------------
        button_nivel_2 = pygame.Rect(475, 350, 300, 50) #x, y, width, lenght
        pygame.draw.rect(WIN,(133, 19, 240),button_nivel_2)
        nivel2_txt = HEALTH_FONT.render("Nivel 2", 1, (250,250,250))
        WIN.blit(nivel2_txt, (580, 360)) #x, y

        #Botón nivel difícil ---------------------------------------------------------------------
        button_nivel_3 = pygame.Rect(925, 350, 250, 50) #x, y, width, lenght
        pygame.draw.rect(WIN,(133, 19, 240),button_nivel_3)
        nivel3_txt = HEALTH_FONT.render("Nivel 3", 1, (250,250,250))
        WIN.blit(nivel3_txt, (1000, 360)) #x, y

        #Botón ranking ---------------------------------------------------------------------
        button_ranking = pygame.Rect(255, 525, 250, 50) #x, y, width, lenght
        pygame.draw.rect(WIN,(133, 19, 240),button_ranking)
        ranking_txt = HEALTH_FONT.render("Ranking", 1, (250,250,250))
        WIN.blit(ranking_txt, (315, 535)) #x, y

        #Botón about ---------------------------------------------------------------------
        button_about = pygame.Rect(715, 525, 250, 50) #x, y, width, lenght
        pygame.draw.rect(WIN,(133, 19, 240),button_about)
        about_txt = HEALTH_FONT.render("About", 1, (250,250,250))
        WIN.blit(about_txt, (795, 535)) #x, y


        #Detecta colisiones del puntero del mouse con los botones --------------------------------
        #Botón nivel fácil
        if button_nivel_1.collidepoint((mx,my)):
            pygame.draw.rect(WIN,(80, 0, 156),button_nivel_1)
            nivel1_txt = HEALTH_FONT.render("Dificultad: Fácil", 1, (250,250,250))
            WIN.blit(nivel1_txt, (85, 360)) #x, y
            if click:
                return pantalla_juego_1()

        #Botón nivel intermedio
        if button_nivel_2.collidepoint((mx,my)):
            pygame.draw.rect(WIN,(80, 0, 156),button_nivel_2)
            nivel2_txt = HEALTH_FONT.render("Dificultad: Intermedio", 1, (250,250,250))
            WIN.blit(nivel2_txt, (475, 360)) #x, y
            if click:
                return pantalla_juego_2()

        #Botón nivel difícil
        if button_nivel_3.collidepoint((mx,my)):
            pygame.draw.rect(WIN,(80, 0, 156),button_nivel_3)
            nivel2_txt = HEALTH_FONT.render("Dificultad: Difícil", 1, (250,250,250))
            WIN.blit(nivel2_txt, (925, 360))
            if click:
                return pantalla_juego_3()

        #Botón ranking
        if button_ranking.collidepoint((mx,my)):
            pygame.draw.rect(WIN,(80, 0, 156),button_ranking)
            ranking_txt = HEALTH_FONT.render("Ranking", 1, (250,250,250))
            WIN.blit(ranking_txt, (315, 535)) #x, y
            if click:
                return pantalla_ranking()

        #Botón about
        if button_about.collidepoint((mx,my)):
            pygame.draw.rect(WIN,(80, 0, 156),button_about)
            about_txt = HEALTH_FONT.render("About", 1, (250,250,250))
            WIN.blit(about_txt, (795, 535)) #x, y
            if click:
                return pantalla_about()

        #Detecta si se cierra la página para eliminar la pantalla y la biblioteca
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
    pantalla_principal()


def pantalla_ranking():
    '''
    #=============================================================================================================
    Pantalla Ranking
    Instituto Tecnológico de Costa Rica
    Ingenieria en Computadores
    Taller de Programación
    CE-1102
    Autores: Dylan Garbanzo Fallas, Gabriel Núñez Morales
    Versión: 1.1
    Versión de python: 3.9.1
    Entradas: Pantalla de inicio, Ranking.txt y Rankig_Nombres.txt
    Salida: Pantalla de inicio
    Restricciones: no se presentan restricciones
    '''


    WIN.blit(fondo_ranking,(0,0))#x,y
    WIN.blit(título2,(75,0))#x,y
    Ranking = open('Ranking.txt','r')
    Ranking_Nombres = open('Ranking_Nombres.txt','r')
    pygame.mixer.music.load(os.path.join('assets2', 'sonidos', 'música_ranking.mp3'))
    pygame.mixer.music.play(-1)

    #Escritura de cada posición dentro del top 10
    #Posición 1
    Lectura1 = Ranking.readline()
    Top10 = HEALTH_FONT.render(Lectura1, True, (255,255,255))
    WIN.blit(Top10, (350, 155))
    Lectura1_2 = Ranking_Nombres.readline()
    Top10_2 = HEALTH_FONT.render(Lectura1_2, True, (255,255,255))
    WIN.blit(Top10_2, (450, 155))

    #Posición 2
    Lectura2 = Ranking.readline(5)
    Top10 = HEALTH_FONT.render(Lectura2, True, (255,255,255))
    WIN.blit(Top10, (350, 210))
    Lectura2_2 = Ranking_Nombres.readline(19)
    Top10_2 = HEALTH_FONT.render(Lectura2_2, True, (255,255,255))
    WIN.blit(Top10_2, (450, 210))

    #Posición 3
    Lectura3 = Ranking.readline(10)
    Top10 = HEALTH_FONT.render(Lectura3, True, (255,255,255))
    WIN.blit(Top10, (350, 265))
    Lectura3_2 = Ranking_Nombres.readline(29)
    Top10_2 = HEALTH_FONT.render(Lectura3_2, True, (255,255,255))
    WIN.blit(Top10_2, (450, 265))

    #Posición 4
    Lectura4 = Ranking.readline(15)
    Top10 = HEALTH_FONT.render(Lectura4, True, (255,255,255))
    WIN.blit(Top10, (350, 320))
    Lectura4_2 = Ranking_Nombres.readline(39)
    Top10_2 = HEALTH_FONT.render(Lectura4_2, True, (255,255,255))
    WIN.blit(Top10_2, (450, 320))

    #Posición 5
    Lectura5 = Ranking.readline(20)
    Top10 = HEALTH_FONT.render(Lectura5, True, (255,255,255))
    WIN.blit(Top10, (350, 375))
    Lectura5_2 = Ranking_Nombres.readline(49)
    Top10_2 = HEALTH_FONT.render(Lectura5_2, True, (255,255,255))
    WIN.blit(Top10_2, (450, 375))

    #Posición 6
    Lectura6 = Ranking.readline(25)
    Top10 = HEALTH_FONT.render(Lectura6, True, (255,255,255))
    WIN.blit(Top10, (350, 430))
    Lectura6_2 = Ranking_Nombres.readline(59)
    Top10_2 = HEALTH_FONT.render(Lectura6_2, True, (255,255,255))
    WIN.blit(Top10_2, (450, 430))

    #Posición 7   
    Lectura7 = Ranking.readline(30)
    Top10 = HEALTH_FONT.render(Lectura7, True, (255,255,255))
    WIN.blit(Top10, (350, 485))
    Lectura7_2 = Ranking_Nombres.readline(69)
    Top10_2 = HEALTH_FONT.render(Lectura7_2, True, (255,255,255))
    WIN.blit(Top10_2, (450, 485))

    #Posición 8
    Lectura8 = Ranking.readline(35)
    Top10 = HEALTH_FONT.render(Lectura8, True, (255,255,255))
    WIN.blit(Top10, (350, 540))
    Lectura8_2 = Ranking_Nombres.readline(79)
    Top10_2 = HEALTH_FONT.render(Lectura8_2, True, (255,255,255))
    WIN.blit(Top10_2, (450, 540))

    #Posición 9
    Lectura9 = Ranking.readline(40)
    Top10 = HEALTH_FONT.render(Lectura9, True, (255,255,255))
    WIN.blit(Top10, (350, 595))
    Lectura9_2 = Ranking_Nombres.readline(89)
    Top10_2 = HEALTH_FONT.render(Lectura9_2, True, (255,255,255))
    WIN.blit(Top10_2, (450, 595))

    #Posición 10
    Lectura10 = Ranking.readline(45)
    Top10 = HEALTH_FONT.render(Lectura10, True, (255,255,255))
    WIN.blit(Top10, (350, 650))
    Lectura10_2 = Ranking_Nombres.readline(99)
    Top10_2 = HEALTH_FONT.render(Lectura10_2, True, (255,255,255))
    WIN.blit(Top10_2, (450, 650))

    Ranking.close()

    #Botón pantalla_principal ---------------------------------------------------------------------
    button_principal = pygame.Rect(900, 345, 250, 50) #x, y, width, lenght
    pygame.draw.rect(WIN,(133, 19, 240),button_principal) 

    run = True
    click = False
    while run == True:
        mx,my = pygame.mouse.get_pos()
        #Botón pantalla_principal ---------------------------------------------------------------------
        button_principal = pygame.Rect(900, 345, 250, 50) #x, y, width, lenght
        pygame.draw.rect(WIN,(133, 19, 240),button_principal) 
        principal_txt = HEALTH_FONT.render("Pantalla Principal", 1, (250,250,250))
        WIN.blit(principal_txt, (900, 350)) #x, y 

        #detección de colisión entre el botón y el cursero del mouse
        if button_principal.collidepoint((mx,my)):
            pygame.draw.rect(WIN,(80, 0, 156),button_principal)
            nivel1_txt = HEALTH_FONT.render("Pantalla Principal", 1, (250,250,250))
            WIN.blit(nivel1_txt, (900, 350)) #x, y 
            if click:
                return pantalla_principal()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                    return pantalla_principal()
            #detección de click
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
    pantalla_ranking()


def pantalla_about():
    '''
    #=============================================================================================================
    Pantalla About
    Instituto Tecnológico de Costa Rica
    Ingenieria en Computadores
    Taller de Programación
    CE-1102
    Autores: Dylan Garbanzo Fallas, Gabriel Núñez Morales
    Versión: 1.1
    Versión de python: 3.9.1
    Entradas: pantalla de inicio
    Salida: pantalla de inicio
    Restricciones: no se presentan restricciones
    '''

    WIN.blit(fondo_about,(0,0))#x,y
    nombre1 = HEALTH_FONT.render('Dylan G', True, (255,255,255))
    WIN.blit(nombre1, (1075, 100))
    WIN.blit(foto_Dylan,(1050,150))#x,y
    nombre2 = HEALTH_FONT.render('Gabriel J', True, (255,255,255))
    WIN.blit(nombre2, (835, 100))
    WIN.blit(foto_Gabriel,(800,150))#x,y
    pygame.mixer.music.load(os.path.join('assets2', 'sonidos', 'música_about.mp3'))
    pygame.mixer.music.play(-1)


    pais = HEALTH_FONT.render('Costa Rica', True, (255,255,255))
    WIN.blit(pais, (55, 155))
    universidad = HEALTH_FONT.render('Tecnológico de Costa Rica', True, (255,255,255))
    WIN.blit(universidad, (55, 210))
    carrera = HEALTH_FONT.render('Ingeniería en Computadores', True, (255,255,255))
    WIN.blit(carrera, (55, 265))
    asignatura = HEALTH_FONT.render('Taller de programación, 2021, grupo 02', True, (255,255,255))
    WIN.blit(asignatura, (55, 320))
    profe = HEALTH_FONT.render('Milton Villegas Lemus', True, (255,255,255))
    WIN.blit(profe, (55, 375))
    versión = HEALTH_FONT.render('Versión 1.1', True, (255,255,255))
    WIN.blit(versión, (55, 430))
    autores = HEALTH_FONT.render('Dylan Gerardo Garbanzo Fallas y Gabriel Julián Núñez Morales', True, (255,255,255))
    WIN.blit(autores, (55, 485))
    autores_modificados = HEALTH_FONT.render('Autores de módulos modificados: Tech With Tim y DaFluffyPotato ', True, (255,255,255))
    WIN.blit(autores_modificados, (55, 540))



    run = True
    click = False
    while run == True:
        mx,my = pygame.mouse.get_pos()
        #Botón pantalla_principal ---------------------------------------------------------------------
        button_principal = pygame.Rect(55, 595, 250, 50) #x, y, width, lenght
        pygame.draw.rect(WIN,(133, 19, 240),button_principal) 
        principal_txt = HEALTH_FONT.render("Pantalla Principal", 1, (250,250,250))
        WIN.blit(principal_txt, (55, 595)) #x, y 

        #detección de colisión entre el botón y el cursero del mouse
        if button_principal.collidepoint((mx,my)):
            pygame.draw.rect(WIN,(80, 0, 156),button_principal)
            nivel1_txt = HEALTH_FONT.render("Pantalla Principal", 1, (250,250,250))
            WIN.blit(nivel1_txt, (55, 595)) #x, y 
            if click:
                return pantalla_principal()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                    return pantalla_principal()
            #detección de click
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
    pantalla_about()

def mi_auto_doc():
    with open('Readme.txt', 'w') as file:
        texto = ('"Beyond the Stars"\n'
                'Un juego hecho en Python 3.9.1\n'
                'El juego consta de 3 niveles de una duración de un minuto cada uno\n'
                'Para poder obtener puntos, el jugador tiene que esquivar los asteroides de\n'
                'Entre más difícil la dificultad, habrá mayor cantidad de asteroides de\n'
                'Pero el jugador ganará un mayor puntaje\n'
                + (pantalla_principal.__doc__)
                + (pantalla_ranking.__doc__)
                + (pantalla_about.__doc__)
                + (pantalla_juego_1.__doc__)
                + (pantalla_juego_2.__doc__)
                + (pantalla_juego_3.__doc__))
        file.write(texto)

if __name__ == "__main__":
    mi_auto_doc()
    pantalla_principal()

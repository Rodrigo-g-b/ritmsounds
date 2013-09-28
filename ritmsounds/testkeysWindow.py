#!/usr/bin/python
# -*- coding: latin-1 -*-
import juego
import pygame
from pygame.locals import *
import escritor

def startWindow( width, height):
    res = (width,height)
    pygame.init()
    pygame.display.set_caption("modo prueba de teclas")
    pantalla = pygame.display.set_mode(res)
    escritor.flog("iniciado modo de prueba")
    teclas = {}
    teclas[K_a] = 0
    teclas[K_s] = 1
    teclas[K_z] = 2
    teclas[K_x] = 3
    reloj = pygame.time.Clock()
    end = False
    pantalla.fill((134,230,120))
    letras = pygame.font.Font(None, 14)
    mensaje = "precione las teclas a, s, z y x para o�r los sonidos a los que corresponden."
    mensaje2 = "Precione escape para retornar al men�"
    msj1 = letras.render(mensaje,1,(255,255,255), (100,100,100))
    msj2 = letras.render(mensaje2,1,(255,255,255))
    
    pantalla.blit(msj1, (50,10))
    pantalla.blit(msj2,(50,60))
    pygame.display.flip()
    


    while (not end):
        reloj.tick(60)
        for event in pygame.event.get():
            if (event.type == pygame.quit):
                pygame.display.quit()
                end=True
                escritor.flog("cierre modo prueba por evento de salida")
            elif (event.type == pygame.KEYDOWN):
                if event.key == K_s or event.key == K_a or event.key == K_x or event.key == K_z:
                    juego.hitEvent(teclas[event.key])
                    escritor.flog("precionada la tecla n�mero " + str(teclas[event.key]))

                elif(event.key == K_ESCAPE):
                    pygame.display.quit()
                    escritor.flog("cierre por escape")
                    end=True


















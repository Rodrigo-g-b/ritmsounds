#!/usr/bin/python
# -*- coding: latin-1 -*-
import pygame as pg
import juego
import song
import eventos
import escritor
from pygame.locals import *
import soundevents
import testkeysWindow
import recordWindow
import playWindow



screen_width = 640
screen_height =480
songs_dir = "sfx\\"

def menu():
    option = ""
    print ("bienvenido a la primera verci�n de ritmsounds! \n Veamos si eres capaz de seguir el ritmo s�lo oyendo las indicaciones")

    while (option != "0"):
        print ("men� principal: �qu� deseas hacer? \n escribe 0 para salir \n escribe 1 para probar las teclas y conocer los sonidos asociados \n 2 para jugar una canci�n \n 3 para grabar tu propia secuencia de pasos para una canci�n")
        option = raw_input()
        if option == "1":
            testkeysWindow.startWindow(screen_width, screen_height)




if(__name__ == "__main__"):
    menu()
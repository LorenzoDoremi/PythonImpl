from tokenize import String
from PIL import Image
from numpy import size
from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import sin
import pygame
import numpy


# questo codice, mal programmato, applica l'effetto gradient map di Photoshop.


def rgbtohex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'


def rgbtohexA(color):
    return f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'



im = Image.open('./immagini/girl.jpg')
width, height = im.size

pixel_values = list(im.getdata())

pix_gen = [x for x in pixel_values]


            

window = Tk()

pygame.init()
pygame.display.set_caption('Hello World!')
canvas = pygame.display.set_mode((width, height))

for x in range(0, width):
    for y in range(0, height):
     
       
        
        canvas.set_at((x, y), x+y)
      
        







while True: # main game loop

    for event in pygame.event.get():
      ""
    pygame.display.update()

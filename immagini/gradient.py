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

def mix(gradient, power,  max):

    r,g,b = 0,0,0
    step = max/(len(gradient)-1)

    #per ciascuna gradazione di intensità (0-255)
    for j in range(0,power):

      c_r, c_g, c_b = 0,0,0
      # per ciascun colore del gradiente
      for i in range(0,len(gradient)):
        # i*step = 0, 127, 255
        c_r += gradient[i][0]*
        c_g += gradient[i][1]
        c_b += gradient[i][2]
      
      r+= c_r/len(gradient)
      g+= c_g/len(gradient)
      b+= c_b/len(gradient)

      print(int(r/max))
      print(int(g/max))
      print(int(b/max))



    return [int(r/max), int(g/max), int(b/max)]


im = Image.open('Images/girl.jpg')
width, height = im.size

pixel_values = list(im.getdata())

pix_gen = [x for x in pixel_values]
gradient = (
    [155, 0, 155],
    [0, 200, 255],
    [255, 255, 55]
)


window = Tk()
canvas = Canvas(window, width=width, height=height, bg="#000000")
canvas.pack()
img = PhotoImage(width=width, height=height)
canvas.create_image((width/2, height/2), image=img, state="normal")


mapped = numpy.array([rgbtohexA(mix(gradient, ratio, 255)) for ratio in range(0,255)])


lastt = 0;
bitmap = []

pygame.init()
pygame.display.set_caption('Hello World!')
DISPLAYSURF = pygame.display.set_mode((width, height))

for x in range(0, width):
    for y in range(0, height):
     
        w = int(sum(pixel_values[y*width + x])/3)
       
        DISPLAYSURF.set_at((x, y), mapped[w])
        total = int((((width*x + y)/(width*height)))*100)
        if(lastt != total):
          print(str(total)+"%")
          lastt = total
        







while True: # main game loop

    for event in pygame.event.get():
      ""
    pygame.display.update()

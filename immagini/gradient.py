from PIL import Image
from numpy import size
from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import sin
import pygame as pygame



# questo codice, mal programmato, applica l'effetto gradient map di Photoshop.



# funzione che rimappa un numero in nuovo intervallo
def remap(n,in1,fin1,in2,fin2):
   
    left = (n-in1)*(in2-fin2)/(in1-fin1)
    return in2+left

# funzioni di supporto non utilizzate 
def rgbtohex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'


# funzioni di supporto non utilizzate 
def rgbtohexA(color):
    return f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'



im = Image.open('immagini/under/girl.jpg')
width, height = im.size

pixel_values = list(im.getdata())

# due colori RGB (c1 sostituisce lo scuro, c2 il chiaro )
c1 = (40,0,0)
c2 = (180,40,16)
pix_gen = []
for p in pixel_values: 
    #non il modo migliore, ma funziona. (le tinte vengono percepite in maniera diversa dall'occhio)
    brightness = sum(p)/3
    color_1 = remap(brightness,0,255,c1[0],c2[0])
    color_2 = remap(brightness,0,255,c1[1],c2[1])    
    color_3 = remap(brightness,0,255,c1[2],c2[2])  
    pix_gen.append((color_1,color_2,color_3))      

            

window = Tk()

pygame.init()
pygame.display.set_caption('Hello World!')
canvas = pygame.display.set_mode((width, height))

for x in range(0, width):
    for y in range(0, height):
     
       
        
        canvas.set_at((x, y), pix_gen[y*width + x])
      
        





start = True

while True : # main game loop

    for event in pygame.event.get():
      ""
    if(start):
        pygame.display.update()
        start = False

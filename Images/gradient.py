from tokenize import String
from PIL import Image
from numpy import size
from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import sin


# questo codice, mal programmato, applica l'effetto gradient map di Photoshop. Perchè è mal programmato?


def rgbtohex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'


def rgbtohexA(color):
    return f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}'

def mix(color1, color2, ratio, max):

    r = color1[0]*(max-ratio) + color2[0]*(ratio)
    g = color1[1]*(max-ratio) + color2[1]*(ratio)
    b = color1[2]*(max-ratio) + color2[2]*(ratio)
    return [int(r/max), int(g/max), int(b/max)]


im = Image.open('Images/girl.jpg')
width, height = im.size

pixel_values = list(im.getdata())

gradient = (
    [0, 0, 0],
    [255, 255, 255]
)


window = Tk()
canvas = Canvas(window, width=width, height=height, bg="#000000")
canvas.pack()
img = PhotoImage(width=width, height=height)
canvas.create_image((width/2, height/2), image=img, state="normal")


mapped = [rgbtohexA(mix(gradient[0], gradient[1], ratio, 255)) for ratio in range(0,255)]


for x in range(0, width):
    for y in range(0, height):
     
        w = int(sum(pixel_values[y*width + x])/3)
        img.put(mapped[w], (x, y))
        

mainloop()

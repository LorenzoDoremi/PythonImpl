# init tk
import tkinter
from random import random

import numpy

root = tkinter.Tk()


data = []
for i in range(0, 100):
    data.append(random()*800)

#sistema che crea linee di sfondo
def lines(canvas: tkinter.Canvas, width, height, n, max):
    for i in range(1, n+1):
        canvas.create_line(0, i*height/n, width, i*height/n, fill='#EEEEEE')
        canvas.create_text(10, i*height/n - 10, text=int(max - i*(max/n)))


def simpleArrayPlot(myCanvas : tkinter.Canvas, data):
    # creo un sommario di dati
    summary = []
    currs = 0

    for j in range(0, len(data)):

        if j != 0 and j % 10 == 0 or j == len(data)-1:
            summary.append(currs/10)
            currs = 0
        else:
            currs += data[j]
    max = numpy.max(summary)
    
    # tengo in memoria il punto precedente per collegare
    lastx = 0
    lasty = 0
    # creo lo sfondo
    lines(myCanvas, width, height/2, 10, max*1.5)

    for i in range(0, len(summary)):
        # posizione iniziale
       
        x = 100+i*(width-100)/len(summary)

        # calcolo l'altezza relativa dei punti
        mapped = (summary[i]/(max*1.5))*(height/2)
        y = height/2 - mapped
        if i > 0:
            myCanvas.create_line(lastx, lasty, x, y, fill="blue")

        myCanvas.create_oval(x-7, y-7, x+7, y+7, fill="blue", activefill="red")
        myCanvas.create_text(x, y-20, text=int(summary[i]))
       
        lastx = x
        lasty = y

    myCanvas.create_text(50, height/2+50, text='MAX = '+str(int(numpy.max(summary))),)
    myCanvas.create_text(50, height/2+100, text='MEDIA = '+str(int(numpy.average(summary))),)







# create canvas
width = 1200
height = 800
myCanvas = tkinter.Canvas(root, bg="white", height=height, width=width)
simpleArrayPlot(myCanvas, data)


# add to window and show
myCanvas.pack()
root.mainloop()

from tokenize import String
from PIL import Image
import tkinter

from numpy import size

#questo codice trasforma un'immagine in ASCII


im = Image.open('immagini/under/girl.jpg')
width, height = im.size

pixel_values = list(im.getdata())



# init tk
root = tkinter.Tk()

# create canvas
myCanvas = tkinter.Canvas(root, bg="black", height=height, width=width)

weights = ["", "-", "o", "x", "X"]
i = 0
sieve = 8
for x in range(0,width,sieve):
 for y in range(0,height,sieve):
   w = weights[
     min(
       int(
         (
           (sum(pixel_values[y*width + x])/3)*len(weights))/255), 
           len(weights)-1)]
   myCanvas.create_text(x, y,
                         fill="#ffffff", text=w, font=('Arial',sieve))

# add to window and show
myCanvas.pack()
root.mainloop()

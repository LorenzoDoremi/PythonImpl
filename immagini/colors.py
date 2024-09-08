from tokenize import String
from PIL import Image
import tkinter


# vectorial distance between two colors
def coldist(col1, col2):

    return abs((col1[0] - col2[0]) + (col1[1] - col2[1]) + (col1[2] - col2[2]))

# relational average between two colors


def colAvg(col1, col2, strength):
    return [(col1[0]*strength + col2[0]*(100-strength)) / 100, (col1[1]*strength + col2[1]*(100-strength)) / 100, (col1[2]*strength + col2[2]*(100-strength)) / 100]


im = Image.open('immagini/under/girl.jpg')
width, height = im.size
bucketsNum = 70
buckets = []
occs = []
pixel_values = list(im.getdata())

# creo i bucket randomici
i = int(0)
while i < len(pixel_values):

    buckets.append(
        [pixel_values[i][0],
         pixel_values[i][1],
         pixel_values[i][2],
         0])

    i += int((len(pixel_values)/bucketsNum))
    occs.append(0)


# ciclo tutti i pixel
k = int(0)
while k < len(pixel_values):
    dist = 10000
    index = 0
    j = 0
    for j in range(len(buckets)):

        currd = coldist(buckets[j], pixel_values[k])

        if currd < dist:
            dist = currd
            index = j

        buckets[index][3] += 1

    k += 1000


def rgbtohex(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'


# init tk
root = tkinter.Tk()

# create canvas
width = 1200
height = 500
myCanvas = tkinter.Canvas(root, bg="white", height=height, width=width)


for x in range(len(buckets)):

    color = rgbtohex(r=int(buckets[x][0]), g=int(
        buckets[x][1]), b=int(buckets[x][2]))
    myCanvas.create_rectangle(x*width/bucketsNum, 0, x*width/bucketsNum + width/bucketsNum, height,
                              fill=color)

for x in range(len(buckets)):

    myCanvas.create_text(x*width/bucketsNum + 20, 100,
                         fill="#ffffff", text=buckets[x][3])

# add to window and show
myCanvas.pack()
root.mainloop()

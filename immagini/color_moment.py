
from tokenize import String
from PIL import Image
import tkinter
import numpy
import pygame as pygame
from numpy import size, sqrt

# questo codice trasforma un'immagine in ASCII
def remap(v,min,max,new_min,new_max):
    
    old_range = max-min
    new_range = new_max-new_min

    inc = v/old_range
    
    return new_min + (new_range)*inc





# chiamabile su vettori di pari lunghezza N. 
# calcola la distanza cartesiana tra due vettori a N dimensioni.
def vector_distance(a1,a2):

    distance = 0
    for i in range(0,len(a1)):
        distance += (a1[i]-a2[i])**2
    
    return sqrt(distance)



# sieve è un valore per cui divido il numero di interazioni. sieve = 10, controllo un decimo dei pixel
def get_moments(image: Image, sieve):

    width, height = image.size
    pixel_values = list(image.getdata())
    mean_r, mean_g, mean_b = 0,0,0
    dev_r, dev_g, dev_b = 0,0,0
    skew_r, skew_g, skew_b, skew_bri = 0,0,0,0

    # calcolo la media per i valori rgb
    for y in range(0, height, sieve):
        for x in range(0, width, sieve):

            mean_r += pixel_values[y*width + x][0]
            mean_g += pixel_values[y*width + x][1]
            mean_b += pixel_values[y*width + x][2]


    mean_r /= ((width*height)/sieve)
    mean_g /= ((width*height)/sieve)
    mean_b /= ((width*height)/sieve)
    # calcolo la deviazione standard e skewness per i valori rgb
    for y in range(0, height, sieve):
        for x in range(0, width, sieve):

            dev_r += (pixel_values[y*width + x][0]-mean_r)**2
            dev_g += (pixel_values[y*width + x][1]-mean_g)**2
            dev_b += (pixel_values[y*width + x][2]-mean_b)**2
            #skewness
            skew_r += (pixel_values[y*width + x][0]-mean_r)**3
            skew_g += (pixel_values[y*width + x][1]-mean_g)**3
            skew_b += (pixel_values[y*width + x][2]-mean_b)**3
            #brightness
            skew_bri += (sum(pixel_values[y*width + x])-(mean_r+mean_g+mean_b))**3

    dev_r = sqrt(dev_r/((width*height)/sieve))
    dev_g = sqrt(dev_g/((width*height)/sieve))
    dev_b = sqrt(dev_b/((width*height)/sieve))
    #skewness
    skew_r = (skew_r/((width*height)/sieve))**(1/3)
    skew_g = (skew_g/((width*height)/sieve))**(1/3)
    skew_b = (skew_b/((width*height)/sieve))**(1/3)
    # brightness skewness
    skew_bri = (skew_bri/((width*height)/sieve))**(1/3)
   
    
    mean = [mean_r, mean_g, mean_b]
    dev = [dev_r, dev_g, dev_b]
    skew = [skew_r, skew_g, skew_b]
    return [mean, dev, skew]
    
            

#carico le immagini
im = Image.open('immagini/under/girl.jpg')
im2 = Image.open('immagini/result.png')
im3 = Image.open('immagini/img2.jpg')
im4 = Image.open('immagini/img.jpg')


width, height = im.size

#assegno ad un array per comodità       
images = [im,im2,im3,im4]

#calcolo i tre momenti colore per tutte le immagini
moments = [ get_moments(x, 32) for x in images]

#moments[0] = media, 
#moments[1] = deviazione standard
#moments[2] = skewness


moment = 3
#preparo la matrice da riempire
mean_distances = numpy.zeros((len(images), len(images)))

for i in range(0,len(mean_distances)):
    for j in range(0,len(mean_distances[i])):
         
        for mom in range(moment):
          mean_distances[i][j] += vector_distance(moments[j][mom], moments[i][mom])
        mean_distances[i][j]  = remap(mean_distances[i][j], 0 ,100, 0, 1)



print(mean_distances)



'''

pygame.init()
pygame.display.set_caption('Stars')
canvas = pygame.display.set_mode((width, height))

while True:  # main game loop

    for event in pygame.event.get():
        ""
    pygame.display.update()
'''
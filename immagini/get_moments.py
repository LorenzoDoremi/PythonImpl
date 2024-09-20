from PIL import Image
from math import sqrt
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
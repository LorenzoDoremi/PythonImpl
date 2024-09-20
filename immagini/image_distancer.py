import requests
from PIL import Image
from io import BytesIO
from get_moments import get_moments
from cosine import cosine
# utilizzo immagini dal web per analizzare i momenti colore. 
# la distanza vettoriale dei vettori momento permette di trovare immagini simili. 



image_urls = [
    "https://images.unsplash.com/photo-1518709268805-4e9042af9f23",
    "https://images.unsplash.com/photo-1494173853739-c21f58b16055",
    "https://images.pexels.com/photos/414612/pexels-photo-414612.jpeg",
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_960_720.jpg",
    "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0",
    "https://images.pexels.com/photos/158607/cairn-fog-mystical-background-158607.jpeg",
    "https://cdn.pixabay.com/photo/2016/02/19/11/23/aurora-1208203_960_720.jpg"
]

sizes = []
for url in image_urls:
    w = 0
    h = 0
    try:
        # Send a GET request to fetch the image
        response = requests.get(url)
        # Open the image using Pillow
        img = Image.open(BytesIO(response.content))
        sizes.append(get_moments(img, 10))
        
    except: 
        print("not found")
    

print(sizes)

test = sizes[0]
for i in range(1,len(sizes)):
    distance = cosine(test, sizes[i])
    print(distance)



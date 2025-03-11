# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random


generi = ["rock","jazz","metal","alternative","heavy metal","hard rock","grunge","blues","fusion","electronic"]

l = len(generi)

# genero canzoni casuali
songs = []
for i in range(0,20):
    r = int(random.uniform(1,4))
    g_list = []
    for j in range(0,r):
        g_list.append(generi[int(random.uniform(0,len(generi)))])
    songs.append({"id": i, "generi": g_list})

bests = []
song = {"id": 898, "generi": ["grunge","heavy metal","rock"]}
# confronto la canzone test con quelle generate.
for song_i in songs:
    union = set(song["generi"]) | set(song_i["generi"])
    intersection = set(song["generi"]) & set(song_i["generi"])
    jaccard = len(intersection)/len(union)
    bests.append({"s": song_i, "sim": jaccard})
# prendo le migliori 5 
bests.sort(key = lambda d: d["sim"])
# print(bests)
best_5 = bests[-5:]
print(best_5)

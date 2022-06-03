import re


profanity = [
    "sedere",
    "cacca",
    "seni",
    "chiappette",
    "nerda",
    "viga",

]
def profanityFilter(string, sub):
  
   for i in range(0,len(profanity)):
     # compilo un'espressione regolare che ignora il maiuscolo
     insensitive = re.compile(re.escape(profanity[i]), re.IGNORECASE)
     #sostituisco la
     string =  insensitive.sub(sub*len(profanity[i]), string)
   
   
   return string



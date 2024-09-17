from random import random
from english_italian_dataset import dataset
inputs = [{"on": 0, "p1": random(), "p2": random()} for _ in range(26)]

def accendi(parola):
    for lettera in parola.lower(): 
        if 'a' <= lettera <= 'z':  # Ensure only valid letters
            inputs[ord(lettera) - 97]["on"] = 1

def allena(dataset, input, learning_rate=0.01, correct_adjustment = 0.0001):
    giusto = 0
    for parola in dataset:
        accendi(parola[0])
        s1 = sum(input["on"] * input["p1"] for input in inputs)
        s2 = sum(input["on"] * input["p2"] for input in inputs)

        # Determine response
        risposta = 0 if s1 > s2 else 1
        corretto = (risposta == parola[1])
        if corretto:
            giusto += 1

       # aggiorno i pesi
        for input in inputs:
            if corretto:
                # se è corretto rinforzo un poco
                if risposta == 0:  
                    input["p1"] += correct_adjustment * input["on"]
                    input["p2"] -= correct_adjustment * input["on"]
                else:  
                    input["p1"] -= correct_adjustment * input["on"]
                    input["p2"] += correct_adjustment * input["on"]
            else:
                # se è sbagliato, aggiusto di più
                if risposta == 0: 
                    input["p1"] -= learning_rate * input["on"]
                    input["p2"] += learning_rate * input["on"]
                else:  
                    input["p1"] += learning_rate * input["on"]
                    input["p2"] -= learning_rate * input["on"]

            input["on"] = 0  # resetto i nodi
    return giusto / len(dataset)



def test(parole):
    italiano = 0
    inglese = 0
    
    for parola in parole:
        accendi(parola)
        s1 = sum(input["on"] * input["p1"] for input in inputs)
        s2 = sum(input["on"] * input["p2"] for input in inputs)

        # determino la risposta
        if s1 > s2:  
            inglese += 1
        else: 
            italiano += 1
        
        # resetto gli input
        for input in inputs:
            input["on"] = 0
    
    # proporzioni
    total = italiano + inglese
    italiano_percentage = italiano / total
    inglese_percentage = inglese / total
    if(italiano_percentage > inglese_percentage):
        print("penso sia italiano")
    else:
        print("penso sia inglese")
    return "Italiano:"+ str(italiano_percentage) +"Inglese:"+str(inglese_percentage)

# Example test phrase
frase = "cosa ne pensi dei politici?"
parole = frase.split()


for i in range(0,100):
    allena(dataset,inputs)
# Run test and print results
print(test(parole))
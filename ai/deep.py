from random import random


dataset = [
    ("the", 0),
    ("a", 0),
    ("an", 0),
    ("il", 1),
    ("lo", 1),
    ("uno", 1),
    ("un", 1),
    ("la", 1),
    ("and", 0),
    ("or", 0),
    ("but", 0),
    ("e", 1),
    ("o", 1),
    ("ma", 1),
    ("cat", 0),
    ("dog", 0),
    ("gatto", 1),
    ("fazzoletto", 1),
    ("falce", 1),
    ("elemosina", 1),
    ("elephant", 0),
    ("king", 0),
    ("reticence", 0),
    ("guerriero", 1),
    ("detrazione", 1),
    ("warrior", 0),
    ("cloud", 0),
    ("berserk", 0),
    ("vendetta", 1),
    ("fiscalita", 1),
    ("isola", 1),
    ("ratti", 1),
    ("milanese", 1),
    ("innocence", 0),
    ("limit", 0),
    ("brought", 0),
    ("demon", 0),
    ("cat", 0),
    ("dog", 0),
    ("gatto", 1),
    ("fazzoletto", 1),
    ("falce", 1),
    ("elemosina", 1),
    ("elephant", 0),
    ("king", 0),
    ("reticence", 0),
    ("guerriero", 1),
    ("detrazione", 1),
    ("warrior", 0),
    ("cloud", 0),
    ("berserk", 0),
    ("vendetta", 1),
    ("fiscalita", 1),
    ("isola", 1),
    ("ratti", 1),
    ("milanese", 1),
    ("innocence", 0),
    ("limit", 0),
    ("brought", 0),
    ("demon", 0),
    ("gatto", 1),
    ("fazzoletto", 1),
    ("falce", 1),
    ("elemosina", 1),
    ("elephant", 0),
    ("king", 0),
    ("reticence", 0),
    ("guerriero", 1),
    ("detrazione", 1),
    ("warrior", 0),
    ("cloud", 0),
    ("berserk", 0),
    ("vendetta", 1),
    ("fiscalita", 1),
    ("isola", 1),
    ("ratti", 1),
    ("milanese", 1),
    ("innocence", 0),
    ("limit", 0),
    ("brought", 0),
    ("demon", 0),
    ("cat", 0),
    ("dog", 0),
    ("gatto", 1),
    ("cane", 1),
    ("house", 0),
    ("casa", 1),
    ("tree", 0),
    ("albero", 1),
    ("book", 0),
    ("libro", 1),
    ("car", 0),
    ("macchina", 1),
    ("water", 0),
    ("acqua", 1),
    ("food", 0),
    ("cibo", 1),
    ("city", 0),
    ("città", 1),
    ("love", 0),
    ("amore", 1),
    ("school", 0),
    ("scuola", 1),
    ("sun", 0),
    ("sole", 1),
    ("moon", 0),
    ("luna", 1),
    ("star", 0),
    ("stella", 1),
    ("friend", 0),
    ("amico", 1),
    ("bread", 0),
    ("pane", 1),
    ("milk", 0),
    ("latte", 1),
    ("fish", 0),
    ("pesce", 1),
    ("sky", 0),
    ("cielo", 1),
    ("heart", 0),
    ("cuore", 1),
    ("mountain", 0),
    ("montagna", 1),
    ("river", 0),
    ("fiume", 1)

]

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
    
    return "Italiano:"+ str(italiano_percentage) +"Inglese:"+str(inglese_percentage)

# Example test phrase
frase = "benvenuti a casa mia signori. cosa ne pensate del kink dei ratti?"
parole = frase.split()

# Run test and print results
print(test(parole))
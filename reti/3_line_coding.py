# questo file mostra vari livelli di codifica in linea
import matplotlib.pyplot as plt
import random 

# genero un messaggio casuale
messaggio = [ int(random.uniform(0,2)) for i in range(0,35)]
print(messaggio)

def NRZ(dati):
    coding = [ -1 if i == 0 else 1 for i in dati ]
    return coding 
def NRZ_I(dati):
    coding = [ 1 if i == 0 else -1 for i in dati ]
    return coding 
def Manchester(dati):
    coding = [] 
    for bit in dati: 
        if bit == 0: 
         coding.append(0)
         coding.append(1)
        else: 
         coding.append(1)
         coding.append(0)
    return coding 
def PAM_4(dati):
    coding = []
    for i in range(0,len(dati)-1):
        if dati[i] == 0 and dati[i+1] == 0: 
            coding.append(-2)
        if dati[i] == 0 and dati[i+1] == 1:
            coding.append(-1)
        if dati[i] == 1 and dati[i+1] == 0:
            coding.append(1)
        if dati[i] == 1 and dati[i+1] == 1:
            coding.append(2)
    return coding 
            

# creo dei subplot (una matrice 2x2 = 4 subplot)
f, assi = plt.subplots(2,2)

# creo per comodità un asse X per ogni bit inviato 
x = [i for i in range(0,len(messaggio))]

# PRIMO PLOT
assi[0][0].plot(x, NRZ(messaggio))
assi[0][0].set_title('NRZ') 

assi[0][1].plot(x, NRZ_I(messaggio))
assi[0][1].set_title('NRZ-I') 

manc = Manchester(messaggio)
assi[1][0].plot([i for i in range(0,len(manc))], manc)
assi[1][0].set_title('Manchester') 


pam = PAM_4(messaggio)

    
assi[1][1].plot([i for i in range(0,len(pam))], pam)
assi[1][1].set_title('PAM-4') 

# aumento il padding
plt.subplots_adjust(hspace=0.5, wspace=0.3)

plt.show()
    
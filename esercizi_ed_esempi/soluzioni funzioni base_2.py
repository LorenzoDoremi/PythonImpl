# esercizio 1 
def bit_converter(bit, tipo):
    if(tipo == "byte"):
        return bit/8
    elif(tipo == "kilobyte"):
        return bit/(8*10**3)
    elif(tipo == "megabyte"):
        return bit/(8*10**6)
    elif(tipo == "gigabyte"):
        return bit/(8*10**9)
# esercizio 2 
def bit_converter_2(data, tipo):
    if(tipo == "byte"):
        return data*8
    elif(tipo == "kilobyte"):
        return data*(8*10**3)
    elif(tipo == "megabyte"):
        return data*(8*10**6)
    elif(tipo == "gigabyte"):
        return data*(8*10**9)
# esercizio 3
def temperature_conv(gradi, tipo):
    # se  ho ricevuto celsius ritorno kelvin
    if(tipo == "Celsius"):
        return gradi + 273.15
    else: 
        return gradi - 273.15
# esercizio 4
def seconds_to(secondi, tipo):
    if(tipo == "minuti"):
        return secondi/60
    elif(tipo == "ore"):
        return secondi/3600
    elif(tipo == "giorni"):
        return secondi/(3600*24)
# esercizio 5
def radianti(deg, tipo):
    # se ricevo gradi, ritorno radianti
    if(tipo == "gradi"):
        return deg*(3.14/180)
    else: 
        return deg/(3.14/180)


# esercizio 6 
from math import log10
def db_to_watt(db):
      return 10**(db/10)
def watt_to_db(watt):
      return 10*log10(watt/10)
#esercizio 7 
def richter_tnt(joule):
    # 15g = 63kj 
    # 1g = 1000*(63/15) joule 
    grammi =  joule/(1000*63/15)
    return grammi/1000
#esercizio inverso: ritorno i joule
def tnt_richter(chili):
    return chili*1000*(1000*63/15)
# esercizio 8 
def errore_assoluto(reale,atteso):
    return reale-atteso 
def errore_relativo(reale,atteso):
    return (reale - atteso)/reale
# esercizio 9 
'''
questa domanda è pressochè impossibile.
questo perché la velocità di un'auto non e 
direttamente proporzionale ai cavalli. 

tuttavia possiamo fare una stima basandoci su dati.
prendiamo un paio di auto e confrontiamo. 
auto 1 = 177cv = 230km/h
auto 2 = 55cv = 160km/h
auto 3 = 400cv = 300 km/h
tentiamo di trovare un'equazione che più o meno soddisfi questi risultati. 
'''
from math import sqrt
def max_speed(cavalli):
    # dopo un po' di tentativi!
    return 100+10*sqrt(cavalli)



# esercizio 10 
def fattoriale(n):
      if(n == 1):
          return 1
      else:
          return n*fattoriale(n-1)


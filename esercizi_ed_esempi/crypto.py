



def caesar_encode(string, key):
    
    temp = ""
    for i in range(0, len(string)):
        temp += chr(ord(string[i])+key)
    return temp
def caesar_decode(string,key):
    temp = ""
    for i in range(0, len(string)):
        temp += chr(ord(string[i])-key)
    return temp



# ESEMPIO DI CRITTOGRAFIA A FLUSSO (BANALE)
def flux_encode(string, key):

    temp = ""
    for i in range(0,len(string)):
        
        #scelgo il numero della chiave passata
        key_value = int(ord(key[i%len(key)]))
        
        #se sono al primo, crittografo la prima lettera aggiungendo semplicemente la chiave
        if i == 0:
            temp+= chr((ord(string[i])+key_value)%255)
            
           
        #se sono dopo il primo, sfrutto anche la lettera prima. 
        else: 
            
            temp+=chr((ord(string[i])+key_value+ord(string[i-1]))%255)
    return temp

def flux_decode(string, key):
    
    temp = ""
    for i in range(0,len(string)):
        
        key_value = int(ord(key[i%len(key)]))
        if i == 0:
            temp+= chr((ord(string[i])-key_value)%255)
        else: 
            # per crittografare la i-esima lettera, devo aver prima crittograffato quello i-1esima.
            temp+=chr((ord(string[i])-key_value-ord(temp[i-1]))%255)
    return temp

stringa = "Congatulations you have solved a streamed caesar code"
crypto = stringa

crypto = flux_encode(crypto, "f25346fdg7347gdf63")
print(crypto)
crypto = flux_decode(crypto, "f25346fdg7347gdf63")
print(crypto)


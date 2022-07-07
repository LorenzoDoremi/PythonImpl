# data una string multilinea, si trasformino tutte le iniziali in maiuscolo, e si tolgano gli spazi doppi

stringa = '''nel mezzo del cammin di nostra vita 
 mi ritrovai per una selva oscura'''


def multi(string):
    mod = ""
    last = " "
    for l in stringa:
    # se l'ultimo era uno spazio, non considero lo spazio successivo
     if last == " " or last == "\n":
        if l == " ":
            continue

        else:
            if 97 < ord(l) < 122:
                mod += chr(ord(l)-32)
            else:
                mod += l
    # se l'ultimo era un carattere
    else:
        mod += l
    last = l


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


def flux_encode(string, key):

    temp = ""
    for i in range(0,len(string)):
        
        key_value = int(key[i%len(key)])
        
        if i == 0:
            temp+= chr((ord(string[i])+key_value)%255)
            
           

        else: 
            
            temp+=chr((ord(string[i])+key_value+ord(string[i-1]))%255)
    return temp

def flux_decode(string, key):
    
    temp = ""
    for i in range(0,len(string)):
        
        key_value = int(key[i%len(key)])
        if i == 0:
            temp+= chr((ord(string[i])-key_value)%255)
        else: 
            temp+=chr((ord(string[i])-key_value-ord(temp[i-1]))%255)
    return temp

''' crypto = caesar_encode(stringa, 3)
print(crypto)
crypto = caesar_decode(crypto, 3)
print(crypto)
 '''

crypto = stringa

crypto = flux_encode(crypto, "2558")
print(crypto)
crypto = flux_decode(crypto, "2558")
print(crypto)

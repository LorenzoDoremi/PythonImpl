# data una string multilinea, si trasformino tutte le iniziali in maiuscolo, e si tolgano gli spazi doppi

stringa = '''Congatulations you have solved a streamed caesar code'''



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

crypto = flux_encode(crypto, "25")
print(crypto)
crypto = flux_decode(crypto, "25")
print(crypto)


''' E·ßÚ|||||Ø×îãÒ×âÚâãÎÙààäàËìèÜÈÓÔÎÆËÚÙÕ×ÕÎ '''
''' E·ßÚ|||||ÊÚëæÏÚßÝßæéËÜÝçÝçÝÎëÙËÐ×ËÉÈÝÖØÔØË '''
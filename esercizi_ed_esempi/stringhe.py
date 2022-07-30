string = "nel mezzo del cammin di nostra vita"


#cosa fa? 

# ASCII 97-122 = a-z
def multi(string):
    mod = ""
    last = " "
    for l in string:
    # se l'ultimo era uno spazio, non considero lo spazio successivo
     if last == " " or last == "\n":
        if l == " ":
            mod+="_"
            continue

        else:
            if 97 <= ord(l) <= 122:
                mod += chr(ord(l)-32)
            else:
                mod += l
     # se l'ultimo era un carattere
     else:
        mod += l
     last = l

    return mod






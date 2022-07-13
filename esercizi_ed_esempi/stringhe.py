string = "abscd"
def multi(string):
    mod = ""
    last = " "
    for l in string:
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

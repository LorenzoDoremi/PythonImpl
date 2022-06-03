# approssimazione zeri di una funzione tramite bisezione
def bisection(func, min, max, iteractions):

    a = min
    b = max
    mid = (min + max)/2
    if iteractions == 0 or func(mid) == 0:
        return mid
    else:
        if func(a)*func(mid) < 0:
            return bisection(func, a, mid, iteractions - 1)
        else:
            return bisection(func, mid, b, iteractions - 1)


# approssimazione zeri tramite corde (regula falsi)
def regulaFalsi(func, min, max, iteractions):

    a = min
    b = max
    # coefficiente angolare della retta
    coeff = (func(b) - func(a))/(b - a)
    # valore x dello zero della retta
    sec = min + abs(func(min)/coeff)

    if iteractions == 0 or func(sec) == 0:
        return sec
    else:
        if func(a)*func(sec) < 0:
            return regulaFalsi(func, a, sec, iteractions - 1)
        else:
            return regulaFalsi(func, sec, b, iteractions - 1)



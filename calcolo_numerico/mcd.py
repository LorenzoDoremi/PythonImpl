def mcd(a, b):

    while a % b != 0:

        if a-b > b:
            a = a-b
        else:
            b = a-b

        
    return b


print(mcd(13, 3))

import numpy

# come migliorare questo codice? quali problemi?


def primeNumbers(end):

    numbers = numpy.zeros(end)

    #salvo i numeri primi che trovo
    primes = [0, 1]
    for i in range(2, end):
        
        if(numbers[i] != end+1):
            primes.append(i)
       
        for j in range(i+i, end, i):
            numbers[j] = end+1

    print(primes)

# cosa è cambiato? cosa è migliorato? 
def primeNumbersFix(end):

    numbers = [True] * end

    for i in range(2, end):
        for j in range(i+i, end, i):
            numbers[j] = False

    for i in range(0, end):
        if(numbers[i]):
            print(i)



# append = occupare spazio inutilmente. ho già gli indici nell'array che corrispondono ai numeri
# numbers non mi serve a nulla e settare end+1 è uno spreco di tempo e spazio
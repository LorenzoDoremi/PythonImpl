import numpy

# come migliorare questo codice? quali problemi?


def primeNumbers(end):

    numbers = numpy.zeros(end)
    primes = [0, 1]
    for i in range(2, end):
        if(numbers[i] != end+1):
            primes.append(i)
        for j in range(i+i, end, i):
            numbers[j] = end+1

    print(primes)

# cosa è cambiato?
def primeNumbersFix(end):

    numbers = [True] * end

    for i in range(2, end):
        for j in range(i+i, end, i):
            numbers[j] = False

    for i in range(0, end):
        if(numbers[i]):
            print(i)

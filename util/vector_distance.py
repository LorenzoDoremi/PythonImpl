from math import sqrt


def vector_distance(a1,a2):
    
    distance = 0
    for i in range(0,len(a1)):
        distance += (a1[i]-a2[i])**2
    
    return sqrt(distance)

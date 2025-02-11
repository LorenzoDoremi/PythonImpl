def bubble_sort(v):
 
    for i in range(0,len(v)):
        for j in range(0,len(v)-1):
            if v[j] > v[j+1]:
                v[j],v[j+1] = v[j+1],v[j]
 
def doremi_sort(v):
    for i in range(0,len(v)):
        for j in range(i+1,len(v)):
            if v[i] > v[j]:
                v[i],v[j] = v[j],v[i]              

def selection_sort(v):
    for posizione in range(len(v)):
        val_min = v[posizione]
        pos = posizione 
        for i in range(posizione,len(v)):
            if v[i] < val_min:
                val_min = v[i]
                posizione = i 
        v[posizione],v[pos] = v[pos],v[posizione]


#merge di supporto 
def merge(v, in1, in2, end):
    s = []
    i, j = in1, in2
    while i < in2 and j <= end:  # Assicuriamoci che j arrivi fino a end
        if v[i] < v[j]:
            s.append(v[i])
            i += 1
        else:
            s.append(v[j])
            j += 1
    while i < in2:
        s.append(v[i])
        i += 1
    while j <= end:
        s.append(v[j])
        j += 1
    for k in range(len(s)):
        v[in1 + k] = s[k]
'''
v = vettore
in1 = indice della prima cella
end = indice dell'ultima cella 
'''
def merge_sort_rec(v,in1,end):
    if in1 < end: 
        mid = (in1+end) // 2
        merge_sort_rec(v,in1,mid)
        merge_sort_rec(v,mid+1,end)
        merge(v,in1,mid+1,end)
        
def merge_sort(v):
    merge_sort_rec(v,0,len(v)-1)
                     
from math import sqrt 
def bucket_sort(v):
    buckets = [[] for i in range(int(sqrt(len(v))))]
    re = max(v)/len(buckets)
    for el in v: 
        buckets[min(int(el/re),len(buckets)-1)].append(el)
    i = 0
    for bucket in buckets: 
        bubble_sort(bucket)
        for el in bucket: 
            v[i] = el 
            i+=1

def counting_sort(v):
    massimo = max(v)
    minimo = min(v)
    abaco = [0 for _ in range(0, massimo+abs(minimo)+1)]
    for elemento in v: 
        abaco[elemento+abs(minimo)] +=1
    k = 0 
    for i in range(len(abaco)): 
        for rip in range(abaco[i]):
            v[k] = i-abs(minimo)
            k+=1
            
            
            
            
        
    

vettore = [1,6,-2,8,3,-9,0,7,-4,5]
#bubble_sort(vettore)
#doremi_sort(vettore)
#selection_sort(vettore)
#merge_sort(vettore)
#bucket_sort(vettore)
counting_sort(vettore)
print(vettore)


        

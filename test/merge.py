a1 = [1,6,8,9]
a2 = [0,3,4,10]

fin = []

i = 0
j = 0

while(i < len(a1) and j < len(a2)):
    if(a1[i] < a2[j]):
        fin.append(a1[i])
        i+=1
    else:
        fin.append(a2[j])
        j+=1

while(i < len(a1)):
    fin.append(a1[i])
    i+=1
while(j < len(a2)):
    fin.append(a2[j])
    j+=1  

print(fin) 

def merge_sort(arr, inizio, fine):
    m = int((fine+inizio)/2)
    if(inizio < fine):
        
        merge_sort(arr,inizio, m)
        merge_sort(arr,m,fine)
    else:
       merge 
        
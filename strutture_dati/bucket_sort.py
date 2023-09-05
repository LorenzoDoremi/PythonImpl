from random import random
def my_sort(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

def bucket_sort(arr,l):

 bucket_n = l
 buckets = []
 for i in range(0,bucket_n):
    buckets.append([])

 m_min = min(arr)
 m_max = max(arr)
 r = m_max-m_min;
 bucket_size = r/bucket_n +1;

 for i in range(0,len(arr)):
    pos = int(arr[i]/bucket_size)
    buckets[pos].append(arr[i])


 pos = 0
 for i in range(0,len(buckets)):
    my_sort(buckets[i])
    for j in range(0,len(buckets[i])):
        arr[pos] = buckets[i][j]
        pos+=1
 return arr






arr = []

for i in range(0,100) :
    arr.append(int(random()*100))

bucket_sort(arr,5)
print(arr)




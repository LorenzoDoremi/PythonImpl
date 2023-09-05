arr = [5,4,6,8,9,1,2,3,7,100]
print(arr)
bucket_n = 5
buckets = []
for i in range(0,bucket_n):
    buckets.append([])

min = min(arr)
max = max(arr)
r = max-min;
bucket_size = r/bucket_n +1;

for i in range(0,len(arr)):
    pos = int(arr[i]/bucket_size)
    buckets[pos].append(arr[i])

print(buckets)


 
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
 
 
def merge(arr, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    t = []
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[start + i]
 
    for j in range(0, n2):
        R[j] = arr[mid + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = start     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
           # t.append(L[i])
            i += 1
            
        else:
            arr[k] = R[j]
          #  t.append(R[j])
            j += 1
            
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
       # t.append(L[i])
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
       #  t.append(R[j])
        j += 1
        k += 1

 
 
# l is for start index and r is end index of the
# sub-array of arr to be sorted






 
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
 
 
def place_merge(arr, start, mid, end):
    
    t = []
 
    i = start    
    j = mid+1    
    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
          
            t.append(arr[i])
            i += 1
            
        else:
           
            t.append(arr[j])
            j += 1
            
     
 
    while i <= mid:
      
        t.append(arr[i])
        i += 1
     
 
    while j <= end:
       
        t.append(arr[j])
        j += 1
      
   
    k = start
    for i in range(0,len(t)):
        arr[k] = t[i]
        k+=1

 
 
# l is for start index and r is end index of the
# sub-array of arr to be sorted

 
 
def mergeSort(arr, l, r):
 
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        place_merge(arr, l, m-1, r)
 
 
# Driver code to test above
arr = [12, 11, 13,2, 5, 6, 7, 9]
mergeSort(arr,0,len(arr)-1)
 
# This code is contributed by Mohit Kumra
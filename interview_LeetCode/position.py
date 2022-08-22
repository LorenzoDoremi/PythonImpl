def searchInsert(nums, target):
        
        start = 0
        end = len(nums) -1
        
        m = 0
        while start < end:
         m = (start + end ) // 2
         print(m)
         if nums[m] == target:
            return m
         else:
           if target > nums[m]:
             start = m+1
           else:
             end = m-1
         
        m = (start+end) // 2
        if target > nums[m]:
                return m+1
        else:
            return m



list = [1,3]

n = 0


a = searchInsert(list, n)
print("risultato \n")
print(a)


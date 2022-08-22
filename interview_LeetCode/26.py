class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = 1
        if len(nums) == 0:
          k = 0
        
        last = 1
        curr = nums[0]
        i = 0
        while i < len(nums):
            
            if nums[i] != curr:
              nums[last] = nums[i]
              curr = nums[i]
              last+=1
              k+=1
            i+=1
        return k
            
              
            
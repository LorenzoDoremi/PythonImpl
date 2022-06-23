class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
      l  = 0
      for i in range(0, len(s)):
        
        curr_set = set()
        curr_l = 0
        while i < len(s) and s[i] not in curr_set:
            curr_l += 1
            curr_set.add(s[i])
            i += 1
           
        
        
       
        if curr_l > l:
            l = curr_l
        
      return l
        
        
        
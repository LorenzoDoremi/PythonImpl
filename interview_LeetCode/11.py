class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max = 0
        i = 0
        j = len(height) -1
        while i < j:
          area = min(height[j], height[i]) * (j - i) 
          if area > max:
            max = area
          if height[j] > height[i]:
            i+=1
          else:
            j -= 1
                
        return max
                
        
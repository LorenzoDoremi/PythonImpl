# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def check(self, n1, n2, v):
        if n1 and n2:
            if n1.val == n2.val:
                self.check(n1.left, n2.left, v)
                self.check(n1.right, n2.right, v)
            else:
                v[0] = False
        elif n1 and not n2 or n2 and not n1:
            v[0] = False
        
        
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        k = [True]
        self.check(p,q,k)
        return k[0]
        
        
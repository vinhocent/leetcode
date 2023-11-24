# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        stack = [root]
        ans = []
        
        if root == None:
            return ans
        
        while len(stack):
            currAns = []
            
            for i in range(len(stack)):
                

                curr = stack.pop(0)
                
                currAns.append(curr.val)
                
                if curr.left:
                    stack.append(curr.left)
                if curr.right:
                    stack.append(curr.right)       
                    
                    
            
            ans.append(currAns)
            
        return ans
        
        
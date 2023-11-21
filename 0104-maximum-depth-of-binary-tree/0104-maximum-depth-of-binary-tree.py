# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root == None:
            return 0
        
        if (root.left == None and root.right == None):
            return 1
        
        leftlen = self.maxDepth(root.left)
        rightlen = self.maxDepth(root.right)
        
        maxlen = 0
        
        if leftlen >= rightlen :
            maxlen = leftlen + 1
            
        else:
            maxlen = rightlen + 1
            
        return maxlen
            
        
        
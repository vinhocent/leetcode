# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if subRoot == None:
            return True
        if root == None:
            return False
        
        if self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        
        
    def isSameTree(self,left: Optional[TreeNode],right:Optional[TreeNode]) -> bool:
        
        
        if left == None and right == None:
            return True
        
        elif left and right and left.val == right.val:
            return self.isSameTree(left.left , right.left) and self.isSameTree(left.right , right.right)
            

        return False
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inverter(root):
    
    if root == None:
        return None

    if (root.right == None and root.left == None):
        return root

    temp = root.left
    root.left = root.right
    root.right = temp

    if (root.left != None): inverter(root.left)
    if (root.right != None): inverter(root.right)
    return root
    
    
    
    
class Solution(object):
        
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return inverter(root)

        
            
            
        
        
        
        
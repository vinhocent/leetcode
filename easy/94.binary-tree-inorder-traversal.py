#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        array = []
        
        current = root
        while (current != None  or (len(stack) != 0)):
            while (current != None):
                stack.append(current)
                print(current.val)
                current = current.left
               
            current = stack.pop() # previously null
            array.append(current.val)
            current = current.right 
        
        return array
    
# @lc code=end


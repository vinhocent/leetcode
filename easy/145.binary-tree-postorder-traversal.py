#
# @lc app=leetcode id=145 lang=python
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        array = []
        if (root == None):
            return array
        
        
        stack = [root]
       
        current = root
        while (len(stack) != 0):
            current = stack.pop()
            array.append(current.val)
            if  current.left != None :    
                stack.append(current.left)
            if  current.right  != None :    
                stack.append(current.right)


        
        return array[::-1]
        
# @lc code=end


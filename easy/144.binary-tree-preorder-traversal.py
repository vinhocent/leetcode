#
# @lc app=leetcode id=144 lang=python
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # iterative solution:
        stack = [root]
        array = []
        current = root
        while (current != None  or (len(stack) != 0)):
            current = stack.pop()
            if current :    
                
                array.append(current.val)
                stack.append(current.right)
                stack.append(current.left)
        
        return array

        # recursive solution:
        # res = []
        
        # def trav(root, arr):
        #     if root:
        #         arr.append(root.val)
        #         trav(root.left, arr)
        #         trav(root.right, arr )
                         
        # trav(root, res)
        
        # return res
        
# @lc code=end


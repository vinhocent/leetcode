#
# @lc app=leetcode id=617 lang=python
#
# [617] Merge Two Binary Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """

        def merge(node1, node2):
            if node1 == None:
                return node2
            if node2 == None:
                return node1            
            node1.val += node2.val
            node1.right = merge(node1.right, node2.right)
            node1.left = merge(node1.left, node2.left)
            
            return node1
        
        
        return merge(root1, root2)
        
# @lc code=end


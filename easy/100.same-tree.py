#
# @lc app=leetcode id=100 lang=python
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def merge(node1, node2):

            
            if node1 == None and node2 == None:
                return True
                
            elif node1 == None or node2 == None:
                return False

            elif node1.val != node2.val:
                return False
            
            
            
            variable = (merge(node1.right, node2.right) and merge(node1.left, node2.left))
            return variable
        
        
        return merge(p, q)
        
# @lc code=end


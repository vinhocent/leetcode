#
# @lc app=leetcode id=1379 lang=python
#
# [1379] Find a Corresponding Node of a Binary Tree in a Clone of That Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        def traverse(o, c, t):
            if o:
                if o.val == t.val:
                    self.ans = c
            
                traverse(o.right, c.right, t)
                traverse(o.left, c.left, t)
            
            
        traverse(original, cloned, target)
        return self.ans
        
# @lc code=end


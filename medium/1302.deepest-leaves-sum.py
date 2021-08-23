#
# @lc app=leetcode id=1302 lang=python
#
# [1302] Deepest Leaves Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = 0
        summ = {}
        
        def trav(root, level, summ):
            if level in summ:
                summ[level] += root.val
            else:              
                summ[level] = root.val
            if root.left:
                trav(root.left, level+1, summ)
            if root.right:
                trav(root.right, level+1, summ)     
        trav(root, level, summ)
        return summ[max(summ.iterkeys())] 
        
# @lc code=end


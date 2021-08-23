#
# @lc app=leetcode id=1315 lang=python
#
# [1315] Sum of Nodes with Even-Valued Grandparent
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        level = 0
        
        summ = 0
        
        def trav(root, parent, gp):
            summ = 0
            if root:
                if gp != None and gp.val % 2 == 0:
                    summ += root.val
                if root.left and root.right:
                    return summ + trav(root.left, root, parent) + trav(root.right, root, parent)
                elif not root.right:
                    return summ + trav(root.left, root, parent)
                elif not root.left:
                    return summ + trav(root.right, root, parent)
            else:
                return summ
                         
        return trav(root, None, None)
        
        
# @lc code=end


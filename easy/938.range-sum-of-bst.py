#
# @lc app=leetcode id=938 lang=python
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
            
        def summup(root, low, high):
            summ = 0      
            if root:
                if low <= root.val <= high:
                    summ += root.val  
                if root.left and root.right:
                    return summ + summup(root.left, low, high) + summup(root.right, low, high)
                elif not root.right:
                    return summ + summup(root.left, low, high)
                elif not root.left:
                    return summ + summup(root.right, low, high)
            else:
                return summ
        return summup(root, low, high)
        
# @lc code=end


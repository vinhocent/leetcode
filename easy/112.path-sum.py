#
# @lc app=leetcode id=112 lang=python
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        res = []
        def trav(root, currSum ):
            if root:
                currSum += root.val
                
                if not root.left and not root.right:
                    if currSum == targetSum:
                        return True
                if trav(root.left, currSum):
                    return True
                if trav(root.right, currSum):
                    return True
                
                return False
                
                
                
        return trav(root, 0)
        
# @lc code=end


#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """      
        
        def depth(root, level):
            if root == None:
                return level - 1
            if root.left and root.right:
                return max(depth(root.left, level+1) , depth(root.right, level+1))
            elif root.left:
                return max(depth(root.left, level+1) , None)
            else:
                return max(depth(root.right, level+1) , None)
        
        return depth(root, 1)
        
# @lc code=end


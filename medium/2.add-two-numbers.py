#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        solution = ListNode(val = (l1.val + l2.val) % 10)
        carry = (l1.val + l2.val) // 10

        node = solution
        while (l1.next) and (l2.next):
            l1 = l1.next
            l2 = l2.next
            node.next  =  ListNode(val = (carry + l1.val + l2.val) % 10)
            carry = (carry + l1.val + l2.val) // 10
            node = node.next
            
        while (l1.next):
            l1 = l1.next
            node.next  =  ListNode(val = (carry + l1.val) % 10)
            carry = (carry + l1.val) // 10
            node = node.next
            
        while (l2.next):
            l2 = l2.next
            node.next  =  ListNode(val = (carry + l2.val) % 10)
            carry = (carry + l2.val) // 10
            node = node.next
            
        if (carry > 0):
            node.next = ListNode(val = 1)
            
        return solution
            
        
# @lc code=end


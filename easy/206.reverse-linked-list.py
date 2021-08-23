#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

                
        if (head == None):
            return head
        
        elif (head.next == None):

            return head
        
        p = self.reverseList(head.next)

        head.next.next = head
        
        head.next = None

            
        return p
        
# @lc code=end


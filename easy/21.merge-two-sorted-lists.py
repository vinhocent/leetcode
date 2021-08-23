#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newnode = ListNode()
        ans = newnode   
        while (l1 != None) or (l2 != None):           
            if (l1  == None):
                ans.next = l2
                break  
            elif (l2 == None):
                ans.next = l1
                break         
            elif (l1.val <= l2.val):
                ans.next = ListNode(l1.val)
                l1  = l1.next 
            else :
                ans.next = ListNode(l2.val)
                l2 = l2.next 
            ans = ans.next          
        return newnode.next
        
# @lc code=end


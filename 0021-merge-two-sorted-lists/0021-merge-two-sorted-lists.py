# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        newNode = ListNode(1)
        ans = newNode
        
        current1 = list1
        current2 = list2
        while current1 != None or current2 != None:
            if current1 == None:
                print("1")
                ans.next = current2
                break
            if current2 == None:
                print("2")
                ans.next = current1
                break
                
            if current1.val >= current2.val:
                print("dick")
                ans.next = ListNode(current2.val)
                current2 = current2.next
            else:
                ans.next = ListNode(current1.val)
                current1 = current1.next     
                
            ans = ans.next
            
        return newNode.next
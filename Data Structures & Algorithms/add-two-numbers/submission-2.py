# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        current = dummy

        while l1 or l2 or carry:
            if l1 and l2:
                value = (l1.val+l2.val+carry) % 10
                carry = (l1.val+l2.val+carry) // 10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                value = (l1.val+carry) % 10
                carry = (l1.val+carry) // 10
                l1 = l1.next
            elif l2:
                value = (l2.val+carry) % 10
                carry = (l2.val+carry) // 10
                l2 = l2.next
            else:
                value = carry
                carry = 0
            
            current.next = ListNode(value)
            current = current.next
        
        return dummy.next
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        curr = dummy.next
        prev_start = dummy

        while True:
            start = curr
            
            for _ in range(k):
                if curr is None:
                    return dummy.next
                
                curr = curr.next
        
            next_start = curr

            prev = next_start
            node = start

            while node != next_start:
                saved_next = node.next
                node.next = prev
                prev = node
                node = saved_next

            prev_start.next = prev

            prev_start = start





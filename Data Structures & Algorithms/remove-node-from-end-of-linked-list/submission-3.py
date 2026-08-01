# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # list is an easy way to do this one



        first = head

        nodes = []

        while head:
            nodes.append(head)
            head = head.next
        
        if n == len(nodes):
            return first.next
        if n == 1:
            nodes[len(nodes)-2].next = None
            return first

        index_of_interest = len(nodes)-n
        left = index_of_interest-1
        right = index_of_interest+1

        nodes[left].next = nodes[right]

        return first






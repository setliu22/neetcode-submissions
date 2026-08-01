# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        nodes = []
        front = head

        while head:
            nodes.append(head)
            head = head.next
        
        # 2, 4, 6, 8, 10

        # have two pointers at the ends move inwards
        left = 0
        right = len(nodes)-1
        
        while left < right:
            nodes[left].next = nodes[right]

            nodes[right].next = nodes[left+1]

            left += 1
            right -= 1

        nodes[(len(nodes)//2)].next = None
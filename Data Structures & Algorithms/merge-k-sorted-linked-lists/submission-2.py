# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy

        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        while heap:
            val, index, node = heapq.heappop(heap)
            print(f"{val} {index} {node}")

            current.next = ListNode(val)
            current = current.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))

        return dummy.next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Put the first node of each non-empty list into the heap.
        # The heap acts like a machine that always gives us the smallest node.
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        # Dummy node makes it easy to build the result linked list.
        dummy = ListNode(0)
        tail = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            # Add the smallest node to the result list.
            tail.next = node
            tail = tail.next

            # If this node has another node after it,
            # that next node is now a candidate to be the next smallest.
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # convert to list and do all operations in the list

        nodes = []

        starting_node = head

        while head:
            nodes.append(head)
            head = head.next
        
        n = len(nodes)
        
        # 1 2 3 4 5 6
        # 0 1 2 3 4 5

        for start in range(0, n-k+1, k): #0, 4
            node_after_curr_group = nodes[start+k-1].next

            for i in range(start+k-1, start, -1): # go backwards, stop at start

                nodes[i].next = nodes[i-1]

            # set first element next to the first element of previous group if that group getting flipped

            if start+2*k-1 < n:
                nodes[start].next = nodes[start+2*k-1]
            else:
                nodes[start].next = node_after_curr_group
            
        if n >= k:
            return nodes[k-1]
        else:
            return nodes[0]

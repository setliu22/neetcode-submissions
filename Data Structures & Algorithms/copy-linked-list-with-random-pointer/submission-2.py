"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
            
        first = head

        # nodes = []

        conv_dict = {}

        while head:
            # nodes.append(head)
            conv_dict[head] = Node(head.val)
            head = head.next
        
        head = first

        while head:
            if head.next:
                conv_dict[head].next = conv_dict[head.next]
            if head.random:
                conv_dict[head].random = conv_dict[head.random]
            head = head.next
        
        return conv_dict[first]


        # make a dict with hold nodes pointing to copied nodes

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Make a dictionary that acts like a machine:
        # give it an original node, and it gives back that node's copied version.
        # None should stay None, so random/next pointers that are None are easy to handle.
        old_to_new = {None: None}

        curr = head

        # First pass: create a copied node for every original node.
        # At this point, we are only making the nodes, not connecting them yet.
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        # Second pass: connect the copied nodes.
        # For each original node, use the dictionary machine to find
        # the copied versions of curr, curr.next, and curr.random.
        while curr:
            copy = old_to_new[curr]

            copy.next = old_to_new[curr.next]
            copy.random = old_to_new[curr.random]

            curr = curr.next

        # Return the copied version of the original head.
        return old_to_new[head]
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Dummy node handles cases where the head itself changes after reversal.
        dummy = ListNode(0, head)

        # group_prev points to the node right before the group we want to reverse.
        group_prev = dummy

        while True:
            # Find the kth node from group_prev.
            # This tells us whether there are enough nodes to reverse.
            kth = group_prev

            for _ in range(k):
                kth = kth.next

                # Fewer than k nodes remain, so leave the rest unchanged.
                if not kth:
                    return dummy.next

            # The node immediately after the current group.
            # This is where the reversed group should eventually connect.
            group_next = kth.next

            # Reverse the current group.
            # prev starts as group_next so the old first node will point to it
            # after reversal.
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # group_prev.next is the old first node of the group.
            # After reversal, it becomes the last node of the group.
            old_group_start = group_prev.next

            # kth is now the first node of the reversed group.
            group_prev.next = kth

            # Move group_prev to the end of the reversed group,
            # so the next loop starts after it.
            group_prev = old_group_start
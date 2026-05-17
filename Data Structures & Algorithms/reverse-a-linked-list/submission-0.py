class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # save the next node
            curr.next = prev     # reverse the pointer
            prev = curr          # move prev forward
            curr = nxt           # move curr forward

        return prev
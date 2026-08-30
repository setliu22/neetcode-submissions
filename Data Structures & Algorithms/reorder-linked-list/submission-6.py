class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find end of first half. second half will always be smaller than first half
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half set prev = None to completely disconnect the two
        second = slow.next
        slow.next = None

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # 3. Merge halves
        first = head
        second = prev

        while second:
            firstNext = first.next
            secondNext = second.next

            first.next = second
            second.next = firstNext

            first = firstNext
            second = secondNext
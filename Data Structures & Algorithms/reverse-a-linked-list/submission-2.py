# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        at 0, store 1, point 0 to ListNode()
        go to 1
        at 1, store 2, point 1 to 0
        go to 2
        at 2, store 3, point 2 to 1
        go to 3
        at 3, store next as None, point 3 to 2
        go to None
        stop because you are at None
        """

        prevNode = None
        node = head

        while node:
            nextNode = node.next # 1
            node.next = prevNode # 0 -> Node
            prevNode = node # prevNode is 0
            node = nextNode # node is 1

        return prevNode
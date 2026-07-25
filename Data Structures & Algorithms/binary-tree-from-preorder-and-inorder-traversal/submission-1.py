# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.index = 0

        lookupDict = {val: index for index, val in enumerate(inorder)}

        def finder(start, end):
            print(str(start) + " " + str(end))
            if start > end:
                return None
            if self.index == len(inorder):
                return None

            value = preorder[self.index]
            print(value)

            node = TreeNode(value)
            self.index += 1

            node.left = finder(start, lookupDict[value]-1)
            node.right = finder(lookupDict[value]+1, end)

            return node
            
        return finder(0, len(inorder))
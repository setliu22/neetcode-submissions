class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its position in inorder.
        # This lets us quickly find where the root is in inorder.
        inorder_index = {val: i for i, val in enumerate(inorder)}

        # This points to the next root in preorder.
        pre_i = 0

        def build(left, right):
            nonlocal pre_i

            # No nodes in this range
            if left > right:
                return None

            # Preorder gives us the current root
            root_val = preorder[pre_i]
            pre_i += 1

            root = TreeNode(root_val)

            # Find root in inorder
            mid = inorder_index[root_val]

            # Everything left of mid is the left subtree
            root.left = build(left, mid - 1)

            # Everything right of mid is the right subtree
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
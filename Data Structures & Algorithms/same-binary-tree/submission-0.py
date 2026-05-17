class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        if self.isSameTree(p.right, q.right) == False:
            return False

        if self.isSameTree(p.left, q.left) == False:
            return False

        return True
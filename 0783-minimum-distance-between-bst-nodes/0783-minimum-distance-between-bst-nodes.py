class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        self.prev: int | None = None
        self.min_diff = float("inf")

        def inorder(node: TreeNode | None) -> None:
            if not node:
                return

            inorder(node.left)

            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return int(self.min_diff)
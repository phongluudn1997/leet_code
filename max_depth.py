class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def max_depth(self, root: TreeNode):
        if root is None:
            return 0
        return 1 + max(self.max_depth(root.left), self.max_depth(root.right))

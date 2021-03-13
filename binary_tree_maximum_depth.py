class TreeNode(object):
    """docstring for TreeNode"""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


root = TreeNode(3)
root.right = TreeNode(5)
root.right.right = TreeNode(10)

print(Solution().maxDepth(root))

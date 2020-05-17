"""
link: https://leetcode.com/problems/symmetric-tree/
"""


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


class Solution:
    def is_symetric_tree(self, root: TreeNode):
        return root is None or self.is_symetric_tree_helper(root.left, root.right)

    def is_symetric_tree_helper(self, left, right):
        if left is None or right is None:
            return left == right
        if left.val != right.val:
            return False
        else:
            return self.is_symetric_tree_helper(left.left, right.right) and self.is_symetric_tree_helper(left.right, right.left)

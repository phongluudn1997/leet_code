class Solution:
    def approach_1(self, root, target_value):
        closest = root.value
        node = root
        while node is not None:
            if abs(node.value - target_value) < abs(closest - target_value):
                closest = node.value
            if node.value < target_value:
                node = node.right
            elif node.value > target_value:
                node = node.left
            else:
                break
        return closest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = BST(10)
root.left = BST(5)
root.right = BST(15)
root.right.left = BST(13)

print(Solution().approach_1(root, 13))

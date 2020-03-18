class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


list_node = ListNode([1, 2, 3, 4, 5])
solution = Solution()
solution.deleteNode(3)
while list_node:
    print(list_node.val)

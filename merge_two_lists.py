class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def show_node(self):
        while self:
            print(self.val)
            self = self.next


class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val < l2.val:
                l1.next = self.merge_two_lists(l2, l1.next)
                return l1
            else:
                l2.next = self.merge_two_lists(l2.next, l1)
                return l2
        return


l1 = ListNode(1)
l1_2 = ListNode(3)
l1_3 = ListNode(5)
l1.next = l1_2
l1_2.next = l1_3
l1.show_node()

l2 = ListNode(2)
l2_2 = ListNode(3)
l2_3 = ListNode(4)
l2.next = l2_2
l2_2.next = l2_3
l2.show_node()

l3 = Solution().merge_two_lists(l1, l2)
l3.show_node()

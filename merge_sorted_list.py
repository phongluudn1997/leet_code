# List Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self, node):
        self.head = node

    def insert_node(self, node):
        if not self.head:
            return SingleLinkedList(node)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

        return self.head

    def display(self):
        while self.head:
            print(f'{self.head.value} -> ')
            self.head = self.head.next


class Solution:
    def merge_sorted_list(self, l1, l2):
        head = SingleLinkedList(-1)
        current = head
        while l1 and l2:
            if l1.value < l2.value:
                current.next = l1
                current = current.next
                l1 = l1.next
            else:
                current.next = l2
                current = current.next
                l2 = l2.next

        if l1:
            current.next = l1

        if l2:
            current.next = l2
        return head.next

    def merge_sorted_list_2(self, l1, l2):
        if not l1:
            return l2

        if not l2:
            return l1

        if l1.value < l2.value:
            l1.next = self.merge_sorted_list_2(l1.next, l2)
            return l1

        if l2.value < l1.value:
            l2.next = self.merge_sorted_list_2(l2.next, l1)
            return l2


if __name__ == '__main__':

    a = Node(1)
    b = Node(3)
    c = Node(6)

    l1 = SingleLinkedList(a)
    l1.insert_node(b)
    l1.insert_node(c)

    d = Node(2)
    e = Node(4)
    f = Node(5)

    l2 = SingleLinkedList(d)
    l2.insert_node(e)
    l2.insert_node(f)

    merged_list = Solution().merge_sorted_list_2(a, d)

    while merged_list:
        print(merged_list.value)
        merged_list = merged_list.next

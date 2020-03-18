class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def reverse_linked_list(self):
        prev = None
        while self.head:
            current = self.head
            self.head = self.head.next
            current.next = prev
            prev = current


node_1 = Node('1')
node_2 = Node('2')
node_3 = Node('3')
linked_list = LinkedList()
linked_list.head = node_1
node_1.next = node_2
node_2.next = node_3

linked_list.print_linked_list()

a = linked_list.reverse_linked_list()
linked_list.print_linked_list()

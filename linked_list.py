class Node(object):
    nextNode: Node

    def __init__(self, value):
        self.value = value


class LinkedList(object):
    head_node: Node

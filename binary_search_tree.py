class Node:
    right = None
    left = None

    def __init__(self, data):
        self.data = data

    def insert(self, value):
        if value <= self.data:
            if not self.left:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if not self.left:
                return False
            else:
                return self.left.contains(value)
        elif value > self.data:
            if not self.right:
                return False
            else:
                return self.right.contains(value)

    def print_in_order(self):
        if not self.left:
            self.left.print_in_order()
        print(self.data)
        if not self.right:
            self.right.print_in_order()


def factorials(n):
    if n == 0:
        return 1
    return n * factorials(n - 1)


a = factorials(3)
print(a)

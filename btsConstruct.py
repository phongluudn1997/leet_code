class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(N)) time | O(1) space
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    # Average: O(log(N)) time | O(1) space
    # Worse: O(N) time | O(1) space
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if currentNode.value == value:
                return True
            elif currentNode.value < value:
                currentNode = currentNode.right
            else:
                currentNode = currentNode.left
        return False

    def remove(self, value):
        """
            @STRATEGY:
            - Replace the potential deleted node with the smallest node of its right sub tree.

            @TODO:
            - Find the node needs to be deleted.
            - 4 cases:
                - node doesn't have left or right -> replace with None
                - node only has left subtree -> replace with the left subtree.
                - node only has right subtree -> replace with the right subtree.
                - node has both left and right -> replace the value with the value of minimum node in the right subtree, delete the minimum node.

        """
        currentNode = self
        parentNode = None
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is None and currentNode.right is None:
                    parentNode.replaceChild(currentNode, None)
                    break
                elif currentNode.left and currentNode.right:
                    minNode = self.right.findMin()
                    currentNode.value = minNode.value
                    currentNode.right.removeNode(currentNode.value)
                    break
                elif currentNode.left:
                    parentNode.replaceChilde(currentNode, currentNode.left)
                    break
                else:
                    parentNode.replaceChild(currentNode, currentNode.right)
                    break
        return self

    def printInOrder(self):
        if self.left:
            self.left.printInOrder()
        print(self.value)
        if self.right:
            self.right.printInOrder()

    def getNodeWithValue(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return currentNode
        return None

    def findMin(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode

    def replaceChild(self, childNode, replacement):
        """
            @params: replacement: type BST || None
        """
        if not self.left and not self.right:
            print('No child to replace.')
        elif childNode.value < self.value:
            self.left = replacement
        else:
            self.right = replacement


# O(n) time | O(n) space
def inOrderTraverse(tree, array=[]):
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array

# O(n) time | O(n) space


def preOrderTraverse(tree, array=[]):
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array

# O(n) time | O(n) space


def postOrderTraverse(tree, array=[]):
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array


def isValidBST(self):
    def validBSTHelper(node, minValue, maxValue):
        if not node.left and not node.right:
            return True
        elif node.value < minValue or node.value >= maxValue:
            return False
        else:
            return validBSTHelper(node.left, minValue, node.value) and validBSTHelper(node.right, node.value, maxValue)
    return validBSTHelper(self, float("-inf"), float("inf"))


# O(nlog(n)) time | O(n) space
def minHeightBST(array):
    return constructMinHeight(array, 0, len(array) - 1)


def constructMinHeight(array, startIdx, endIdx):
    if endIdx < startIdx:
        return None
    midIdx = (endIdx - startIdx) // 2
    midVal = array[midIdx]
    bst = BST(midVal)
    bst.left = constructMinHeight(array, 0, midIdx - 1)
    bst.right = constructMinHeight(array, midIdx + 1, endIdx)
    return bst


def invertBst(bst):
    queue = [bst]
    while len(queue):
        current = queue.pop()
        if current is None:
            continue
        current.left, current.right = current.right, current.left
        queue.append(current.left)
        queue.append(current.right)


if __name__ == "__main__":
    bst = BST(10)
    bst.insert(5)
    bst.insert(12)
    bst.insert(9)
    print(inOrderTraverse(bst))

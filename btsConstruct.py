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
                if currentNode.left == None:
                    currentNode.left = BST(value) 
                    break
                else:
                     currentNode = currentNode.left
            else:
                if currentNode.right == None:
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
        def getReplacement(currentNode):
            if currentNode.left is None and currentNode.right is None:
                return None                
            elif currentNode.left is not None and currentNode.right is not None:
                minNode = findMin(currentNode.right)
                currentNode.value = minNode.value
                currentNode.right.remove(currentNode.value)
            elif currentNode.left is not None:
                return currentNode.left
            else:
                return currentNode.right
        
        def findMin(currentNode):
            while currentNode.left is not None:
                currentNode = currentNode.left
            return currentNode

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
                if currentNode.value < parentNode.value:
                    parentNode.left = getReplacement(currentNode)
                else:
                    parentNode.right = getReplacement(currentNode)
        return self

if __name__ == "__main__":
    bst = BST(10)    
    bst.insert(11)
    bst.insert(12)
    bst.remove(12)

class Node:
    """Represent a node of a binary tree"""
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def getNodeValue(self):
        if self.value != None:
            return self.value


    def insert(self, value):
        """Insert a new node with data"""
        if self.value:
            if value < self.value:
                if self.left == None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right == None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
            #no value = self.value condition
        else:
            self.value = value

    def lookup(self, value, parent=None):
        """Look up node with a value"""
        if self.value:
            if value < self.value:
                if self.left == None:
                    return None, None
                return self.left.lookup(value, self)
            elif value > self.value:
                if self.right == None:
                    return None, None
                return self.right.lookup(value, self)
            else:
                return self, parent
        else:
            return None, None

    def children_count(self):
        """return the number of children, 0, 1, 2"""
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def delete(self, value):
        


def getValue(node):
    if node != None:
        return node.getNodeValue()
    else:
        return None

def printList(node):
    if node != None:
        printList(node.getLeftChild())
        print (node.getNodeValue())
        printList(node.getRightChild())


def testTree():
    myTree = Node(9)
    myTree.insert(19)
    myTree.insert(7)
    myTree.insert(6)
    myTree.insert(3)
    myTree.insert(4)
    myTree.insert(11)
    myTree.insert(8)
    myTree.insert(10)
    printList(myTree)
    node, parent = myTree.lookup(10)
    print (getValue(node), getValue(parent))
    node1, parent1 = myTree.lookup(18)
    print (getValue(node1), getValue(parent1))



testTree()


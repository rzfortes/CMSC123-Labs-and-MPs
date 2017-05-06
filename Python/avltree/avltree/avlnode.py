class AVLTreeNode:

    def __init__(self, key, value, parent=None, left=None, right=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.height = None
        self.balance = None
        self.child = None
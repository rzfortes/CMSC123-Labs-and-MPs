from bstnode import BinarySearchTreeNode


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, key, value):
        new_node = BinarySearchTreeNode(key, value, None, None, None)
        if self.root == None:
            self.root = new_node
            inserted_node = self.root
        else:
            current = self.root
            prev = None
            while current != None:
                prev = current
                if key < current.key:
                    current = current.left
                else:
                    current = current.right
            if key < prev.key:
                prev.left = new_node
                inserted_node = prev.left
            else:
                prev.right = new_node
                inserted_node = prev.right
            new_node.parent = prev

        return inserted_node
        pass

    def delete(self, key):
        current = self.root
        child = 0 #ctr for children
        while current != None:
            if key == current.key:
                break;
            elif key < current.key:
                current = current.left
                child = -1
            else:
                current = current.right
                child = 1
        if current == None:
            return None
        else:
            delete = None
            temp_parent = current.parent
            if current.left == None and current.right == None:
                delete = current
                delete.parent = None
                if child == 1:
                    temp_parent.right = None
                elif child == -1:
                    temp_parent.left = None
                elif child == 0:
                    self.root == None
                delete.parent = None
                delete.right = None
                return delete
            else:
                delete = current
                delete.parent = None
                if current.right == None:
                    temp_left = current.left
                    temp_left.parent = temp_parent
                    if current == self.root:
                        self.root = temp_left
                    else:
                        if child == 1:
                            temp_parent.right = temp_left
                        elif child == -1:
                            temp_parent.left = temp_left
                    delete.right = None
                    return delete
                elif current.left == None:
                    temp_right = current.right
                    temp_right.parent = temp_parent
                    if current == self.root:
                        self.root = temp_right
                    else:
                        if child == 1:
                            temp_parent.right = temp_right
                        elif child == -1:
                            temp_parent.left = temp_right
                    delete.right = None
                    return delete
                else:
                    rightSubTree = current.right
                    min = self.minimum(rightSubTree)
                    self.delete(min)
                    current.key = min
        pass

    def get(self, key):
        current = self.root
        while current != None:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        pass

    def minimum(self):
        if self.root == None:
            return None
        else:
            current = self.root
            while current.left != None:
                current = current.left
            return current.value
        pass

    def maximum(self):
        if self.root == None:
            return None
        else:
            current = self.root
            while current.right != None:
                current = current.right
            return current.value
        pass

    def traverse_preorder(self):
        arrayOfValues = []
        self.recursive_preorder(arrayOfValues, self.root)
        return arrayOfValues
        pass

    def traverse_inorder(self):
        arrayOfValues = []
        self.recursive_inorder(arrayOfValues, self.root)
        return arrayOfValues
        pass

    def traverse_postorder(self):
        arrayOfValues = []
        self.recursive_postorder(arrayOfValues, self.root)
        return arrayOfValues
        pass

    def recursive_preorder(self, arrayOfValues, node):
        if node is not None:
            arrayOfValues += [node.value]
            self.recursive_preorder(arrayOfValues, node.left)
            self.recursive_preorder(arrayOfValues, node.right)
            #return arrayOfValues
        pass

    def recursive_inorder(self, arrayOfValues, node):
        if node is not None:
            self.recursive_inorder(arrayOfValues, node.left)
            arrayOfValues += [node.value]
            self.recursive_inorder(arrayOfValues, node.right)
            #return arrayOfValues
        pass

    def recursive_postorder(self, arrayOfValues, node):
        if node is not None:
            self.recursive_postorder(arrayOfValues, node.left)
            self.recursive_postorder(arrayOfValues, node.right)
            arrayOfValues += [node.value]
            #return arrayOfValues
        pass
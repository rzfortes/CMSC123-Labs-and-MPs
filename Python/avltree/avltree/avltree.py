from avlnode import AVLTreeNode


class AVLTree:

    def __init__(self):
        self.root = None

    # functions in the bstree
    def insert(self, key, value):
        new_node = AVLTreeNode(key, value, None, None, None)
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
                    new_node.child = -1;
                else:
                    current = current.right
                    new_node.child = 1;
            if key < prev.key:
                prev.left = new_node
                inserted_node = prev.left
            else:
                prev.right = new_node
                inserted_node = prev.right
            new_node.parent = prev

        # update and check for violations
        current = prev
        while current is not None:
            rh = self.height(current.right)
            lh = self.height(current.left)
            current.height = 1+max(lh, rh)

            if lh > rh:
                current.balance = -1
            elif rh > lh:
                current.balance = 1
            else:
                current.balance = 0

            dh = abs(lh-rh)

            if dh > 1:
                if prev.balance == 1 and current.balance == 1:
                    self.leftrotate(current)
                elif prev.balance == -1 and current.balance == -1:
                    self.rightrotate(current)
                elif prev.balance == -1 and current.balance == 1:
                    self.rightrotate(prev)
                    self.leftrotate(current)
                elif prev.balance == 1 and current.balance == -1:
                    self.leftrotate(prev)
                    self.rightrotate(current)

            prev = current
            current = current.parent

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

        #update and check for violations after deleting node
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

    # functions for avltree
    def height(self, node):
        if n is not None:
            return node.height;
        else:
            return -1;

    def leftrotate(self, node):
        #check whether there are redundant or unnecessary steps
        p = node.parent
        r = node.right
        l = r.left
        r.left = node
        node.parent = r
        r.parent = p
        node.right = l
        node.height = 1+max(self.height(node.left), self.height(node.right))
        r.height = 1+max(self.height(r.left), self.height(r.right))
        
        if l is not None:
            l.parent = node
            l.child = 1
        if p is not None:
            if node.child == 1:
                p.right = r
            elif node.child == -1:
                p.left = r
        else:
            self.root = r
        pass

    def rightrotate(self, node):
        #check whether there are redundant or unnecessary steps
        p = node.parent
        l = node.left
        r = l.right
        l.right = node
        node.parent = l
        l.parent = p
        node.left = r
        node.height = 1+max(self.height(node.left), self.height(node.right))
        l.height = 1+max(self.height(l.left), self.height(l.right))

        if r is not None:
            r.parent = node
            r.child = 1
        if p is not None:
            if node.child == 1:
                p.right = 1
            elif node.child == -1:
                p.left = l
        else:
            self.root = l
        pass
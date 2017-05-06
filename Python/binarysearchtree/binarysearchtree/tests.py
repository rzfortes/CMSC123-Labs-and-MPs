import unittest

from bstree import BinarySearchTree
from bstnode import BinarySearchTreeNode


class BinarySearchTreeTestCase(unittest.TestCase):

    def setUp(self):
        self.tree = BinarySearchTree()

    def test_should_have_a_root_property(self):
        self.assertTrue(hasattr(self.tree, 'root'))

    def test_should_default_root_to_none(self):
        self.assertEqual(self.tree.root, None)


class BinarySearchTreeInsertTestCase(unittest.TestCase):

    def setUp(self):
        self.tree = BinarySearchTree()

    def test_should_return_a_binarysearchtreenode_instance(self):
        node = self.tree.insert(1, 'one')
        self.assertTrue(isinstance(node, BinarySearchTreeNode))

    def test_should_make_first_inserted_value_the_root(self):
        node = self.tree.insert(1, 'one')
        self.assertEqual(self.tree.root, node)

        self.tree.insert(2, 'two')
        self.assertEqual(self.tree.root, node)

    def test_should_set_the_node_properties_properly(self):
        two = self.tree.insert(2, 'two')
        self.assertEqual(two.parent, None)
        self.assertEqual(two.left, None)
        self.assertEqual(two.right, None)

        one = self.tree.insert(1, 'one')
        self.assertEqual(one.parent, two)
        self.assertEqual(one.left, None)
        self.assertEqual(one.right, None)
        self.assertEqual(two.left, one)

        four = self.tree.insert(4, 'four')
        self.assertEqual(four.parent, two)
        self.assertEqual(four.left, None)
        self.assertEqual(four.right, None)
        self.assertEqual(two.right, four)

        three = self.tree.insert(3, 'three')
        self.assertEqual(three.parent, four)
        self.assertEqual(three.left, None)
        self.assertEqual(three.right, None)
        self.assertEqual(four.left, three)


class BinarySearchTreeDeleteTestCase(unittest.TestCase):

    def setUp(self):
        self.tree = BinarySearchTree()
        self.seven = self.tree.insert(7, 'seven')
        self.fifteen = self.tree.insert(15, 'fifteen')
        self.eight = self.tree.insert(8, 'eight')
        self.fourteen = self.tree.insert(14, 'fourteen')
        self.nine = self.tree.insert(9, 'nine')
        self.thirteen = self.tree.insert(13, 'thirteen')
        self.ten = self.tree.insert(10, 'ten')
        self.twelve = self.tree.insert(12, 'twelve')
        self.eleven = self.tree.insert(11, 'eleven')

    def test_should_return_the_deleted_node(self):
        node = self.tree.delete(8)
        self.assertEqual(node, self.eight)

    def test_should_set_deleted_node_properties_to_none(self):
        node = self.tree.delete(8)
        self.assertEqual(node.parent, None)
        self.assertEqual(node.left, None)
        self.assertEqual(node.right, None)

    def test_should_replace_deleted_node_with_smallest_value_in_right_subtree(self):
        self.tree.delete(8)

        # in this tree, node "9" should replace the deleted node "8"
        self.assertEqual(self.fifteen.left, self.nine)
        self.assertEqual(self.nine.parent, self.fifteen)
        self.assertEqual(self.nine.left, None)
        self.assertEqual(self.nine.right, self.fourteen)

        # node "9" will then be replaced with node "10"
        self.assertEqual(self.fourteen.left, self.ten)
        self.assertEqual(self.ten.parent, self.fourteen)
        self.assertEqual(self.ten.left, None)
        self.assertEqual(self.ten.right, self.thirteen)

        # node "10" will then be replaced with node "11"
        self.assertEqual(self.thirteen.left, self.eleven)
        self.assertEqual(self.eleven.parent, self.thirteen)
        self.assertEqual(self.eleven.left, None)
        self.assertEqual(self.eleven.right, self.twelve)

    def test_should_set_root_to_replacement_if_root_is_deleted(self):
        self.tree.delete(7)
        self.assertEqual(self.tree.root, self.eight)
        self.assertEqual(self.eight.parent, None)
        self.assertEqual(self.eight.left, None)
        self.assertEqual(self.eight.right, self.fifteen)


class BinarySearchTreeGetTestCase(unittest.TestCase):

    def setUp(self):
        self.tree = BinarySearchTree()
        self.tree.insert(2, 'two')
        self.tree.insert(1, 'one')
        self.tree.insert(3, 'three')

    def test_should_return_the_value_associated_with_the_key(self):
        value = self.tree.get(2)
        self.assertEqual(value, 'two')

        value = self.tree.get(1)
        self.assertEqual(value, 'one')

        value = self.tree.get(3)
        self.assertEqual(value, 'three')


class BinarySearchTreeMinimumMaximumTestCase(unittest.TestCase):

    def setUp(self):
        self.tree = BinarySearchTree()
        self.tree.insert(7, 'seven')
        self.tree.insert(15, 'fifteen')
        self.tree.insert(8, 'eight')
        self.tree.insert(14, 'fourteen')
        self.tree.insert(9, 'nine')
        self.tree.insert(13, 'thirteen')
        self.tree.insert(10, 'ten')
        self.tree.insert(12, 'twelve')
        self.tree.insert(11, 'eleven')
        self.tree.insert(4, 'four')
        self.tree.insert(2, 'two')
        self.tree.insert(5, 'five')
        self.tree.insert(1, 'one')
        self.tree.insert(3, 'three')
        self.tree.insert(6, 'six')

    def test_minimum_should_return_the_value_of_the_minimum_key_in_the_tree(self):
        minimum = self.tree.minimum()
        self.assertEqual(minimum, 'one')

    def test_maximum_should_return_the_value_of_the_maximum_key_in_the_tree(self):
        maximum = self.tree.maximum()
        self.assertEqual(maximum, 'fifteen')


class BinarySearchTreeTraversalsTestCase(unittest.TestCase):

    def setUp(self):
        self.tree = BinarySearchTree()
        self.tree.insert(7, '7')
        self.tree.insert(4, '4')
        self.tree.insert(9, '9')
        self.tree.insert(2, '2')
        self.tree.insert(5, '5')
        self.tree.insert(8, '8')
        self.tree.insert(12, '12')
        self.tree.insert(1, '1')
        self.tree.insert(3, '3')
        self.tree.insert(6, '6')
        self.tree.insert(11, '11')
        self.tree.insert(13, '13')
        self.tree.insert(10, '10')

    def test_preorder_should_return_array_of_preordered_values(self):
        values = self.tree.traverse_preorder()
        expected = ['7', '4', '2', '1', '3', '5', '6', '9', '8', '12', '11', '10', '13']
        self.assertSequenceEqual(values, expected)

    def test_inorder_should_return_array_of_inordered_values(self):
        values = self.tree.traverse_inorder()
        expected = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
        self.assertSequenceEqual(values, expected)

    def test_postorder_should_return_array_of_postordered_values(self):
        values = self.tree.traverse_postorder()
        expected = ['1', '3', '2', '6', '5', '4', '8', '10', '11', '13', '12', '9', '7']
        self.assertSequenceEqual(values, expected)


if __name__ == '__main__':
    unittest.main()

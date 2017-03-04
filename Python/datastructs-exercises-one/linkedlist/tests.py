import unittest

from linkedlist import LinkedList
from linkedlist.node import LinkedListNode


class LinkedListTestCase(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()

    def test_has_head(self):
        self.assertTrue(hasattr(self.list, 'head'))


class LinkedListAddTestCase(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()

    def test_add_should_point_head_to_the_first_item(self):
        self.list.add(1)
        self.assertEqual(self.list.head.value, 1)

        self.list.add(2)
        self.assertEqual(self.list.head.value, 1)

    def test_add_should_initialize_linkedlistnode_for_added_item(self):
        self.list.add(1)
        self.assertTrue(isinstance(self.list.head, LinkedListNode))

    def test_add_should_return_linkedlistnode(self):
        node = self.list.add(1)
        self.assertTrue(isinstance(node, LinkedListNode))

    def test_add_should_increment_list_size(self):
        self.list.add(1)
        self.assertEqual(self.list.size(), 1)


class LinkedListAppendTestCase(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()

    def test_append_should_point_head_to_the_first_item(self):
        self.list.append(1)
        self.assertEqual(self.list.head.value, 1)

        self.list.append(2)
        self.assertEqual(self.list.head.value, 1)

    def test_append_should_initialize_linkedlistnode_for_appended_item(self):
        self.list.append(1)
        self.assertTrue(isinstance(self.list.head, LinkedListNode))

    def test_append_should_return_linkedlistnode(self):
        node = self.list.append(1)
        self.assertTrue(isinstance(node, LinkedListNode))

    def test_append_should_increment_list_size(self):
        self.list.append(1)
        self.assertEqual(self.list.size(), 1)


class LinkedListInsertTestCase(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()
        self.one = self.list.append(1)
        self.two = self.list.append(2)
        self.three = self.list.append(3)

    def test_insert_should_point_head_to_new_item_if_inserted_at_first_position(self):
        self.list.insert(4, 0)
        self.assertEqual(self.list.head.value, 4)

        self.list.insert(5, 0)
        self.assertEqual(self.list.head.value, 5)

    def test_insert_should_not_modify_head_if_item_is_not_inserted_at_first_position(self):
        self.list.insert(4, 1)
        self.assertEqual(self.list.head.value, 1)

        self.list.insert(5, 4)
        self.assertEqual(self.list.head.value, 1)

    def test_insert_should_point_next_of_previous_node_to_new_item(self):
        self.list.insert(4, 1)
        self.assertEqual(self.one.next.value, 4)

        self.list.insert(5, 4)
        self.assertEqual(self.three.next.value, 5)

    def test_insert_should_point_next_of_new_item_to_next_node(self):
        node = self.list.insert(4, 1)
        self.assertEqual(node.next.value, 2)

        node = self.list.insert(5, 4)
        self.assertEqual(node.next.value, None)

    def test_insert_should_initialize_linkedlistnode_for_inserted_item(self):
        self.list.insert(4, 0)
        self.assertTrue(isinstance(self.list.head, LinkedListNode))

    def test_insert_should_return_linkedlistnode(self):
        node = self.list.insert(4, 1)
        self.assertTrue(isinstance(node, LinkedListNode))

    def test_insert_should_increment_list_size(self):
        self.assertEqual(self.list.size(), 3)

        self.list.insert(4, 1)
        self.assertEqual(self.list.size(), 4)


class LinkedListRemoveTestCase(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()
        self.one = self.list.append(1)
        self.two = self.list.append(2)
        self.three = self.list.append(3)

    def test_remove_should_update_head_if_removed_item_is_current_head(self):
        self.list.remove(1)
        self.assertEqual(self.list.head, self.two)

        self.list.remove(2)
        self.assertEqual(self.list.head, self.three)

        self.list.remove(3)
        self.assertEqual(self.list.head, None)

    def test_remove_should_update_the_next_property_of_the_previous_node(self):
        self.list.remove(2)
        self.assertEqual(self.one.next, self.three)

        self.list.remove(3)
        self.assertEqual(self.one.next, None)

    def test_remove_should_return_the_removed_node(self):
        node = self.list.remove(1)
        self.assertEqual(node, self.one)

        node = self.list.remove(2)
        self.assertEqual(node, self.two)

        node = self.list.remove(3)
        self.assertEqual(node, self.three)

    def test_remove_should_return_none_if_node_is_not_found(self):
        node = self.list.remove(4)
        self.assertEqual(node, None)

    def test_remove_should_set_the_next_property_of_removed_node_to_none(self):
        node = self.list.remove(1)
        self.assertEqual(node.next, None)

        node = self.list.remove(2)
        self.assertEqual(node.next, None)

        node = self.list.remove(3)
        self.assertEqual(node.next, None)

    def test_successful_remove_should_decrement_list_size(self):
        self.list.remove(1)
        self.assertEqual(self.list.size(), 2)

    def test_failed_remove_should_not_decrement_list_size(self):
        self.list.remove(4)
        self.assertEqual(self.list.size(), 3)


class LinkedListSearchTestCase(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()
        self.list.append(1)
        self.list.append(2)
        self.list.append(3)

    def test_search_should_return_true_if_item_is_in_the_list(self):
        self.assertTrue(self.list.search(1))
        self.assertTrue(self.list.search(2))
        self.assertTrue(self.list.search(3))

    def test_search_should_return_false_if_item_is_not_in_the_list(self):
        self.assertFalse(self.list.search(4))
        self.assertFalse(self.list.search(5))


class LinkedListSizeTestCase(unittest.TestCase):

    def setUp(self):
        self.list = LinkedList()

    def test_size_should_return_the_number_of_items_in_the_list(self):
        self.assertEqual(self.list.size(), 0)

        self.list.append(1)
        self.assertEqual(self.list.size(), 1)

        self.list.append(2)
        self.assertEqual(self.list.size(), 2)


if __name__ == '__main__':
    unittest.main()

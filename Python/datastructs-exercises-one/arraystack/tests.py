import unittest

from arraystack import Stack


class StackTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_stack_should_use_array_for_storing_items(self):
        self.assertTrue(isinstance(self.stack.items, list))


class StackPushTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push_should_add_item_to_the_end_of_items_list(self):
        self.stack.push(1)
        self.assertEqual(self.stack.items[0], 1)

        self.stack.push(2)
        self.assertEqual(self.stack.items[1], 2)

    def test_push_should_increment_stack_size(self):
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)


class StackPopTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

    def test_pop_should_return_the_last_item_of_its_items_list(self):
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)

    def test_pop_should_return_none_if_stack_is_already_empty(self):
        self.stack.pop()
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(self.stack.pop(), None)

    def test_pop_should_decrement_stack_size(self):
        self.stack.pop()
        self.assertEqual(self.stack.size(), 2)


class StackPeekTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

    def test_peek_should_return_the_last_item_of_its_items_list(self):
        self.assertEqual(self.stack.peek(), 3)
        self.assertEqual(self.stack.peek(), 3)
        self.assertEqual(self.stack.peek(), 3)

    def test_peek_should_return_none_if_stack_is_already_empty(self):
        self.stack.pop()
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(self.stack.peek(), None)

    def test_peek_should_not_decrement_stack_size(self):
        self.stack.peek()
        self.assertEqual(self.stack.size(), 3)


class StackSizeTestCase(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_size_should_return_the_number_of_items_in_the_stack(self):
        self.assertEqual(self.stack.size(), 0)

        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)

        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)

        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)

        self.stack.peek()
        self.assertEqual(self.stack.size(), 1)


if __name__ == '__main__':
    unittest.main()

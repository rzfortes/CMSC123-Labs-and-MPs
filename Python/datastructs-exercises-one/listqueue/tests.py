import unittest

from listqueue import Queue
from linkedlist import LinkedList


class QueueTestCase(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_queue_should_use_linkedlist_for_storing_items(self):
        self.assertTrue(isinstance(self.queue.items, LinkedList))


class QueueEnqueueTestCase(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_enqueue_should_add_item_to_the_end_of_items_list(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.items.head.value, 1)

        self.queue.enqueue(2)
        self.assertEqual(self.queue.items.head.next.value, 2)

    def test_enqueue_should_incremement_queue_size(self):
        self.assertEqual(self.queue.size(), 0)

        self.queue.enqueue(1)
        self.assertEqual(self.queue.size(), 1)


class QueueDequeueTestCase(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

    def test_dequeue_should_return_the_first_item_of_its_items_list(self):
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)

    def test_dequeue_should_return_none_if_queue_is_already_empty(self):
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertEqual(self.queue.dequeue(), None)

    def test_dequeue_should_decrement_queue_size(self):
        self.assertEqual(self.queue.size(), 3)

        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 2)


class QueueFrontTestCase(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

    def test_front_should_return_the_first_item_of_its_items_list(self):
        self.assertEqual(self.queue.front(), 1)
        self.assertEqual(self.queue.front(), 1)
        self.assertEqual(self.queue.front(), 1)

    def test_front_should_return_none_if_queue_is_already_empty(self):
        self.queue.dequeue();
        self.queue.dequeue();
        self.queue.dequeue();
        self.assertEqual(self.queue.front(), None)

    def test_front_should_not_decrement_queue_size(self):
        self.assertEqual(self.queue.size(), 3)

        self.queue.front()
        self.assertEqual(self.queue.size(), 3)


class QueueRearTestCase(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

    def test_rear_should_return_the_last_item_of_its_items_list(self):
        self.assertEqual(self.queue.rear(), 3)
        self.assertEqual(self.queue.rear(), 3)
        self.assertEqual(self.queue.rear(), 3)

    def test_rear_should_return_none_if_queue_is_already_empty(self):
        self.queue.dequeue();
        self.queue.dequeue();
        self.queue.dequeue();
        self.assertEqual(self.queue.rear(), None)

    def test_rear_should_not_decrement_queue_size(self):
        self.assertEqual(self.queue.size(), 3)

        self.queue.rear()
        self.assertEqual(self.queue.size(), 3)


class QueueSizeTestCase(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_size_should_return_the_number_of_items_in_the_queue(self):
        self.assertEqual(self.queue.size(), 0)

        self.queue.enqueue(1)
        self.assertEqual(self.queue.size(), 1)

        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)

        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 1)

        self.queue.front()
        self.assertEqual(self.queue.size(), 1)

        self.queue.rear()
        self.assertEqual(self.queue.size(), 1)


if __name__ == '__main__':
    unittest.main()

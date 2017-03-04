from linkedlist.node import LinkedListNode

class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None
		self.ctr = 0
		
	def add(self, item):
		new_node = LinkedListNode(item, None)

		if(self.ctr == 0):
			self.head = self.tail = new_node
			inserted_item = self.head
		else:
			current = self.head
			for i in range(0, self.ctr - 1):
				current = current.next
			current.next = new_node
			self.tail = new_node
			inserted_item = self.tail
		self.ctr = self.ctr + 1
		return inserted_item
		pass

	def append(self, item):
		new_node = LinkedListNode(item, None)

		if(self.ctr == 0):
			self.head = self.tail = new_node
			inserted_item = self.head
		else:
			current = self.head
			for i in range(0, self.ctr - 1):
				current = current.next
			current.next = new_node
			self.tail = new_node
			inserted_item = self.tail
		self.ctr = self.ctr + 1
		return inserted_item
		pass

	def insert(self, item, position):
		if position < 0 or position > self.ctr:
			return False
		node = LinkedListNode(item, None)
		if position == 0:
			node.next = self.head
			self.head = node
			inserted_item = self.head
		elif position == self.ctr:
			#self.append(item)
			self.tail.next = node
			self.tail = node
			inserted_item = self.tail
		else:
			temp = self.head
			for i in range(0, position - 1):
				temp = temp.next
			node.next = temp.next
			temp.next = node
			inserted_item = temp.next
		self.ctr = self.ctr + 1
		return inserted_item
		pass

	def remove(self, item):
		# gives the position of the item to be removed
		index = self.getPosition(item)
		if (self.ctr == 0) or (index >= self.ctr) or (index < 0):
			return None

		current = self.head
		if(index == 0):
			self.head = current.next
			current.next = None
			removed_item = current
		else:
			for i in range(0, index - 1):
				current = current.next
			if(index == self.ctr - 1):
				self.tail = current
				current = current.next
				current.next = None
				removed_item = current
			else:
				current2 = current.next
				current.next = current2.next
				current2.next = None
				removed_item = current2
		self.ctr = self.ctr - 1
		return removed_item
		pass

	def search(self, item):
		current = self.head
		if(current != None):
			for i in range(0, self.ctr):
				if(current.value == item):
					return True
				current = current.next
			return False
		return False
		pass

	def size(self):
		return self.ctr
		pass

	def getPosition(self, item):
		if(self.ctr == 0):
			return -1

		current = self.head
		if(current != None):
			for i in range(0, self.ctr):
				if(current.value == item):
					return i
				current = current.next
		return -1
		pass
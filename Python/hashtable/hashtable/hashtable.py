# sources in open hashing:
# http://stackoverflow.com/questions/11963711/what-is-the-most-efficient-way-to-search-nested-lists-in-python
# https://www.quora.com/How-do-I-create-my-own-Hash-Table-implementation-in-Python


class hashtable:

	def __init__(self):
		# remember, the size of the array is only 10
		self.closed_htable = []
		self.open_htable = [[] for x in range(10)]

	# hash function
	def hash_function(self, item):
		h = item % 10; # since we don't initialize the size of the list
		return h

	# insert by linear probing
	def closed_insert(self, item):
		h_index = self.hash_function(item)
		if self.closed_htable[h_index] == "inf" or self.closed_htable[h_index] is None:
			self.closed_htable[h_index] = item
		else:
			for i in range(10):
				if self.closed_htable[i % 10] is None:
					self.closed_htable[i % 10] = item
					break

	# search by linear probing
	def closed_search(self, item):
		h_index = self.hash_function(item)
		if self.closed_htable[h_index] == item:
			print "Item found!"
		else:
			for i in range(10):
				if self.closed_htable[i] is None:
					print "Item does not exists!"
					break
				elif self.closed_htable[i] == item:
					print "Item found!"
					break

	# delete by linear probing
	def closed_delete(self, item):
		h_index = self.hash_function(item)
		if self.closed_htable[h_index] == item:
			self.closed_htable[h_index] = "inf"
		else:
			for i in range(10):
				if self.closed_htable[i] is None:
					print "Item does not exists!"
					break
				elif self.closed_htable[i] == item:
					self.closed_htable[i] = "inf"
					break

	# print the items
	def closed_print(self):
		for i in range(0, 10):
			print self.closed_htable[i]


# ---------------- open hashing ----------------
	def open_insert(self, item):
		h_index = hash_function(item)
		self.open_htable[h_index].append(item)
		pass

	def open_search(self, item):
		h_index = hash_function(item)
		if item in [h_index for i in self.open_htable for h_index in i]:
			print "Item found!"
			pass

	def open_delete(Self, item):
		h_index = hash_function(item)
		self.open_htable[h_index].remove(item)
		pass
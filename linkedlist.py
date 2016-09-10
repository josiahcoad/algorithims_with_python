class Node:
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, next_node):
		self.next_node = next_node




class LinkedList:
	def __init__(self, head=None):
		self.head = head
	
	def append_head(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node

	def append_tail(self, data):
		previous = None
		current = self.head
		count = 0
		while current:
			current = current.get_next()
			count += 1
		if current == None:
			self.append_head(data)
		else:
			current.data = data


	def length(self):
		current = self.head
		count = 0
		while current:
			current = current.get_next()
			count += 1
		return count
	
	def find(self, data):
		current = self.head
		found = False
		index = 0
		while current and found == False:
			if current.get_data() == data:
				found = True
			else:
				current = current.get_next()
				index += 1
		if current is None:
			raise ValueError("Data not in list")
		return index

	def delete(self, data):
		previous = None
		current = self.head
		found = False
		while current and found is False:
			if current.get_data() == data:
				found = True
			else:
				previous = current
				current = current.get_next()
		if found is False: # meaning it got to the end of the list without finding the data
			raise ValueError("Data not in list")
		elif previous is None: # meaning the data was in the first Node
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())


myLL = LinkedList()
myLL.append_tail("Hello")
myLL.append_tail("Goodbye")
print (myLL.find("Hello"))
print (myLL.find("Goodbye"))
print (myLL.length())


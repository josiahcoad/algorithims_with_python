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
	
	def append(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node

	def length(self):
		current = self.head
		count = 0
		while current:
			current = current.get_next()
			count += 1
		return count
	
	def get_index(self, data):
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
	
	def __getitem__(self, i):
	# def data_at_place(self, i):
		current = self.head
		index = 0
		while current:
			if index == i: return current.get_data()
			current = current.get_next()
			index += 1
		return IndexError
			
	
	def __len__(self):
		return self.length()
		
	def remove_at_place(self, i):
		self.delete(self[i])

myLL = LinkedList()
myLL.append("Hello")
myLL.append("Goodbye")
myLL.remove_at_place(len(myLL)-1)

print (len(myLL))


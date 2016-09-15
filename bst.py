class Node:
	def __init__(self, key=None, v=None, l=None, r=None, parent=None):
		self.key = key
		self.v = v
		self.l = l
		self.r = r
		self.parent = parent

	def hasLeftChild(self):
		return self.l

	def hasRigthChild(self):
		return self.r

	def isLeftChild(self):
		return self.parent and self.parent.l == self # should be self.v ?

	def isRightChild(self):
		return self.parent and self.parent.r == self # should be self.v ?

	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not (self.r or self.l)

	def hasAnyChildren(self):
		return self.r or self.l

	def hasBothChilden(self):
		return self.r and self.l

	def replaceNodeData(self, new_key, new_val, new_l, new_r):
		self.key = new_key
		self.v = new_val
		self.l = new_l
		self.r = new_r
		if self.hasLeftChild():
			self.l.parent = self
		if self.hasRigthChild():
			self.r.parent = self




class BSTmap:
	def __init__(self):
		self.root = None
		self.size = 0

	def length(self):
		return self.size

	def __len__(self):
		return self.size

	def __iter__(self):
		return self.root.__iter__()

	def put(self, key, val):
		if self.root:
			self._put(key, val, self.root)

		else: 
			self.root = Node(key, val)
		self.size += 1

	def _put(self, key, val, current_node):
		if key < current_node.key:
			if current_node.hasLeftChild():
				self._put(key, val, current_node.l)
			else:
				self.l = Node(key, val, parent=current_node)
		else:
			if current_node.hasRigthChild():
				self._put(key, val, current_node.r)
			else:
				self.r = Node(key, val, parent=current_node)

	def __setitem__(self, k, v):
		self.put(k,v)

	def get(self, key):
		if self.root:
			found_node = self._get(key, self.root)
			if found_node: return found_node.v
			else: return None
		else:
			return None

	def _get(self, key, current_node):
		if not current_node: return None
		elif current_node.key == key: return current_node
		elif key < current_node.key:
			return self._get(key, current_node.l)
		else:
			return self._get(key, current_node.r)

	def __getitem__(self, key):
		return self.get(key)

	def __contains__(self, key):
		return self._get(key, self.root)






mymap = BSTmap()
print (len(mymap))
mymap.put("a", "aligator")
mymap["b"] = "bear"
mymap["c"] = "cat"
print (len(mymap))
print (mymap["b"])
print (mymap.get("b"))



 

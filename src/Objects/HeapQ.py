# Heap Q implementation for Dijkstra (similar to our HW with decrease key)
# Simple Node Class -- we can add accessors/mutators as needed
class HeapQ:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.arr = [None]*maxsize

    def insert(self, node):
    	if self.size >= maxsize:
    		return
    	arr[size] = node
		size++
		self.__upHeap(size-1)

	def remove_min(self):
		if self.size == 0:
			return
		size--
		temp = arr[0]
		if (size != 0):
			arr[0] = arr[size]
			arr[0].position = 0;
			self.__downHeap(0)
		temp.position = -1 #out of heap
		return temp

	def decreaseKey(self, position, value):
		self.arr[position].key = value
		self.__upHeap(position)


	def __upHeap(self, new_pos):
		temp_node = self.arr[new_pos]
		int parent = (new_pos-1)/2;
		while ((new_pos != 0) && temp_node.key < self.arr[parent].key):
			self.arr[new_pos] = self.arr[parent].key
			self.arr[new_pos].position = new_pos
			new_pos = parent
			parent = (new_pos-1)/2
		self.arr[new_pos] = temp_node
		self.arr[new_pos].position = new_pos

	def __downHeap(self, root):
		temp = arr[root]
		if (size == 1):
			return
		int child = 2*root + 1
		while true:
			if (child < size -1):
				if (self.arr[child+1].key < self.arr[child].key): #pick smaller child
					child++
			if (self.arr[child].key < temp.key):
				self.arr[root] = self.arr[child]
				self.arr[root].position = root
				root = child
				child = 2*root+1
			if (child >= size):
				break
		self.arr[root] = temp
		self.arr[root].position = root

        


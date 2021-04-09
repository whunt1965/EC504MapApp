# Heap Q implementation for Dijkstra (similar to our HW with decrease key)

class HeapQ:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.arr = [None] * maxsize

    def insert(self, node):
        if self.size < self.maxsize:
            self.arr[self.size] = node
            self.arr[self.size].position = self.size
            self.size += 1
            self.__upHeap(self.size - 1)

    def remove_min(self):
        if self.size == 0:
            print("size is 0")
        else:
            self.size -= 1
            temp = self.arr[0]
            if self.size != 0:
                self.arr[0] = self.arr[self.size]
                self.arr[0].position = 0
                self.__downHeap(0)
            temp.position = -1  # out of heap
            return temp


    def decreaseKey(self, position, value):
        self.arr[position].key = value
        #print("decrease key time")
        self.__upHeap(position)

    def Empty(self):

        return self.size <= 0

    def Full(self):
        return self.size >= self.maxsize

    def __upHeap(self, new_pos):
        temp_node = self.arr[new_pos]
        parent = int((new_pos - 1) / 2)
        #print("inside decrease")
        while (new_pos != 0) and temp_node.key < self.arr[parent].key:
            self.arr[new_pos] = self.arr[parent]
            self.arr[new_pos].position = new_pos
            new_pos = parent
            parent = int((new_pos - 1) / 2)
            #print("parent")
        self.arr[new_pos] = temp_node
        self.arr[new_pos].position = new_pos

    def __downHeap(self, root):
        temp = self.arr[root]
        if self.size == 1:
            pass
            # print("this is root, no children")
        else:
            child = 2 * root + 1
            while True:
                if child < self.size - 1:
                    if self.arr[child + 1].key < self.arr[child].key:  # pick smaller child
                        child += 1
                if self.arr[child].key < temp.key:
                    self.arr[root] = self.arr[child]
                    self.arr[root].position = root
                    root = child
                    child = 2 * root + 1
                else:
                    break
                if child >= self.size:
                    break
            self.arr[root] = temp
            self.arr[root].position = root

# Simple Node Class -- we can add accessors/mutators as needed
class Node:
    def __init__(self, NodeID, index):
        self.id = NodeID
        self.index = index
        self.edges = []
        self.key = 100000
        self.Parent = -1
        self.isSrc = False
        self.isDest = False


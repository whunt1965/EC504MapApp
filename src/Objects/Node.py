# Simple Node Class -- we can add accessors/mutators as needed
class Node:
    def __init__(self, NodeID, index):
        self.id = NodeID
        self.index = index
        self.edges = []
        self.key = 0
        self.Parent = None
        self.isSrc = False
        self.isDest = False


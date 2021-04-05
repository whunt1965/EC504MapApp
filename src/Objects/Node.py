# Simple Node Class -- we can add accessors/mutators as needed
class Node:
    def __init__(self, NodeID):
        self.id = NodeID
        self.edges = []
        self.key = 0
        self.Parent = None


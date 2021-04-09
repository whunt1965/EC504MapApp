# Simple Node Class -- we can add accessors/mutators as needed
class Node:
    def __init__(self, NodeID, index):
        self.id = NodeID  # ID is the nodeID provided by osmnx (used for mapping)
        self.index = index  # the index of the node in the Nodes list
        self.position = -1  # The position of the node in the heap (for Djikstra)
        self.edges = []  # The edge list for a given node
        self.key = 100000  # The key of a given node (distance from src)
        self.Parent = -1  # The Parent of a node in a path from src to distance
        self.Direction = [None, None]  # The name and length of the edge used to arrive at a node from its parent
        self.h = 0  # h(x) distance used for A* - Euclidean approximation
        self.isSrc = False  # Indicates whether a node is the source node
        self.isDest = False  # Indicates whether a node is the destination node

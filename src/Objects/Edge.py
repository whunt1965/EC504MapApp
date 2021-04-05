# Simple Edge Class -- we can add accessors and mutators as needed
class Edge:
    def __init__(self, Name, start, end, weight):
        self.name = Name
        self.start = start
        self.end = end
        self.weight = weight
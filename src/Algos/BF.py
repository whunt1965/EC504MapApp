# BF.py - Bellman Ford Shortest Path
import queue
from src.Utils import Routes

def BF(Nodes, Map, start, end):
    q = queue.Queue()
    inQ = [False]*len(Nodes)
    src = Nodes[Map.get(start)]
    inQ[Map.get(start)] = True
    src.key = 0
    q.put(src)

    while not q.empty():
        node = q.get()
        # if node.isDest: # Break when we find the end node
        #     break
        inQ[node.index] = False
        for edge in node.edges:
            v = Map[edge.end]
            dv = node.key + edge.weight
            if Nodes[v].key > dv:
                Nodes[v].key = dv
                Nodes[v].Parent = node.id
                Nodes[v].Direction = [edge.name, edge.weight]  # Capture edge name and and length
                if not inQ[v]:
                    q.put(Nodes[v])
                    inQ[v] = True


    node = Nodes[Map.get(end)]  #Get destination node
    dist = node.key  # Get final distance
    route, directions = Routes.getRoute(node, Nodes, Map)  # Computer travel route and human readable directions

    return route, directions, dist





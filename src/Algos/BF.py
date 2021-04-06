# Bellman Ford Algo Here

LARGE = 9999999999
import queue

def getRoute(node, Nodes, Map):
    ret = []
    sum = 0
    while not node.isSrc:
        ret.append(node.id)
        sum+= node.key
        parent = node.Parent
        if parent == -1:
            print("Something went wrong!")
            return None, None # Something went wrong -- lets figure out a better solution
        node = Nodes[Map.get(parent)]
    ret.append(node.id) # Add src node
    ret.reverse()
    return ret, sum


def BF(Nodes, Map, start, end):
    q = queue.Queue()
    inQ = [False]*len(Nodes)

    for node in Nodes:
        node.key = LARGE
        node.Parent = -1

    src = Nodes[Map.get(start)]
    inQ[Map.get(start)] = True
    src.key = 0
    q.put(src)

    while not q.empty():
        node = q.get()
        if node.isDest: # Break when we find the end node
            break
        inQ[node.index] = False
        for edge in node.edges:
            v = Map[edge.end]
            dv = node.key + edge.weight
            if Nodes[v].key > dv:
                Nodes[v].key = dv
                Nodes[v].Parent = node.id
                if not inQ[v]:
                    q.put(Nodes[v])
                    inQ[v] = True


    # Computer Predecessor Array
    node = Nodes[Map.get(end)]
    route, sum = getRoute(node, Nodes, Map)

    return route, sum





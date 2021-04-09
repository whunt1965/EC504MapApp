# Dijkstra Algo here...

from src.Objects.HeapQ import HeapQ

LARGE = 9999999999


def getRoute(node, Nodes, Map):
    ret = []
    while not node.isSrc:
        ret.append(node.id)
        parent = node.Parent
        if parent == -1:
            print("Something went wrong!")
            return None, None  # Something went wrong -- lets figure out a better solution
        node = Nodes[Map.get(parent)]
    ret.append(node.id)  # Add src node
    ret.reverse()
    return ret


def Dijkstra(Nodes, Map, start, end):
    Mark = [-1 for i in range(len(Nodes))]
    src = Nodes[Map.get(start)]
    src.key = 0
    min_v = src
    min_d = 0
    finished = 1

    while finished < len(Nodes):

        for edge in min_v.edges:  # go through edges of a node with minimum key
            v = Map[edge.end]
            dv = min_v.key + edge.weight
            if Nodes[v].key > dv:
                Nodes[v].key = dv
                Nodes[v].Parent = min_v.id

        min_d = LARGE
        for node in Nodes:
            if Mark[node.index] < 1:  # if not visited
                if node.key < min_d:
                    min_d = node.key
                    min_v = node

        Mark[min_v.index] = 1
        finished += 1

    node = Nodes[Map.get(end)]  # Get destination node
    dist = node.key  # Get final distance
    route = getRoute(node, Nodes, Map)  # Computer Predecessor Array (route)
    return route, dist


def Dijkstra_HeapQ(Nodes, Map, start, end):
    queue = HeapQ(len(Nodes))
    src = Nodes[Map.get(start)]
    src.key = 0
    for node in Nodes:
        queue.insert(node)

    count = 0
    while queue.size > 0:
        min_v = queue.remove_min()
        count +=1
        if count == 10:
            print(queue.size)
            count = 0
        for edge in min_v.edges:  # go through edges of a node with minimum key
            v = Map[edge.end]
            dv = min_v.key + edge.weight
            if Nodes[v].key > dv:
                Nodes[v].key = dv
                Nodes[v].Parent = node.id
                queue.decreaseKey(Nodes[v].index, Nodes[v].key)
        print("size" + str(queue.size))

    print("gather")
    node = Nodes[Map.get(end)]  # Get destination node
    dist = node.key  # Get final distance
    route = getRoute(node, Nodes, Map)  # Computer Predecessor Array (route)
    return route, dist

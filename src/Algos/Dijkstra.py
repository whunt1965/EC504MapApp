# Dijkstra Algo here...

from src.Objects.HeapQ import HeapQ
from src.Utils import Routes

LARGE = 9999999999


def Dijkstra(Nodes, Map, start, end):
    Mark = [-1 for i in range(len(Nodes))]
    src = Nodes[Map.get(start)]
    src.key = 0
    min_v = src
    min_d = 0
    finished = 1

    while finished < len(Nodes):
        if min_v.id == end:
            print("end loop early")
            break
        for edge in min_v.edges:  # go through edges of a node with minimum key
            v = Map[edge.end]
            dv = min_v.key + edge.weight
            if Nodes[v].key > dv:
                Nodes[v].key = dv
                Nodes[v].Parent = min_v.id
                Nodes[v].Direction = [edge.name, edge.weight]  # Capture edge name and and length

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
    route, directions = Routes.getRoute(node, Nodes, Map)  # Computer Predecessor Array (route)
    return route, directions, dist


def Dijkstra_HeapQ(Nodes, Map, start, end):
    queue = HeapQ(len(Nodes))
    src = Nodes[Map.get(start)]
    src.key = 0
    for node in Nodes:
        queue.insert(node)

    while queue.size > 0:
        min_v = queue.remove_min()
        if min_v.id == end:
            print("end loop early")
            break
        for edge in min_v.edges:  # go through edges of a node with minimum key
            v = Map[edge.end]
            dv = min_v.key + edge.weight
            if Nodes[v].key > dv:
                Nodes[v].key = dv
                Nodes[v].Parent = min_v.id
                Nodes[v].Direction = [edge.name, edge.weight]  # Capture edge name and and length
                queue.decreaseKey(Nodes[v].position, Nodes[v].key)

    node = Nodes[Map.get(end)]  # Get destination node
    dist = node.key  # Get final distance
    route, directions = Routes.getRoute(node, Nodes, Map)  # Computer Predecessor Array (route)
    return route, directions, dist

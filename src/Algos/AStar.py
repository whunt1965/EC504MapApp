# A* Algo here
from src.Objects.HeapQ import HeapQ
from src.Utils import Routes

LARGE = 9999999999

def AStar(Nodes, Map, start, end):

    # initialize priority queue
    queue = HeapQ(len(Nodes))

    src = Nodes[Map.get(start)]
    dest = Nodes[Map.get(end)]

    src.key = 0

    # insert all nodes into priority queue
    for node in Nodes:
        node.inQueue = True
        node.key += node.h
        queue.insert(node)

    vertex_u = queue.remove_min()
    vertex_u.inQueue = False

    while vertex_u is not dest:  # go through edges of a node with minimum key
        for edge in vertex_u.edges:
            adjacent_node_v = Map[edge.end]
            if Nodes[adjacent_node_v].inQueue:
                distance_v = vertex_u.key + edge.weight
                if distance_v < Nodes[adjacent_node_v].key:
                    Nodes[adjacent_node_v].key = distance_v + Nodes[adjacent_node_v].h
                    Nodes[adjacent_node_v].Parent = vertex_u.id
                    Nodes[adjacent_node_v].Direction = [edge.name, edge.weight]
                    queue.decreaseKey(Nodes[adjacent_node_v].position, Nodes[adjacent_node_v].key)

        vertex_u = queue.remove_min()
        vertex_u.inQueue = False

    distance_to_destination = dest.key
    route, directions = Routes.getRoute(dest, Nodes, Map)
    return route, directions, distance_to_destination


# I am a boss, on a boat





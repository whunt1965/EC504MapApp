# Dijkstra Algo here...
import HeapQ 

def Dijkstra(Nodes,Map, start, end): 	
	Mark = [-1 for i in range(len(Nodes))] 

	

    src = Nodes[Map.get(start)]
    src.key = 0
    min_v = src
    min_d = 0
    finished = 1;

    while finished < len(Nodes):

    	for edge in min_node.edges: #go through edges of a node with minimum key
    		v = Map[edge.end]
    		dv = min_v.key + edge.weight
    		if Nodes[v].key > dv:
                Nodes[v].key = dv
                Nodes[v].Parent = node.id

       
        min_d = LARGE
        for node in Nodes:
        	if Mark[node.id] < 1: #if not visited 
        		if node.key < min_d:
        			min_d = node.key
        			min_v = node
        		
        Mark[min_node.index] = 1
        finished++


def Dijkstra_HeapQ(Nodes,Map, start, end):
    queue = heapQ()
    src = Nodes[Map.get(start)]
    src.key = 0

    for node in Nodes:
        queue.insert(node)


    while(queue.isEmpty() == false):
        min_node = queue.remove_min()

        for edge in min_node.edges: #go through edges of a node with minimum key
            v = Map[edge.end]
            dv = min_v.key + edge.weight
            if Nodes[v].key > dv:
                Nodes[v].key = dv
                Nodes[v].Parent = node.id
                queue.decreaseKey(Nodes[v].position, N[v].key)
            

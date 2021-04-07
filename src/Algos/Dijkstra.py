# Dijkstra Algo here...


def Dijkstra(Nodes,Map, start, end): 
	#Dijstra end when destination is found? or we do we map out the entire graph then find shortest map, which is what we did on hw
	
	Mark = [-1 for i in range(len(Nodes))] 

	for node in Nodes:  #Shouldn't the key for nodes already be in LARGE when initilzied?
        node.key = LARGE
        node.Parent = -1

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

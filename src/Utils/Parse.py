# Graph Parsing -- break graph into nodes and edges
import osmnx as ox
from os import path

from src.Objects.Node import Node
from src.Objects.Edge import Edge


# Get source node from lat/long
# Source: https://automating-gis-processes.github.io/site/notebooks/L6/network-analysis.html
def getSource(Graph, lat, long):
    target_xy = (lat, long)
    target_node = ox.get_nearest_node(Graph, target_xy, method='euclidean')
    return target_node


# Get destination node from lat/long
# Source: https://automating-gis-processes.github.io/site/notebooks/L6/network-analysis.html
def getDest(Graph, lat, long):
    target_xy = (lat, long)
    target_node = ox.get_nearest_node(Graph, target_xy, method='euclidean')
    return target_node


# @param<customlocation> A city name of the form 'Boston, MA, USA' which includes the start and end locations
def buildGraph(startlat, startlong, endlat, endlong, customlocation=None):
    Boston = 'Boston, MA, USA'  # Hardcoded location - Boston MA
    filePath = "./maps/Boston.graphml"  # Hardcoded File Path

    if customlocation:
        try:
            G = ox.graph_from_place(customlocation, network_type="drive")
        except:
            return None, None, None, None, None
    else:
        # Retrieve Graph from disk if it exists. Otherwise, load from Overpass API and save for later usage
        if path.exists(filePath):
            G = ox.load_graphml(filePath)
        else:
            G = ox.graph_from_place(Boston, network_type="drive")
            ox.save_graphml(G, filePath)

    RawNodes = list(G.nodes)  # Extract all nodes from the graph

    # Get Source and Destination Vertex (and their lat, long)
    src = getSource(G, startlat, startlong)
    dest = getDest(G, endlat, endlong)
    dest_y_x = (G.nodes()[dest]['y'], G.nodes()[dest]['x'])

    Nodes = []  # Create an empty node list

    Map = dict()  # Create a quick hashtable for matching node id's to indices in list

    # Iterate through raw node list and create node objects
    for index, node in enumerate(RawNodes):
        myNode = Node(node, index)

        # Calculate euclidean approximation for distance between source and this node
        myNode.h = ox.distance.euclidean_dist_vec(G.nodes()[node]['y'], G.nodes()[node]['x'], dest_y_x[0], dest_y_x[1])

        # Mark source node
        if node == src:
            myNode.isSrc = True

        # Mark Destination Node
        if node == dest:
            myNode.isDest = True
            myNode.h = 0

        RawEdges = G.adj[node]  # Get the raw edges for the node
        RawEdgeList = list(RawEdges)  # Convert into a list of neighboring nodes

        # Construct edges and add to edge list of node
        for edge in RawEdgeList:
            myEdge = Edge(Name=RawEdges[edge][0].get("name"), start=node, end=edge,
                          weight=RawEdges[edge][0].get("length"))
            myNode.edges.append(myEdge)
        Map[node] = index  # map node id to its index in the list for fast lookup since no pointers
        Nodes.append(myNode)  # map node id to its index in the "Node" list for fast lookup from edges (eg,
        # Map[NodeID] = index of this node in our list)

    return G, Nodes, Map, src, dest  # Return the graph (for plotting) and the Node list (for the algorithms)

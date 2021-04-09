
from src.Utils import Parse
from src.Algos import BF, Dijkstra
from src.Utils import Output
import osmnx as ox
import networkx as nx


G, Nodes, Map, src, dest = Parse.buildGraph(42.3505, -71.1054, 42.3467, -71.0972)

print("calculating BF")
route1, sum1 = BF.BF(Nodes, Map, src, dest)
print("calculating Dijkstra simple")
route2, sum2 = Dijkstra.Dijkstra(Nodes, Map, src, dest)
print("calculating Dijkstra with HeapQ")
route3, sum3 = Dijkstra.Dijkstra_HeapQ(Nodes, Map, src, dest)
print("BF sum: " + str(sum1))
print("Dijkstra simple sum:" + str(sum2))
print("Dijkstra Heap sum:" + str(sum3))
graph_proj = ox.project_graph(G)
correct_route = nx.shortest_path(G=graph_proj, source=src, target=dest, weight='length')

routes = [route1, route2, route3]
for Algo_route in routes:
    if correct_route != Algo_route:
        print("Not same")
        print("my route", Algo_route)
        print("their route", Algo_route)
    else:
        print(str(Algo_route) + "is correct")



fig, ax = ox.plot_graph_route(graph_proj, route1, show= False, save=True, filepath="map.png")



fig.savefig('pic.png')

Output.giveOutput()






# G, Nodes = Parse.buildGraph(42.3505, -71.1054, 42.3467, -71.0972)
# print(Nodes)
# start = Parse.getSource(G, 42.3505, -71.1054)
# stop = Parse.getSource(G,  42.3467, -71.0972)
# graph_proj = ox.project_graph(G)
# route = nx.shortest_path(G=graph_proj, source=start, target=stop, weight='length')
# fig, ax = ox.plot_graph_route(graph_proj, route)

# G = ox.graph_from_point((42.35, -71.10), dist=750, network_type='all')
# k = G.adj[61340762]
# edges = list(k)
# for edge in edges:
#     print(k[edge][0].get("name"))
#     print(k[edge][0].get("length"))
# print(G.adj[61340762][k[0]][0].get("name"))
# ox.plot_graph(G)


from src.Utils import Parse
from src.Algos import BF
from src.Utils import Output
import osmnx as ox
import networkx as nx


G, Nodes, Map, src, dest = Parse.buildGraph(42.3505, -71.1054, 42.3467, -71.0972)


route1, sum = BF.BF(Nodes, Map, src, dest)
print(sum)
graph_proj = ox.project_graph(G)
route = nx.shortest_path(G=graph_proj, source=src, target=dest, weight='length')
if route != route1:
    print("Not same")
    print("my route", route1)
    print("their route", route)
else:
    print("same")

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

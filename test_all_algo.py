from src.Utils import Parse
from src.Algos import BF, Dijkstra
from src.Utils import Output
from src.Algos import AStar
import osmnx as ox
import networkx as nx

# Data Structure
# results -> City_list -> route_list -> info
#                                    -> Algo -> BF/Dijkstra/Astar
#                                    -> correct -> osm route
global results
global City_list

results = {}
City_list = []


# Calculate
def Run_Algo_on_route(City, route_id):
    src = results[City][route_id]["info"]["src"]
    dest = results[City][route_id]["info"]["dest"]
    G = results[City][route_id]["info"]["G"]
    Nodes = results[City][route_id]["info"]["Nodes"]
    Map = results[City][route_id]["info"]["Map"]
    results[City][route_id]["Algo"] = {}

    #print("calculate shortest from osm as correct result")
    graph_proj = ox.project_graph(G)
    correct_route = nx.shortest_path(G=graph_proj, source=src, target=dest, weight='length')
    results[City][route_id]["correct"] = correct_route

    #print("calculating BF for " + str(City) + " for route " + str(route_id))
    route1, directions1, sum1 = BF.BF(Nodes, Map, src, dest)
    results[City][route_id]["Algo"]["BF"] = {"route": route1, "direction": directions1, "sum": sum1}

    #print("calculating Astar for " + str(City) + " for route " + str(route_id))
    route2, directions2, sum2 = AStar.AStar(Nodes, Map, src, dest)
    results[City][route_id]["Algo"]["Astar"] = {"route": route2, "direction": directions2, "sum": sum2}

    #print("calculating Dijkstra simple for " + str(City) + " for route " + str(route_id))
    route3, directions3, sum3 = Dijkstra.Dijkstra(Nodes, Map, src, dest)
    results[City][route_id]["Algo"]["Dijkstra Simple"] = {"route": route3, "direction": directions3, "sum": sum3}

    #print("calculating Dijkstra with HeapQ for " + str(City) + " for route " + str(route_id))
    route4, directions4, sum4 = Dijkstra.Dijkstra_HeapQ(Nodes, Map, src, dest)
    results[City][route_id]["Algo"]["Dijkstra Heap"] = {"route": route4, "direction": directions4, "sum": sum4}




def Check_results():
    for x in range(len(City_list)): # goes through all the cities
        City_i = City_list[x]
        print("city name: " + str(City_i))
        for route_i in range(1, len(results[City_i])+1): # goes through different routes in same city
            print("route: " + str(route_i))
            correct_route = results[City_i][route_i]["correct"]
            for key, value in results[City_i][route_i]["Algo"].items(): # check algo for each route
                if correct_route != results[City_i][route_i]["Algo"][key]["route"]:
                    print("Not same" + str(key))
                    print("Algo route", results[City_i][route_i]["Algo"][key]["route"])
                    print("correct route", correct_route)
                else:
                    print(str(key) + " is correct")



Boston = 'Boston, MA, USA'
City1 = str(Boston.split(",")[0])
City_list.append(City1)
results[City1] = {1: {}, 2: {}, 3: {}, 4: {}}

# test BU to fenway
G, Nodes, Map, src, dest = Parse.buildGraph_forTest(Boston, 42.3505, -71.1054, 42.3467, -71.0972)
results[City1][1]["info"] = {"G": G, "Nodes": Nodes, "Map": Map, "src": src, "dest": dest}

# test maverick to shawmut
G, Nodes, Map, src, dest = Parse.buildGraph_forTest(Boston, 42.3691, -71.0395, 42.2931, -71.0658)
results[City1][2]["info"] = {"G": G, "Nodes": Nodes, "Map": Map, "src": src, "dest": dest}

# readville to revere
G, Nodes, Map, src, dest = Parse.buildGraph_forTest(Boston, 42.236937, -71.140175, 42.397557, -70.999853)
results[City1][3]["info"] = {"G": G, "Nodes": Nodes, "Map": Map, "src": src, "dest": dest}

# cambridge to quincy
G, Nodes, Map, src, dest = Parse.buildGraph_forTest(Boston, 42.383807, -71.116494, 42.253763, -71.017757)
results[City1][4]["info"] = {"G": G, "Nodes": Nodes, "Map": Map, "src": src, "dest": dest}

for x in range(1, len(results[City1])+1):
    Run_Algo_on_route(City1, x)

Seattle = 'Seattle, WA, USA'
City2 = str(Seattle.split(",")[0])
City_list.append(City2)
results[City2] = {1: {}, 2: {}, 3: {}}

#space needle 47.620580, -122.349453
#smith tower 47.603105, -122.332287
#University of Washington 47.657361, -122.302589

# test space needle to smith tower
G, Nodes, Map, src, dest = Parse.buildGraph_forTest(Seattle, 47.620580, -122.349453, 47.603105, -122.332287)
results[City2][1]["info"] = {"G": G, "Nodes": Nodes, "Map": Map, "src": src, "dest": dest}

# smith tower to university of washington
G, Nodes, Map, src, dest = Parse.buildGraph_forTest(Seattle, 47.603105, -122.332287, 47.657361, -122.302589)
results[City2][2]["info"] = {"G": G, "Nodes": Nodes, "Map": Map, "src": src, "dest": dest}

# university of washington to smith tower
G, Nodes, Map, src, dest = Parse.buildGraph_forTest(Seattle, 47.657361, -122.302589, 47.620580, -122.349453)
results[City2][3]["info"] = {"G": G, "Nodes": Nodes, "Map": Map, "src": src, "dest": dest}



for x in range(1, len(results[City2])+1):
    Run_Algo_on_route(City2, x)

Check_results()



# Test file for Dense Networks
# Sample Cities are New York City, Tokyo, & Sao Paolo

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.Utils import Parse
from src.Algos import BF, Dijkstra, AStar
import osmnx as ox
import networkx as nx
import time
import csv
from os import path


# Runs the Algo for each test case in a City
def Run_Algo_on_route(City, route_id, results,total_edges, csv_filename="output.csv"):
    src = results[City][route_id]["info"]["src"]
    dest = results[City][route_id]["info"]["dest"]
    G = results[City][route_id]["info"]["G"]
    Nodes = results[City][route_id]["info"]["Nodes"]
    Map = results[City][route_id]["info"]["Map"]
    results[City][route_id]["Algo"] = {}

    csv_timing_list = []

    print("Calculate shortest path using default OSM Shortest Path on " + str(City) + " for route " + str(route_id))
    graph_proj = ox.project_graph(G)
    start = time.time()
    correct_route = nx.shortest_path(G=graph_proj, source=src, target=dest, weight='length')
    stop = time.time()
    print("Total Time (seconds) Required to Calculate", stop-start)
    results[City][route_id]["correct"] = correct_route

    print("Calculating Shortest path using BF for " + str(City) + " for route " + str(route_id))
    start = time.time()
    route1, directions1, sum1 = BF.BF(Nodes, Map, src, dest)
    stop = time.time()
    csv_timing_list.append(stop-start)
    print("Distance of Shortest Path " + str(sum1))
    print("Total Time (seconds) Required to Calculate", stop-start)
    results[City][route_id]["Algo"]["BF"] = {"route": route1, "direction": directions1, "sum": sum1}

    print("Calculating Shortest path using A* for " + str(City) + " for route " + str(route_id))
    start = time.time()
    route2, directions2, sum2 = AStar.AStar(Nodes, Map, src, dest)
    stop = time.time()
    csv_timing_list.append(stop - start)
    print("Distance of Shortest Path " + str(sum2))
    print("Total Time (seconds) Required to Calculate", stop-start)
    results[City][route_id]["Algo"]["Astar"] = {"route": route2, "direction": directions2, "sum": sum2}

    print("Calculating Shortest path using Djikstra Simple for " + str(City) + " for route " + str(route_id))
    start = time.time()
    route3, directions3, sum3 = Dijkstra.Dijkstra(Nodes, Map, src, dest)
    stop = time.time()
    csv_timing_list.append(stop - start)
    print("Distance of Shortest Path " + str(sum3))
    print("Total Time (seconds) Required to Calculate", stop-start)
    results[City][route_id]["Algo"]["Dijkstra Simple"] = {"route": route3, "direction": directions3, "sum": sum3}

    print("Calculating Shortest path using Djikstra HeapQ for " + str(City) + " for route " + str(route_id))
    start = time.time()
    route4, directions4, sum4 = Dijkstra.Dijkstra_HeapQ(Nodes, Map, src, dest)
    stop = time.time()
    csv_timing_list.append(stop - start)
    print("Distance of Shortest Path " + str(sum4))
    print("Total Time (seconds) Required to Calculate", stop-start)
    results[City][route_id]["Algo"]["Dijkstra Heap"] = {"route": route4, "direction": directions4, "sum": sum4}

    print("Calculating Shortest path using no-break Djikstra Simple for " + str(City) + " for route " + str(route_id))
    start = time.time()
    route5, directions5, sum5 = Dijkstra.DumbDijkstra(Nodes, Map, src, dest)
    stop = time.time()
    csv_timing_list.append(stop - start)
    print("Distance of Shortest Path " + str(sum5))
    print("Total Time (seconds) Required to Calculate", stop-start)
    results[City][route_id]["Algo"]["Dijkstra Simple No Break"] = {"route": route5, "direction": directions5, "sum": sum5}

    print("Calculating Shortest path using no-break Djikstra HeapQ for " + str(City) + " for route " + str(route_id))
    start = time.time()
    route6, directions6, sum6 = Dijkstra.Dumb_Dijkstra_HeapQ(Nodes, Map, src, dest)
    stop = time.time()
    csv_timing_list.append(stop - start)
    print("Distance of Shortest Path " + str(sum6))
    print("Total Time (seconds) Required to Calculate", stop-start)
    results[City][route_id]["Algo"]["Dijkstra Heap No break"] = {"route": route6, "direction": directions6, "sum": sum6}


    header = ["City","# Edges","BF","A*", "Dij Simple","Dij Heap", "NB Dij Simple","NB Dij Heap"]
    data_row = [City, total_edges]
    for timing in csv_timing_list:
        data_row.append(timing)
    if not path.exists("./" + csv_filename):
        with open(csv_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(header)
            writer.writerow(data_row)
    else:
        with open(csv_filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data_row)



def Check_results(City_list, results):
    for x in range(len(City_list)): # goes through all the cities
        City_i = City_list[x]
        print("city name: " + str(City_i))
        for route_i in range(1, len(results[City_i])+1): # goes through different routes in same city
            print("route: " + str(route_i))
            correct_route = results[City_i][route_i]["correct"]
            for key, value in results[City_i][route_i]["Algo"].items(): # check algo for each route
                if correct_route != results[City_i][route_i]["Algo"][key]["route"]:
                    print("Not same " + str(key))
                    print("Algo route", results[City_i][route_i]["Algo"][key]["route"])
                    print("correct route", correct_route)
                else:
                    print(str(key) + " is correct")


def testCity(routes, csv_filename):
    results = {}
    City_list = []
    CityName = routes[0]
    City1 = str(CityName.split(",")[0])
    City_list.append(City1)
    results[City1] = {1: {}, 2: {}, 3: {}, 4: {}}

    # test 4 routes
    for i in range(1,5):
        G, Nodes, Map, src, dest = Parse.buildGraph(routes[i][0], routes[i][1], routes[i][2], routes[i][3], CityName)
        results[City1][i]["info"] = {"G": G, "Nodes": Nodes, "Map": Map, "src": src, "dest": dest}

    # Print Graph Details
    print("********************* Graph Details ****************************")
    print("Test for " + CityName)
    print("Total Number of Nodes " + str(len(G.nodes())))
    print("Total Number of Edges " + str(len(G.edges())))
    print()

    # Run Algos
    print("********************* Algorithm Results ****************************")
    for x in range(1, len(results[City1]) + 1):
        Run_Algo_on_route(City1, x, results, len(G.edges()), csv_filename)
        print()

    #Check Results
    print("********************* Validation Against Built-In Shortest Path ****************************")
    Check_results(City_list, results)
    print()

# if __name__ == '__main__':
#     csv_file = "denseCities.csv"
#
#     testCity(['New York, NY, USA',[40.524720, -74.238649, 40.750144, -73.705440],
#                                   [40.577345, -73.965786, 40.908174, -73.904183],
#                                   [40.792695, -73.975811, 40.643440, -73.784404],
#                                   [40.705523, -74.012034, 40.888913, -73.835425]], csv_file)
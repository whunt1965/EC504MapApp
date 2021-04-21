# Test file for Medium-Sized Networks
# Sample Cities are Boston, MA and Seattle, Washington

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.Utils import Parse
from src.Algos import BF, Dijkstra, AStar
import osmnx as ox
import networkx as nx
import time
import itertools
import csv
from os import path


# Data Structure
# results -> City -> coordinates
#                 -> path : (list 0:len) -> info
#                                        -> correct -> osm route
#                                        -> correct_distance -> osm route distance
#                                        -> Algo : (BF/Astar/Dijkstra 4 types) -> route
#                                                                              -> direction
#                                                                              -> sum
#                                                                              -> time


def main(results, option, csv_filename):
    # Creating paths

    for key, value in results.items():  # Iterate through different cities
        print("\n********************* Graph Details ****************************")
        results[key]["paths"] = {}  # Initialize route list for this city
        route_count = 0
        if option == 1:
            for i in range(0,len(results[key]["coordinates"])):  # different combinations of paths with different coordinates
                for j in range(i + 1, len(results[key]["coordinates"])):
                    x1 = results[key]["coordinates"][i][0]
                    y1 = results[key]["coordinates"][i][1]
                    x2 = results[key]["coordinates"][j][0]
                    y2 = results[key]["coordinates"][j][1]
                    G, Nodes, Map, src, dest = Parse.buildGraph(x1, y1, x2, y2, key)
                    if route_count == 0:
                        # Print Graph Details
                        print("Test for " + key)
                        print("Total Number of Nodes " + str(len(G.nodes())))
                        print("Total Number of Edges " + str(len(G.edges())))
                        print()
                    results[key]["paths"][route_count] = {}  # Initialize route
                    results[key]["paths"][route_count]["info"] = {"G": G, "Nodes": Nodes, "Map": Map, "src": src,
                                                                  "dest": dest}

                    Run_Algo_on_route(key, route_count, results, len(G.edges()), csv_filename)
                    route_count += 1
        else:
            for i in range(1,len(results[key]["coordinates"]), 2):
                x1 = results[key]["coordinates"][i-1][0]
                y1 = results[key]["coordinates"][i-1][1]
                x2 = results[key]["coordinates"][i][0]
                y2 = results[key]["coordinates"][i][1]
                G, Nodes, Map, src, dest = Parse.buildGraph(x1, y1, x2, y2, key)
                if route_count == 0:
                    # Print Graph Details
                    print("Test for " + key)
                    print("Total Number of Nodes " + str(len(G.nodes())))
                    print("Total Number of Edges " + str(len(G.edges())))
                    print()
                results[key]["paths"][route_count] = {}  # Initialize route
                results[key]["paths"][route_count]["info"] = {"G": G, "Nodes": Nodes, "Map": Map, "src": src,
                                                              "dest": dest}
                Run_Algo_on_route(key, route_count, results, len(G.edges()), csv_filename)
                route_count += 1

    # Check Results
    print("\n*********** Validation Against Built-In Shortest Path *********************")
    Check_results(results)
    print()


# Runs the Algo for each test case in a City
def Run_Algo_on_route(City, route_id, results, total_edges, csv_filename="output.csv"):
    src = results[City]["paths"][route_id]["info"]["src"]
    dest = results[City]["paths"][route_id]["info"]["dest"]
    G = results[City]["paths"][route_id]["info"]["G"]
    Nodes = results[City]["paths"][route_id]["info"]["Nodes"]
    Map = results[City]["paths"][route_id]["info"]["Map"]
    results[City]["paths"][route_id]["Algo"] = {}

    csv_timing_list = []

    print("\nCalculate shortest path using default OSM Shortest Path on " + str(City) + " for route " + str(route_id))
    graph_proj = ox.project_graph(G)
    start = time.time()
    correct_route = nx.shortest_path(G=graph_proj, source=src, target=dest, weight='length')
    stop = time.time()
    correct_distance = nx.shortest_path_length(G=graph_proj, source=src, target=dest, weight='length')
    print("Distance of Shortest Path " + str(correct_distance))
    print("Total Time (seconds) Required to Calculate", stop - start)
    results[City]["paths"][route_id]["correct"] = correct_route
    results[City]["paths"][route_id]["correct_distance"] = correct_distance

    print("Calculating Shortest path using BF for " + str(City) + " for route " + str(route_id))
    start = time.time()
    route1, directions1, sum1 = BF.BF(Nodes, Map, src, dest)
    stop = time.time()
    cal_time = stop - start
    csv_timing_list.append(cal_time)
    print("Distance of Shortest Path " + str(sum1))
    print("Total Time (seconds) Required to Calculate", cal_time)
    results[City]["paths"][route_id]["Algo"]["BF"] = {"route": route1, "direction": directions1, "sum": sum1,
                                                      "time": cal_time}

    print("Calculating Shortest path using A* for " + str(City) + " for route " + str(route_id))
    start = time.time()
    route2, directions2, sum2 = AStar.AStar(Nodes, Map, src, dest)
    stop = time.time()
    cal_time = stop - start
    csv_timing_list.append(cal_time)
    print("Distance of Shortest Path " + str(sum2))
    print("Total Time (seconds) Required to Calculate", cal_time)
    results[City]["paths"][route_id]["Algo"]["Astar"] = {"route": route2, "direction": directions2, "sum": sum2,
                                                         "time": cal_time}

    print("Calculating Shortest path using Djikstra Simple for " + str(City) + " for route " + str(route_id))
    start = time.time()
    route3, directions3, sum3 = Dijkstra.Dijkstra(Nodes, Map, src, dest)
    stop = time.time()
    cal_time = stop - start
    csv_timing_list.append(cal_time)
    print("Distance of Shortest Path " + str(sum3))
    print("Total Time (seconds) Required to Calculate", cal_time)
    results[City]["paths"][route_id]["Algo"]["Dijkstra Simple"] = {"route": route3, "direction": directions3,
                                                                   "sum": sum3,
                                                                   "time": cal_time}

    print("Calculating Shortest path using Djikstra HeapQ for " + str(City) + " for route " + str(route_id))
    start = time.time()
    route4, directions4, sum4 = Dijkstra.Dijkstra_HeapQ(Nodes, Map, src, dest)
    stop = time.time()
    cal_time = stop - start
    csv_timing_list.append(cal_time)
    print("Distance of Shortest Path " + str(sum4))
    print("Total Time (seconds) Required to Calculate", cal_time)
    results[City]["paths"][route_id]["Algo"]["Dijkstra Heap"] = {"route": route4, "direction": directions4, "sum": sum4,
                                                                 "time": cal_time}

    print("Calculating Shortest path using no-break Djikstra Simple for " + str(City) + " for route " + str(route_id))
    start = time.time()
    route5, directions5, sum5 = Dijkstra.DumbDijkstra(Nodes, Map, src, dest)
    stop = time.time()
    cal_time = stop - start
    csv_timing_list.append(cal_time)
    print("Distance of Shortest Path " + str(sum5))
    print("Total Time (seconds) Required to Calculate", cal_time)
    results[City]["paths"][route_id]["Algo"]["Dijkstra Simple No Break"] = {"route": route5, "direction": directions5,
                                                                            "sum": sum5, "time": cal_time}

    print("Calculating Shortest path using no-break Djikstra HeapQ for " + str(City) + " for route " + str(route_id))
    start = time.time()
    route6, directions6, sum6 = Dijkstra.Dumb_Dijkstra_HeapQ(Nodes, Map, src, dest)
    stop = time.time()
    cal_time = stop - start
    csv_timing_list.append(cal_time)
    print("Distance of Shortest Path " + str(sum6))
    print("Total Time (seconds) Required to Calculate", cal_time)
    results[City]["paths"][route_id]["Algo"]["Dijkstra Heap No break"] = {"route": route6, "direction": directions6,
                                                                          "sum": sum6,
                                                                          "time": cal_time}

    header = ["City", "# Edges", "BF", "A*", "Dij Simple", "Dij Heap", "NB Dij Simple", "NB Dij Heap"]
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


def Check_results(results):
    for City_i, content in results.items():  # goes through all the cities
        print("\n Validating: " + str(City_i))
        for route_i in range(len(results[City_i]["paths"])):  # goes through different paths in same city
            print("route: " + str(route_i))
            correct_route = results[City_i]["paths"][route_i]["correct"]
            correct_dist = results[City_i]["paths"][route_i]["correct_distance"]
            for key, value in results[City_i]["paths"][route_i]["Algo"].items():  # check algo for each route
                if correct_route != results[City_i]["paths"][route_i]["Algo"][key]["route"]:
                    print("Not same " + str(key))
                    print("Algo Distance: " + str(results[City_i]["paths"][route_i]["Algo"][key]["sum"]))
                    print("Correct Distance: " + str(correct_dist))
                    print("Algo route", results[City_i]["paths"][route_i]["Algo"][key]["route"])
                    print("correct route", correct_route)
                else:
                    print(str(key) + " is correct")



if __name__ == '__main__':
    
    # Initialize City and endpoints
    # Boston: Cambridge, Quincy, Fenway
    # Seattle: Space Needle, Smith Tower, UW
    # Rochester: Seneca Zoo, Strong Museum, George Eastman Museum
    # Chicago: Cloud Gate, Field Museum, Douglass Golf
    medium_cities = {
        'Boston, MA, USA': {"coordinates": [(42.383807, -71.116494), (42.253763, -71.017757), (42.3467, -71.0972)]},
        'Seattle, WA, USA': {
            "coordinates": [(47.620580, -122.349453), (47.603105, -122.332287), (47.657361, -122.302589)]},
        'Rochester, NY, USA': {
            "coordinates": [(43.209686, -77.624640), (43.156614, -77.603354), (43.1710744, -77.5745238)]},
        'Chicago, IL, USA': {
            "coordinates": [(41.883469, -87.623010), (41.8721873, -87.618736), (41.865040, -87.698550)]}}

    # This can slice the dictionary to the number of cities we want to test
    i = 2
    results = dict(itertools.islice(medium_cities.items(), i))

    # Two options for testing
    #option = 1 # Test all possible combinations, 3 coordinates = 3 paths, 4 coordinates = 6 paths
    option = 2 # Test specific routes from node1 to node2, node3 to node 4, if the array is odd size, then it will only test even
    csv_file = "mediumCities.csv"

    main(results, option, csv_file)

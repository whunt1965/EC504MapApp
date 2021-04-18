from src.Utils import Parse
from src.Algos import BF, Dijkstra
from src.Utils import Output
from src.Algos import AStar
import osmnx as ox
import networkx as nx


citySelection = {
        1: "Boston",
        2: "Nashville",
        3: "Detroit",
        4: "Gotham City",
    }

algorithms = {
        1: "Bellman-Ford",
        2: "Dijkstras",
        3: "A*",
    }



def inputCity():
    for key, value in citySelection.items():
            print(key, ': ', value)
    
    while True:
        while True:
            try:
                city = input ("Select a city to navigate: ")
                city = int(city)
                break
            except:
                print("Please enter an integer 1-4")


        if city >= 1 and city <= 4:
            return city
        else:
            print("Please selection an option between 1 and 4")
            continue

def srcDest():

    while True:
        srcLat = input("Enter source latitude : ")
        srcLong = input("Enter source longitude : ")
        try:
            srcLat=float(srcLat)
            srcLong=float(srcLong)
            srcTuple = (srcLat, srcLong)
            break
        except:
            print("Please enter number")
    while True:
        dstLat = input("Enter destination latitude : ")
        dstLong = input("Enter destination longitude : ")
        try:
            dstLat=float(dstLat)
            dstLong=float(dstLong)
            dstTuple = (dstLat, dstLong)
            break
        except:
            print("Please enter number")


    points = [srcTuple, dstTuple]
    return points


def algoSelection():
    for key, value in algorithms.items():
            print(key, ': ', value)
    while True:
        while True:
            try:
                algo = input ("Select an algorithm to use: ")
                algo = int(algo)
                break
            except:
                print("Please enter an integer 1-4")

        if algo >= 1 and algo <= 3:
            return algo
        else:
            print("Please selection an option between 1 and 4")
            continue


def calculateRoutes(source, destination, city, algoNum):


    #42.383807, -71.116494, 42.253763, -71.017757
    #G, Nodes, Map, src, dest = Parse.buildGraph(source[0], source[1], destination[0], destination[1])
    
    G, Nodes, Map, src, dest = Parse.buildGraph(42.383807, -71.116494, 42.253763, -71.017757)

    print("Calculating route...")
    if algoNum == 1:
        route, directions, sum = BF.BF(Nodes, Map, src, dest)
    elif algoNum == 2:
        route, directions, sum = Dijkstra.Dijkstra(Nodes, Map, src, dest)
    elif algoNum == 3:
        route, directions, sum = AStar.AStar(Nodes, Map, src, dest)

    # #Debug - remove for production
    # print(sum)


    nc = (0.976, 0.411, 0.411, 1.0)
    background=(1.0,1.0,1.0,0.0)
    graph_proj = ox.project_graph(G)
    fig, ax = ox.plot_graph_route(graph_proj, route,node_color='w', node_size=5, edge_linewidth=0.5, route_color= nc, bgcolor = background, show= False, save=True, filepath="map.png")
    #fig.savefig('pic.png')
    Output.giveOutput(source, destination, directions, city)




if __name__ == '__main__':

    while True: 
        city = inputCity()
        print("----------------")
        points = srcDest()
        print("----------------")
        algoNum = algoSelection()
        print("----------------")
        src = str(points[0])
        dst = str(points[1])
    
        print("Travelling from " + src + " to " + dst + " in " + citySelection[city] + " using " + algorithms[algoNum])
        correct = input ("Correct?  [Y/N]: ")
        print("----------------")
    
        if correct == 'Y' or correct == 'y':
            calculateRoutes(points[0], points[1], city, algoNum)
            break
        else:
            continue
    





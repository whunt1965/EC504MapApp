from main import calculateRoutes

def test():
    City_list = {'Key West, FL, USA' : [(24.548847, -81.808354), (24.566556, -81.752220)],
                 'Bath, ME, USA': [(43.932595, -69.819257), (43.891222, -69.818332)],
                 'Stowe, VT, USA':[(44.427876, -72.716742), (44.491012, -72.631137)],
                 'Boston, MA, USA':[(42.287856, -71.047196), (42.362482, -71.135774)],
                 'Seattle, WA, USA': [(47.507297, -122.254868), (47.730847, -122.359925)],
                 'Nashville, TN, USA': [(35.988773, -86.638339), (36.356819, -86.781162)],
                 'New York, New York, USA': [(40.524720, -74.238649), (40.750144, -73.705440)],
                 'Los Angeles, CA, USA': [(33.716850, -118.292293), (34.315587, -118.462581)],
                 'Houston, TX, USA': [(29.570586, -95.087936), (29.866332, -95.557894)]}
    for key, coordinates in City_list.items():
        city = key
        points = coordinates
        algoNum = 1
        src = str(points[0])
        dst = str(points[1])
        print("city " + str(city) + " points" + str(points))
        name = city.split(",")[0] + ".html"
        print(name)
        calculateRoutes(points[0], points[1], city, algoNum, name)




if __name__ == '__main__':
    test()







import itertools
from TestNetwork import main

num_cities = 3
option = 2
csv_filename = "consolidated.csv"

sparse_cities = {
    'Key West, FL, USA': {"coordinates":       [(24.548847, -81.808354), (24.566556, -81.752220),
                                                (24.549337, -81.782893), (24.571023, -81.759769),
                                                (24.564104, -81.768455), (24.559799, -81.803981),
                                                (24.563450, -81.796612), (24.555767, -81.776064)]},

    'Bath, ME, USA': {"coordinates":           [(43.932595, -69.819257), (43.891222, -69.818332),
                                                (43.901587, -69.816278), (43.916612, -69.832510),
                                                (43.927194, -69.812579), (43.906829, -69.826955),
                                                (43.974582, -69.834968), (43.872335, -69.828647)]},

    'Stowe, VT, USA': {"coordinates":          [(44.427876, -72.716742), (44.491012, -72.631137),
                                                (44.433220, -72.683700), (44.521845, -72.755511),
                                                (44.469344, -72.802185), (44.465558, -72.684435),
                                                (44.415837, -72.676139), (44.514078, -72.692889)]}
}

results = dict(itertools.islice(sparse_cities.items(), num_cities))
main(results, option, csv_filename)

medium_cities = {
    'Boston, MA, USA': {"coordinates":         [(42.287856, -71.047196), (42.362482, -71.135774),
                                                (42.338143, -71.027947), (42.289792, -71.163706),
                                                (42.236937, -71.140175), (42.397557, -70.999853),
                                                (42.383807, -71.116494), (42.253763, -71.017757)]},

    'Seattle, WA, USA': {"coordinates":        [(47.507297, -122.254868), (47.730847, -122.359925),
                                                (47.620580, -122.349453), (47.603105, -122.332287),
                                                (47.603105, -122.332287), (47.657361, -122.302589),
                                                (47.657361, -122.302589), (47.620580, -122.349453)]},

    'Nashville, TN, USA': {"coordinates":      [(35.988773, -86.638339), (36.356819, -86.781162),
                                                (36.054305, -86.988528), (36.272720, -86.690524),
                                                (36.218451, -86.858066), (36.255004, -86.748203),
                                                (35.988773, -86.638339), (36.188531, -86.584781)]}
}

results = dict(itertools.islice(medium_cities.items(), num_cities))
main(results, option, csv_filename)

dense_cities = {
    'New York, New York, USA': {"coordinates": [(40.524720, -74.238649), (40.750144, -73.705440),
                                                (40.577345, -73.965786), (40.908174, -73.904183),
                                                (40.792695, -73.975811), (40.643440, -73.784404),
                                                (40.705523, -74.012034), (40.888913, -73.835425)]},

    'Los Angeles, CA, USA': {"coordinates":    [(33.716850, -118.292293), (34.315587, -118.462581),
                                                (34.046337, -118.525753), (34.082741, -118.167324),
                                                (34.259990, -118.594417), (33.939308, -118.242855),
                                                (33.991701, -118.469448), (34.213441, -118.645229)]},

    'Houston, TX, USA': {"coordinates":        [(29.570586, -95.087936), (29.866332, -95.557894),
                                                (29.822543, -95.218276), (29.651983, -95.536783),
                                                (29.889413, -95.296296), (29.605707, -95.403689),
                                                (29.616841, -95.348279), (29.883231, -95.424779)]}
}

results = dict(itertools.islice(dense_cities.items(), num_cities))
main(results, option, csv_filename)


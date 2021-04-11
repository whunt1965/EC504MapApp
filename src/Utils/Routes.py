# Routes.py
import osmnx as ox

# Helper function to find route (node Path) and step-by-step directions on a shortest path
def getRoute(node, Nodes, Map):
    route = []
    directions = []
    while not node.isSrc:
        route.append(node.id)
        parent = node.Parent
        if parent == -1:
            print("Something went wrong!")
            return None, None  # Something went wrong -- lets figure out a better solution

        # Get ordinal/cardinal direction for edge
        node.Direction.append(_degreestoDirection(ox.bearing.get_bearing(Nodes[Map.get(parent)].yx, node.yx)))

        directions.append(node.Direction)
        node = Nodes[Map.get(parent)]
    route.append(node.id)  # Add src node
    route.reverse()
    directions.reverse()
    directions = _itemize(directions)
    return route, directions


# Generates an array of human readable strings to print step-by-step directions from src to destination
def _itemize(directions):
    combo = [directions[0]]  # Combines directions on same street

    # Combine directions along same street
    for i in range(1, len(directions)):
        idx = len(combo) - 1
        # Check for same street and travel distance along street if street is same
        if directions[i][0] == combo[idx][0] and directions[i][2] == combo[idx][2]:
            combo[idx][1] += directions[i][1]
        else:
            combo.append(directions[i])

    # Generate Strings from condensed directions
    ret = []
    for i in range(0, len(combo)):
        if combo[i][0] is None and i < len(combo)-1:
            ret.append(f"Continue {combo[i][2]} onto {combo[i+1][0]} for {combo[i][1]} meters")
        else:
            ret.append(f"Travel {combo[i][2]} for {combo[i][1]} meters along {combo[i][0]}")

    return ret

# Converts degrees to a cardinal direction
def _degreestoDirection(degrees):
    degrees = int(degrees)
    if degrees == 0:
        return "North"
    elif 0 < degrees < 90:
        return "Northeast"
    elif degrees == 90:
        return "East"
    elif 90 < degrees < 180:
        return "Southeast"
    elif degrees == 180:
        return "South"
    elif 180 < degrees < 270:
        return "Southwest"
    elif degrees == 270:
        return "West"
    elif 270 < degrees < 360:
        return "Northwest"
    else:
        return "North"




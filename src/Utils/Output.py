import os


# Create new HTML file, insert link to saved plot, 
# add other relevant information

def giveOutput(src, dst, directions, city, distance, total_time, algo_name, file_name = "output.html"):
    asset_path = "assets"
    if file_name == "output.html":  # main.py
        map_name = "map.png"

    else:
        #parse out .html
        map_name = str(file_name.split(".")[0]) + "_map.png"
        print("file_name after split: " + file_name)
        file_name = str(os.getcwd()) + "/outputs/" + file_name
        print("file path:" + str(file_name))
        asset_path = "../assets"

    print(str(file_name))
    f = open(file_name, 'w')
    message = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title>Destination</title>
    <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="{assets}/style.css">
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </head>
    <body id="grad1">
    <hr class="new3">
    <img src="{assets}/dest.png"  width="600"  class="center"/>
    <hr class="new3">

    <div class="container">
     <div class="container2">
     <h1>ROUTE POINTS</h1>
     <hr class="new4">
    """.format(assets = asset_path)
    f.write(message)

    header = "<h2>"
    endheader = "</h2>"
    locationInfo = header + "Source: " + str(src) + endheader + header + "Destination: " + str(dst) + endheader
    totalDistance = header + "Total Distance: " + str(round(distance, 1)) + " meters" + endheader
    algoInfo = header + "Route calculated in " + str(round(total_time, 1)) + " seconds using " + algo_name + endheader
    f.write(locationInfo)
    f.write(totalDistance)
    f.write(algoInfo)

    image = """
    </div>
    </div>
    <img src="{map_name}" class="center2"/>
      <hr class="new3">
     <div class="container">
     <div class="container2">
     <h2>DIRECTIONS</h2>
     <hr class="new4">
    <ol>
    """.format(map_name = map_name)
    image2 = """
    </div>
    </div>
    <img src="{assets}/map2.jpeg" class="center2"/>
    <hr class="new3">
     <div class="container">
     <div class="container2">
     <h2>DIRECTIONS</h2>
     <hr class="new4">
    """.format(assets = asset_path)
    if city == 4:
        f.write(image2)
        f.write("<h1>SWEAR TO ME!!!!!</h1>")

    else:
        f.write(image)
        i = 0
        p = "<li>"
        endP = "</li>"
        f.write("<ol>")
        while (i < len(directions)):
            direction = p + str(directions[i]) + endP
            f.write(direction)
            i = i + 1
        f.write("</ol>")

    f.write("""</body>
     </div>
    </div>
    </html>""")
    f.close()

    os.system(file_name) # Windows doesn't use open

import os


# Create new HTML file, insert link to saved plot, 
# add other relevant information

def giveOutput(src, dst, directions, city, distance, total_time, algo_name):
    f = open('output.html','w')
    message = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title>Destination</title>
    <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="assets/style.css">
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </head>
    <body id="grad1">
    <hr class="new3">
    <img src="assets/dest.png"  width="600"  class="center"/>
    <hr class="new3">

    <div class="container">
     <div class="container2">
     <h1>ROUTE POINTS</h1>
     <hr class="new4">
    """
    f.write(message)

  
    header = "<h2>"
    endheader = "</h2>"
    locationInfo = header + "Source: " + str(src) + endheader + header + "Destination: " + str(dst) + endheader
    totalDistance = header + "Total Distance: " + str(round(distance, 1)) + " meters" + endheader
    algoInfo = header + "Route calculated in " + str(round(total_time, 1)) + " seconds using " + algo_name + endheader
    f.write(locationInfo)
    f.write(totalDistance)
    f.write(algoInfo)
    
    image="""
    </div>
    </div>
    <img src="map.png" class="center2"/>
      <hr class="new3">
     <div class="container">
     <div class="container2">
     <h2>DIRECTIONS</h2>
     <hr class="new4">
    <ol>
    """
    image2="""
    </div>
    </div>
    <img src="assets/map2.jpeg" class="center2"/>
    <hr class="new3">
     <div class="container">
     <div class="container2">
     <h2>DIRECTIONS</h2>
     <hr class="new4">
    """
    if city == 4:
        f.write(image2)
        f.write("<h1>SWEAR TO ME!!!!!</h1>")

    else:
        f.write(image)
        i=0
        p = "<li>"
        endP = "</li>"
        f.write("<ol>")
        while(i < len(directions)):
            direction = p + str(directions[i]) + endP
            f.write(direction)
            i = i+1
        f.write("</ol>")

    f.write("""</body>
     </div>
    </div>
    </html>""")
    f.close()
    os.system("open output.html")




import os


# Create new HTML file, insert link to saved plot, 
# add other relevant information

def giveOutput(src, dst, route, city):
    f = open('output.html','w')
    message = """<html>
    <head></head>
    <body>
    """
    f.write(message)

  
    header = "<h2>"
    endheader = "<h2/>"
    locationInfo = header + str(src) + endheader + header + str(dst) + endheader
    
    f.write(locationInfo)
    
    image="""
    <img src="pic.png""/>
    </body>
    </html>"""
    image2="""
    <img src="map2.jpeg" />
    </body>
    </html>"""
    if city == 4:
        f.write(image2)
        f.write("<h1>SWEAR TO ME!!!!!</h1>")

    else:
        f.write(image)
        i=0
        p = "<p>"
        endP = "<p/>"
        while(i < 10):
            direction = p + "direction number: " + str(i) + endP
            f.write(direction)
            i = i+1
    f.close()
    os.system("open output.html")




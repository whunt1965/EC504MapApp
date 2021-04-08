import os


# Create new HTML file, insert link to saved plot, 
# add other relevant information

def giveOutput():
    f = open('output.html','w')
    message = """<html>
    <head></head>
    <body>
    """
    f.write(message)

    src = "42.3505, -71.1054"
    dst = "42.3467, -71.0972"
    header = "<h2>"
    endheader = "<h2/>"
    locationInfo = header + src + endheader + header + dst + endheader
    
    f.write(locationInfo)
    
    image="""
    <img src="pic.png" />
    </body>
    </html>"""
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




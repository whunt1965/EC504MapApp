# EC504 Map Application
### Wiley Hunt    Santiago Gomez    Apollo Lo    Ken Krebs

* [Link to Our Report](https://docs.google.com/document/d/1nbyvtMloAYKxHEIoC8Xq5ailhlhB-m4Sr7QJrhC_lKc/edit)
---

![DestLogo@3x](https://user-images.githubusercontent.com/56164075/115408217-b0fa8b80-a1be-11eb-8fc3-93b12b9b3388.png)
---
Destination is a Map application to get directions between longitude and latitude points in any city. It utilizes OpenStreetMap using Python to calculate the shortest routes between points between select algorithms: Bellman-Ford Algorithm, Dijkstra's Algorithm, and A* Algorithm. 


## To Run Locally
Make sure to download and [install](https://docs.conda.io/en/latest/miniconda.html) miniconda if it is not already installed. 

### Setup Miniconda Environment
`conda create --name=<env> --file=requirements.txt`

### To Run
```Linux
conda activate <env>
python main.py
```
### Sample Inputs
```
Boston, MA, USA
Src Lat:42.383807
Src Long: -71.116494, 
Dst Lat: 42.253763
Dst Long: -71.017757
```


## To Run on the SCC
To run Destination on the SCC, an X-Forwarding Application is necessary to view the GUI output provided by the Application. Please consult the appropriate section for your operating system:

#### Windows
An X-Server can be installed and configured on a Microsoft Windows system using [MobaXterm](https://mobaxterm.mobatek.net/)
MobaXterm has an X-server built-in, so after you login to the SCC you should be able to launch a remote graphical application without any extra work.
To test if X-forwarding works correctly:
```scc1% xclock&```

#### Apple OS X
First install the XQuartz/X11 application, which is available at http://xquartz.macosforge.org/landing/, it may already be installed. 
Once XQuartz is intalled, connect to the SCC using:
```your_local_machine% ssh –Y yourBULoginName@scc1.bu.edu```
To test if X-forwarding works correctly:
```scc1% xclock&```
#### Linux

X Forwarding should be built-in on your Linux machine but you will need to include the -X flag with your ssh command.
```your_local_machine% ssh –X yourBULoginName@scc1.bu.edu```
To test if X-forwarding works correctly:
```scc1% xclock&```

### Setup Miniconda Environment
```Linux
./buildEnv.sh
```

### To Run
```Linux
./runApp.sh
```

### Sample Inputs
```
Boston, MA, USA
Src Lat:42.383807
Src Long: -71.116494, 
Dst Lat: 42.253763
Dst Long: -71.017757
```

# EC504 Map Application
### Wiley Hunt    Santiago Gomez    Apollo Lo    Ken Krebs

* [Link to Our Report](https://docs.google.com/document/d/1nbyvtMloAYKxHEIoC8Xq5ailhlhB-m4Sr7QJrhC_lKc/edit)
---

![DestLogo@3x](https://user-images.githubusercontent.com/56164075/115408217-b0fa8b80-a1be-11eb-8fc3-93b12b9b3388.png)
---
Destination is a Map application to get directions between longitude and latitude points in any city. It utilizes OpenStreetMap using Python to calculate the shortest routes between points between select algorithms: Bellman-Ford Algorithm, Dijkstra's Algorithm, and A* Algorithm. 


## To Run Locally
Make sure to download and [install][(https://docs.conda.io/en/latest/miniconda.html) miniconda if it is not already installed. 

### Setup Miniconda Environment
`conda create --name=<env> --file=requirements.txt`

### To Run
```Linux
conda activate <env>
python main.py
```
### Sample Inputs
```Boston, MA, USA
Src:42.383807, -71.116494, 
Dst: 42.253763, -71.017757
```


## To Run on the SCC

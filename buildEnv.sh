module load miniconda
conda config --prepend channels conda-forge
conda create -n ox -c conda-forge osmnx
conda activate ox
conda install networkx=2.5.1 

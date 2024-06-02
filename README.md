# BOSearchStructures
Python Code for Manuscript "An Automated Search Strategy for Novel Ordered Structures of Block Copolymers"

requirements:
- numpy==1.23.5
- [GPyOpt](https://github.com/SheffieldML/GPyOpt)

## Installation and Usage

```bash
conda create --name dqsGpyOpt python=3.9
conda activate dqsGpyOpt
conda install conda-forge::numpy=1.23.5 # higher versions may not work
conda install conda-forge::gpyopt
```

To add a new acquisition function, replace files in "/path/to/conda/envs/dqsGpyOpt/lib/python3.9/site-packages/GPyOpt/" with the files in the GPyOpt_dqsModified folder in this repository.


Change the shebang line in searchStructureMain.py, optimizer.py, and worker.py to the path of your python interpreter:

```python
#!/path/to/python
```

Add executable permissions:

```bash
chmod +x searchStructureMain.py optimizer.py worker.py
```

Prepare the input files: input.json, para.json



```json
input.json is the input file for the SCFT program

para.json is the input file for the automatic search algorithm
{
  "step": 128, // number of BO steps
  "worker": 8, // number of workers
  "spacegroup": 136, // space group number
  "basis": 24, // number of basis functions
  "start_basis": 0, // start basis function
  "bcp": "AB",  // block copolymer type, e.g., AB, ABC
  "fixlevel": true, // true: phi_A==F, phi_B==1-F; false: phi_A==1 if F>level. see phi_generator.py
  "cellratio": 0.5, // if fixratio is True, Lz = cellratio * Lx, otherwise Lz is independent
  "fixratio": true, 
  "lxyzBounds": [2,20], // bounds for Lx, Ly, Lz
  "rand": false,  // randomly generate initial structures
  "weight": 10,  // acquisition weight 
  "distance_weight": -10, // distance weight
  "distance_sigma": 0.1,  // distance sigma
  "distance_lambda": 0.1, // distance lambda
  "list_size": 1000, // tabu length
  "optimizerThread": 8, // number of cpu threads for optimizer.py
  "calPlane": "zy", // calculate plane for 2d structures
  "program": "/home/share/scft2024", // path to the SCFT program
  "partition": "amd_4090,intel_4090,amd_3090,intel_2080ti,intel_2080", // partition for the SCFT program
  "cpupartition": "intel_Xeon,amd_4090,amd_3090" // partition for optimizer.py
}
```


Run the main script:

```bash
/path/to/searchStructureMain.py > a.log 2>&1 &
```





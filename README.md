# MFCAD++ Dataset Generation
This repo contains the scripts used to generate the MFCAD++ dataset for the [Hierarchical CADNet](https://www.sciencedirect.com/science/article/abs/pii/S0010448522000240) paper.

The MFCAD++ dataset can be downloaded from here: https://pure.qub.ac.uk/en/datasets/mfcad-dataset-dataset-for-paper-hierarchical-cadnet-learning-from

Unlike the MFCAD dataset which used Pickled Python lists saved as .face_truth files, the MFCAD++ dataset saved the class labels directly to the ADVANCED_FACES in the STEP files.

## Requirements
See the environment.yml file.

## Instructions
- To generate a dataset of CAD models with different machining features run **main.py**.
- In **main.py**, ```num_features``` parameter changes the number of feature classes to create feature sequences from.
- In **main.py**, ```combo_range``` parameter changes the min and max number of machining features in the feature sequences.
- In **main.py**, ```num_samples``` parameter changes the number of CAD models generated.
- You can change general parameters of the CAD models by changing values in **Utils/parameters.py**.

(It was found that the fillet/round tool in PythonOCC is not very robust and may cause Python to crash.)


## Citation
Please cite this work if used in your research:

    @article{hierarchicalcadnet2022,
      Author = {Andrew R. Colligan, Trevor. T. Robinson, Declan C. Nolan, Yang Hua, Weijuan Cao},
      Journal = {Computer-Aided Design},
      Title = {Hierarchical CADNet: Learning from B-Reps for Machining Feature Recognition},
      Year = {2022}
      Volume = {147}
      URL = {https://www.sciencedirect.com/science/article/abs/pii/S0010448522000240}
    }

## Funding 
This project was funded through DfE funding.


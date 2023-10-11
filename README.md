# End_to_End_Deep_learning_Kidney_tumour_classification_MLFOW_DVC

## Workflows

1. Update config.yaml
2. Update secrets.yaml[optional]
3. Update parms.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. Update the app.py



# How to run?

### steps:

Clone the repository

```bash
https://github.com/senthil100695/End_to_End_Deep_learning_Kidney_tumour_classification_MLFOW_DVC
```

### STEP 01 - Create a conda environment  after opening the repository

```bash
conda create -n cnncls python=3.9 -y
```
```bash
conda activate cnncls
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt

```

#### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/senthil100695/End_to_End_Deep_learning_Kidney_tumour_classification_MLFOW_DVC.mlflow \
MLFLOW_TRACKING_USERNAME=senthil100695 \
MLFLOW_TRACKING_PASSWORD=c6a12eba9766266ebce1f50a4d02ef18796984a2 \
python script.py

Run this to export as env variables if unix use export if you use windows use 'set' instead of export:
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/senthil100695/End_to_End_Deep_learning_Kidney_tumour_classification_MLFOW_DVC.mlflow

export MLFLOW_TRACKING_USERNAME=senthil100695

export MLFLOW_TRACKING_PASSWORD=c6a12eba9766266ebce1f50a4d02ef18796984a2

### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    # .github Keeps the workflows directory tracked by Git, then it is 
    # used later for GitHub Actions (CI/CD) pipelines.
    # .gitkeep is used to keep the directory since Git doesn’t track empty folders,
    
    f"src/{project_name}/__init__.py", # init files Marks directories as Python packages
    f"src/{project_name}/components/__init__.py",
    # Will contain core ML pipeline components, e.g.: Data ingestion, Model training,..
    
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py", # Common helper functions used in the project
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    f"src/{project_name}/pipeline/__init__.py",
    # Will contain pipeline orchestration code. Ex: TrainingPipeline, PredictionPipeline
    f"src/{project_name}/entity/__init__.py",
    #Defines data classes / entities:  DataIngestionConfig, ModelTrainerConfig
    f"src/{project_name}/constants/__init__.py",
    #Stores constants: File paths, Fixed strings, Default values
    "config/config.yaml", # Stores paths & configurations
    "params.yaml", # to store model hyperparameters
    "app.py",  # Entry point for web app / API (FastAPI / Flask)
    "main.py", # Entry point to run training or pipelines
    "Dockerfile",
    "requirements.txt", # Lists all Python dependencies
    "setup.py", # Makes the project installable as a package: pip install -e .
    "research/trials.ipynb", #Jupyter notebook for Experiments
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass # Create the file and don’t write anything to it
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} is already exists")
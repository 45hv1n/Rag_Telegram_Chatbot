import os
from pathlib import Path 
import logging

import sys

print(sys.modules)

logging.basicConfig(level= logging.INFO, format= '[%(asctime)s]: %(message)s')

project_name = "Chatbot"


list_of_files = [ 
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/document_processor.py",
    f"src/{project_name}/components/pinecone_embedding.py",
    f"src/{project_name}/components/model.py",
    f"src/{project_name}/constants/__init__.py",
    ".env",
    "app.py",
    "chain.py",
    "data_processing.py",
    "requirements.txt",
    "setup.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"Creating directory {filedir}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating a file { filepath }")
    else :
        logging.info(f"{ filepath } already exists")
import os
from pathlib import Path
import logging

# Always run relative to this file's location
BASE_DIR = Path(__file__).parent
os.chdir(BASE_DIR)

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s]: %(message)s:'
)

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",

    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",

    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

for file in list_of_files:
    filepath = Path(file)

    # Create parent directories if they don't exist
    if filepath.parent != Path("."):
        filepath.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Creating directory: {filepath.parent}")

    # Create empty file if it doesn't exist
    if not filepath.exists():
        filepath.touch()
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
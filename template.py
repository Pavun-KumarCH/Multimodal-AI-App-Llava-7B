import os
from pathlib import Path
import logging

list_of_files = [
                  "SRC/Components/__init__.py",
                  "SRC/Components/model_pipeline.py",
                  "SRC/Components/transcription.py",
                  "SRC/Components/image_analysis.py",
                  "SRC/Components/text_to_speech.py",
                  "SRC/Components/utils.py",
                  "SRC/Components/config.py",
                  "images/.image.png",
                  "main.py",
                  "logger.py",
                  "Exception.py",
                  "setup.py"
                ]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Created directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"{filepath} is already created..!")
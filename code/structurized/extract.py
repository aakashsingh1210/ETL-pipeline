import pandas as pd
import os
from loguru import logger


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0,SCRIPT_DIR)


# code for getting all files inside a directory
def list_full_paths(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory)]

#  code for finding correct path of local input data
def extract():    
    # Get the list of all files paths inside input directory
    try:
        paths=list_full_paths(SCRIPT_DIR.replace("/structurized","/input"))
        logger.success("extract function completes here-------------")
        return paths
    except:
        logger.info("extract function of structurized unable to get correct path of input files")

    








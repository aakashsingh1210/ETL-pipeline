import pandas as pd
import numpy as np
import os
from google.cloud import storage 
from loguru import logger

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

#upload file
def load(df,index):
    try:
        file_path=SCRIPT_DIR+"/structured"+str(index)+".csv"
        df.to_csv(file_path,index=False)
        logger.success("load function of structurized folder completes here-------")
    except:
        logger.info("some error occurred in load function of structurized folder")

    


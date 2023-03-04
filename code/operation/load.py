import pandas as pd
import numpy as np
import os
from google.cloud import storage 
from loguru import logger

#upload file
def load(df,index):
    try:
        name="final_output"+str(index)+".csv"
        df.to_csv(name,index=False)
        logger.success("load function of operation completed here------------")
    except:
        logger.info("some error occurred in load function of operation folder")





    # code for loading data to google cloud storage 
    
    # try:
    #     abs_path="/home/uslsz344/Desktop/practise/assignment_test/test/ServiceKey_GoogleCloud.json"
    #     os.environ['GOOGLE_APPLICATION_CREDENTIALS']=abs_path
    #     storage_client=storage.Client()
    #     # The bucket on GCS in which to write the CSV file
    #     bucket = storage_client.bucket('de_test1234')
    #     # The path assigned to the CSV file on GCS
    #     blob = bucket.blob('output/aakash_singh_output.csv')
    #     blob.upload_from_string(df.to_csv(), 'text/csv')     #converting dataframe to csv and loading
    #     print(blob.public_url)                               # csv to google cloud
    #     print("load function completed here -----------")
        
    # except:
    #     print("some error occurred while loading data to google cloud")







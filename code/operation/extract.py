import inspect
import pandas as pd
import numpy as np
import os
import sys
from io import BytesIO  # for reading from google cloud to dataframe directly
from google.cloud import storage 
from loguru import logger

# code for extracting data from structurized dataframe

# SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

def extract(index):
    # path=SCRIPT_DIR.replace("/operation","/structurized/structurized.csv")
    try:
        try:
            path=parentdir+"/structurized/structured"+str(index)+".csv"
        except:
            logger.info("unable to get correct input file for operation extract function")
        
        df=pd.read_csv(path)  
        logger.success("extract function of operation completes here--------------")
        return df
    except:
        logger.info("some error occurred in extract function of operation folder")

    
# extract()




# code for using google cloud credentials

#     abs_path="/home/uslsz344/Desktop/practise/assignment_test/test/ServiceKey_GoogleCloud.json"
#     os.environ['GOOGLE_APPLICATION_CREDENTIALS']=abs_path
#     storage_client=storage.Client()

#     df=pd.DataFrame()       # creating empty dataframe

#     #access file 
#     first=1
#     for blob in storage_client.list_blobs('de_test1234', prefix='input/Input'):
#         blobBytes = blob.download_as_bytes()
#         if first:
#             first=0
#             df_temp = pd.read_csv(BytesIO(blobBytes))
#             header_list=df_temp.iloc[9:10].values.tolist()[0]  # getting header from first dataframe
#             for i in range(len(header_list)):                  
#                 header_list[i]=header_list[i].strip()          # stripping header as it contain spaces
#             # print(header_list)
#             # concating all the temporary dataframe from each input file to a dataframe name 'df'

#             df = pd.concat([df, df_temp.iloc[10:]])  # data is from df_temp.iloc[10:]
#             continue
#         df_temp = pd.read_csv(BytesIO(blobBytes))
#         df = pd.concat([df, df_temp.iloc[10:]])     # concating the data to main dataframe
#     df.columns = header_list                        # setting the obtained header list
#     df=df.reset_index(drop=True)                    # resetting index as it was wrongly indexed
#     df = df.astype('int')                           # converting object datatype to int
#     print("extract function completed here --------")
#     return df                       









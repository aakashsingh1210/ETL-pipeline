import sys
import pandas as pd
import numpy as np
from loguru import logger
import time

output_column_name=['employee id','average','out time','in time']
df_out=pd.DataFrame(columns=output_column_name)

def calculate(data):
    global df_out
    in_time=sum(data['area']*data['in time(days)'])/sum(data['area'])
    out_time=sum(data['area']*data['out time'])/sum(data['area'])
    average=sum(data['area']*data['total income'])/sum(data['area'])
    df_out.loc[len(df_out.index)] = [data['employee id'].iat[0],average,out_time,in_time] 


def transform(df):
    global df_out
    try:     
        start=time.time()   
        df.groupby('employee id').apply(calculate)
        lowest_average = df_out['average'].min()
        df_out.insert(loc =2,column = 'lowest average',value = lowest_average)  
        df_out['employee id']=df_out['employee id'].astype(int)
        df_out=df_out.reset_index(drop=True)       # reset the index of dataframe
        logger.success("transform function of operation completed here-----------")
        end=time.time()
        print(start-end)
        return df_out
    except:
        logger.info("some unexpected error occurred in transform function of operation folder")



# transform(extract())







#previous code

    # output_column_name=['employee id','average','out time','in time']
    # df_out=pd.DataFrame(columns=output_column_name)
    
    # #adding new columns using calculation from existing columns
    # df["area*in_time"]=df['area']*df['in time(days)']  #
    # df["area*out_time"]=df['area']*df['out time']
    # df["area*total_income"]=df['area']*df['total income']
    # id_list=df['employee id'].unique().tolist()  # extracted unique employee id 
    # id_list.sort()                               # sorting the unique employee id
    # lowest_average=sys.maxsize                   # setting lowest_average variable to a high value
    
    # for id in id_list:
    #     df_temp=df.loc[df['employee id']==id]
    #     in_time_average=df_temp.sum()[5]/df_temp.sum()[0]  # finding averages by dividing the sums of
    #     out_time_average=df_temp.sum()[6]/df_temp.sum()[0]  # particular columns
    #     average=df_temp.sum()[7]/df_temp.sum()[0]
        
    #     # taking all value from above and adding to the dictionary so that we can convert it to 
    #     # a dataframe and concatenate to the output dataframe
    
    #     data = {'employee id': [id],                         
    #         'average': [average],'out time': [out_time_average],'in time': [in_time_average]}
    #     df1 = pd.DataFrame(data)
    #     df_out=pd.concat([df_out,df1])
    #     if average<lowest_average:           # finding lowest average by comparing values
    #         lowest_average=average
    
    # # inseting lowest average  column
    # df_out.insert(loc =2,column = 'lowest average',value = lowest_average)  
    # df_out=df_out.reset_index(drop=True)       # reset the index of dataframe
    
    # print("transform function completed here -------")
    # print(df_out[10:])


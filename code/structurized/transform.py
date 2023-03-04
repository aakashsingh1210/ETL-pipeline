import pandas as pd
from loguru import logger

def transform(paths):
    try:
        df=pd.DataFrame()
        first=1
        for path in paths:
            if first:
                first=0
                try:
                    df_temp=pd.read_csv(path)
                except:
                    logger.info("transform function of structurized unable to find csv files")
                try:
                    header_list=df_temp.iloc[9:10].values.tolist()[0]  # getting header from first dataframe
                except:
                    logger.info("header is not located is correct position")
                for i in range(len(header_list)):                  
                    header_list[i]=header_list[i].strip()          # stripping header as it contain spaces
                # print(header_list)
                # concating all the temporary dataframe from each input file to a dataframe name 'df'
                df = pd.concat([df, df_temp.iloc[10:]])  # replace by [10:] at end
                continue
            try:
                df_temp=pd.read_csv(path)
            except:
                logger.info("transform function of structurized unable to find csv files")
            df = pd.concat([df, df_temp.iloc[10:]])     # replace by [10:] at end
        df.columns = header_list
        df=df.reset_index(drop=True)
        df = df.astype('int')
        logger.success("tranform function of structurized completes here")
        return df
    except:
        logger.info("some unexpected error occurred in transform function of structurized folder")
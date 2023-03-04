from operation.extract import extract
from operation.load import load
from operation.transform import transform

def main(index):
    df=extract(index)
    df_out=transform(df)
    load(df_out,index)

# main()
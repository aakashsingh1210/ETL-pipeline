from structurized.extract import extract
from structurized.transform import transform
from structurized.load import load
# import sys


def main(index):
    paths=extract()          # calling extract function and sending the obtained dataframe to 
    df=transform(paths)     # transform function and then finally loading the dataframe in csv 
    load(df,index)             # format to the google cloud


# def main_code2():
#     print("hello main_code has been printed")
# main_code()
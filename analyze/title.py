# 만든이 : 정종민
from numpy.core.numeric import nan
import pandas as pd
import csv
import numpy as np

file_list = ["groom","inflearn"]
python_df = pd.DataFrame()
java_df = pd.DataFrame()
c_df = pd.DataFrame()


for file_name in file_list:
    df =  pd.read_csv(f"./data/{file_name}.csv" , encoding = 'utf-8')
    python_list = ["Python","파이썬"]
    java_list = ["Java","자바"]
    c_list = ["C언어","C#","C\+\+"]
    etc_list = python_list + java_list + c_list


    for key in python_list:
        condition = df['title'].str.contains(key,na=False)
        temp_df = df[condition]
        # temp2_df = df.drop_duplicates('title',keep ='first')
        python_df = python_df.append(temp_df,ignore_index=True)
        python_df["subject"] = "파이썬"
        python_df["name"] = f"{file_name}"


    for key in java_list:
        condition = df['title'].str.contains(key,na=False) 
        temp_df = df[condition]
        java_df = java_df.append(temp_df,ignore_index=True)
        java_df["subject"] = "자바"
        java_df["name"] = f"{file_name}"


    for key in c_list:
        condition = df['title'].str.contains(key,na=False) 
        temp_df = df[condition]
        c_df = c_df.append(temp_df,ignore_index=True)
        c_df["subject"] = "C언어"
        c_df["name"] = f"{file_name}"



    # print(python_df)
    # print(java_df)
    # print(c_df)


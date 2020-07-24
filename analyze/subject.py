# 만든이 : 정종민
from numpy.core.numeric import nan
import pandas as pd
import numpy as np

file_list = [
    "groom",
    "inflearn",
    "geek",
    "edwith",
    "kocw",
    "programmers",
    "sangco",
]
for file_name in file_list:
    python_df = pd.DataFrame()
    java_df = pd.DataFrame()
    c_df = pd.DataFrame()

    df = pd.read_csv(f"./data/{file_name}.csv", encoding="utf-8")
    python_list = ["Python", "파이썬", "python"]
    java_list = ["Java", "자바", "JAVA", "java"]
    c_list = ["C언어", "C#", "C\+\+", "c\+\+", "c#", "c언어"]

    for key in python_list:
        python_df["site"] = f"{file_name}"
        condition = df["title"].str.contains(key, na=False)
        temp_df = df[condition]
        # temp2_df = df.drop_duplicates('title',keep ='first')
        python_df = python_df.append(temp_df, ignore_index=True)
        python_df["subject"] = "파이썬"

    python_df.to_csv(f"analyze_data/python/python_{file_name}.csv", index=False)

    for key in java_list:
        java_df["site"] = f"{file_name}"
        condition = df["title"].str.contains(key, na=False)
        temp_df = df[condition]
        java_df = java_df.append(temp_df, ignore_index=True)
        java_df["subject"] = "자바"

    java_df.to_csv(f"analyze_data/java/java_{file_name}.csv", index=False)

    for key in c_list:
        c_df["site"] = f"{file_name}"
        condition = df["title"].str.contains(key, na=False)
        temp_df = df[condition]
        c_df = c_df.append(temp_df, ignore_index=True)
        c_df["subject"] = "C언어"
    c_df.to_csv(f"analyze_data/c/c_{file_name}.csv", index=False)

    all_df = pd.DataFrame()
    all_df = all_df.append(python_df, ignore_index=True)
    all_df = all_df.append(java_df, ignore_index=True)
    all_df = all_df.append(c_df, ignore_index=True)
    all_df.to_csv(f"analyze_data/all/all_{file_name}.csv", index=False)

    etc_df = pd.DataFrame()

    condition = df["title"].isin(all_df["title"])
    temp_df = df[condition == False]
    etc_df = etc_df.append(temp_df, ignore_index=True)
    etc_df["site"] = f"{file_name}"

    etc_df.to_csv(f"analyze_data/etc/etc_{file_name}.csv", index=False)

    # print(etc_df)


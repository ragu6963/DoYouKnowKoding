# 만든이 : 정종민
# 주 언어별 사이트 합계 필터
from numpy.core.numeric import nan
import pandas as pd
import numpy as np


def filter_all(file_list, python_list, java_list, c_list):
    python_df = pd.DataFrame()
    java_df = pd.DataFrame()
    c_df = pd.DataFrame()

    for file_name in file_list:
        df = pd.read_csv(f"crawling_data/{file_name}.csv", encoding="utf-8")

        for key in python_list:
            condition = df["title"].str.lower().str.contains(key, na=False)
            temp_df = df[condition]
            python_df = python_df.append(temp_df, ignore_index=True)
            python_df = python_df.drop_duplicates(
                ["title", "college"], keep="first"
            )

        for key in java_list:
            condition = df["title"].str.lower().str.contains(key, na=False)
            condition2 = (
                df["title"].str.lower().str.contains("javascript", na=False)
            )
            condition3 = (
                df["title"].str.lower().str.contains("자바스크립트", na=False)
            )

            temp_df = df[
                condition & (condition2 == False) & (condition3 == False)
            ]
            java_df = java_df.append(temp_df, ignore_index=True)
            java_df = java_df.drop_duplicates(
                ["title", "college"], keep="first"
            )

        for key in c_list:
            condition = df["title"].str.lower().str.contains(key, na=False)
            temp_df = df[condition]
            c_df = c_df.append(temp_df, ignore_index=True)
            c_df = c_df.drop_duplicates(["title", "college"], keep="first")

    python_df["subject"] = "파이썬"
    python_df.to_csv(f"analyze_data/python/python_all.csv", index=False)

    java_df["subject"] = "자바"
    java_df.to_csv(f"analyze_data/java/java_all.csv", index=False)

    c_df["subject"] = "C언어"
    c_df.to_csv(f"analyze_data/c/c_all.csv", index=False)


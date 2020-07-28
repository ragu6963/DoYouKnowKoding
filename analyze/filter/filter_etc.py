# 만든이 : 정종민
# 기타 언어 사이트별 필터 및 사이트 합계 필터
from numpy.core.numeric import nan
import pandas as pd
import numpy as np


def filter_etc(file_list, python_list, java_list, c_list):
    etc_all_df = pd.DataFrame()
    for file_name in file_list:

        df = pd.read_csv(f"crawling_data/{file_name}.csv", encoding="utf-8")

        python_df = pd.DataFrame()
        java_df = pd.DataFrame()
        c_df = pd.DataFrame()
        etc_df = pd.DataFrame({"site": []})

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
        all_df = pd.DataFrame()
        all_df = all_df.append(python_df, ignore_index=True)
        all_df = all_df.append(java_df, ignore_index=True)
        all_df = all_df.append(c_df, ignore_index=True)

        condition = df["title"].isin(all_df["title"])
        temp_df = df[condition == False]
        etc_df = etc_df.append(temp_df, ignore_index=True)
        etc_df = etc_df.drop_duplicates("title", keep="first")
        etc_df["subject"] = "기타"
        etc_df["site"] = f"{file_name}"

        etc_df.to_csv(f"analyze_data/etc/etc_{file_name}.csv", index=False)

        etc_all_df = etc_all_df.append(etc_df, ignore_index=True)

    etc_all_df = etc_all_df.drop_duplicates("title", keep="first")
    etc_all_df["subject"] = "기타"
    etc_all_df.to_csv(f"analyze_data/etc/etc_all.csv", index=False)


# 만든이 : 정종민
# 사이트별 주 언어 필터
from numpy.core.numeric import nan
import pandas as pd
import numpy as np


def filter_site(file_list, python_list, java_list, c_list):
    for file_name in file_list:

        df = pd.read_csv(f"crawling_data/{file_name}.csv", encoding="utf-8")

        python_df = pd.DataFrame({"site": []})
        java_df = pd.DataFrame({"site": []})
        c_df = pd.DataFrame({"site": []})
        all_df = pd.DataFrame()

        for key in python_list:
            condition = df["title"].str.lower().str.contains(key, na=False)
            temp_df = df[condition]
            python_df = python_df.append(temp_df, ignore_index=True)
            python_df = python_df.drop_duplicates(
                ["title", "college"], keep="first"
            )

        python_df["subject"] = "파이썬"
        all_df = all_df.append(python_df, ignore_index=True)

        python_df["site"] = f"{file_name}"
        python_df.to_csv(
            f"analyze_data/python/python_{file_name}.csv", index=False
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

        java_df["site"] = f"{file_name}"
        java_df["subject"] = "자바"
        all_df = all_df.append(java_df, ignore_index=True)

        java_df.to_csv(f"analyze_data/java/java_{file_name}.csv", index=False)

        for key in c_list:
            condition = df["title"].str.lower().str.contains(key, na=False)
            temp_df = df[condition]
            c_df = c_df.append(temp_df, ignore_index=True)
            c_df = c_df.drop_duplicates(["title", "college"], keep="first")

        c_df["site"] = f"{file_name}"
        c_df["subject"] = "C언어"
        all_df = all_df.append(c_df, ignore_index=True)

        c_df.to_csv(f"analyze_data/c/c_{file_name}.csv", index=False)

        all_df["site"] = f"{file_name}"
        all_df.to_csv(f"analyze_data/all/all_{file_name}.csv", index=False)


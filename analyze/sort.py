# 만든이 : 김민재
import pandas as pd

file_list = ["inflearn", "edwith", "geek", "groom", "kocw", "programmers"]
for file_name in file_list:
    df = pd.read_csv(f"./data/{file_name}.csv")
    temp_dict = {}
    temp_dict["name"] = file_name
    # print(df)

    an_view = df.sort_values(by=["view"], axis=0, ascending=False)
    # print(an_view)

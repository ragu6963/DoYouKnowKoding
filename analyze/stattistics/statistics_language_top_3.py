# 만든이 : 정우영
# %%
import pandas as pd
import numpy as np

# %%
language_list = ["python", "java", "c"]

# %%
temp_df = pd.DataFrame({"subject": [],})
no_free_df = pd.DataFrame()
free_df = pd.DataFrame()

top_3_lecture = pd.DataFrame()
for language_name in language_list:
    df = pd.read_csv(
        f"../../analyze_data/{language_name}/{language_name}_all.csv"
    )
    temp_dict = {}
    temp_dict["subject"] = language_name
    sort_df = df.sort_values(["view"], ascending=False)[:4]
    top_3_lecture = top_3_lecture.append(sort_df, ignore_index=True)

    # temp_series = pd.Series(temp_dict)
    # temp_df = temp_df.append(temp_series, ignore_index=True)

top_3_lecture
top_3_lecture.to_csv("top_3_lecture.csv", index=False)


# %%

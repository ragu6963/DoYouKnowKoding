# 만든이 : 정우영
# %%
import pandas as pd
import numpy as np

# %%
language_list = ["python", "java", "c", "etc"]

# %%
temp_df = pd.DataFrame(
    {
        "subject": [],
        "lec_sum": [],
        "view_max": [],
        "view_min": [],
        "view_sum": [],
        "view_mean": [],
        "view_std": [],
        "price_max": [],
        "price_min": [],
        "price_mean": [],
        "price_std": [],
    }
)
for language_name in language_list:
    df = pd.read_csv(f"../analyze_data/{language_name}/{language_name}_all.csv")
    temp_dict = {}
    temp_dict["subject"] = language_name

    # 강의 수
    lec_sum = df.shape[0]
    lec_sum
    temp_dict["lec_sum"] = lec_sum

    # view 최댓값
    # view_max = df["view"].max()
    # temp_dict["view_max"] = view_max

    # view 최솟값
    # view_min = df["view"].min()
    # temp_dict["view_min"] = view_min

    # view 합계
    # view_sum = df["view"].sum()
    # temp_dict["view_sum"] = view_sum

    # view 평균
    view_mean = int(df["view"].mean())
    temp_dict["view_mean"] = view_mean

    # view 표준편차
    view_std = df["view"].std()
    temp_dict["view_std"] = view_std

    columns_list = df.columns

    price_df = df[df.price != 0]
    # price 최댓값
    price_max = price_df["price"].max()
    temp_dict["price_max"] = price_max

    # price 최솟값
    price_min = price_df["price"].min()
    temp_dict["price_min"] = price_min

    # price 평균
    price_mean = price_df["price"].mean()
    temp_dict["price_mean"] = price_mean

    # price 표준편차
    price_std = price_df["price"].std()
    temp_dict["price_std"] = price_std

    # if "like" in columns_list:
    #     # like 최댓값
    #     like_max = df["like"].max()
    #     temp_dict["like_max"] = like_max

    #     # like 최솟값
    #     like_min = df["like"].min()
    #     temp_dict["like_min"] = like_min

    #     # like 평균
    #     like_mean = int(df["like"].mean())
    #     temp_dict["like_mean"] = like_mean

    #     # like 표준편차
    #     like_std = df["like"].std()
    #     temp_dict["like_std"] = like_std

    # else:
    #     like_mean = np.nan

    # if "score" in columns_list:
    #     # score 최댓값
    #     score_max = df["score"].max()
    #     temp_dict["score_max"] = score_max
    #     # score 최솟값
    #     score_min = df["score"].min()
    #     temp_dict["score_min"] = score_min

    #     # score 평균
    #     df["score"] = np.where(df["score"] == -1, np.nan, df["score"])
    #     score_mean = int(df["score"].mean())
    #     temp_dict["score_mean"] = score_mean

    #     # score 표준편차
    #     score_std = df["score"].std()
    #     temp_dict["score_std"] = score_std
    # else:
    #     score_mean = np.nan

    temp_series = pd.Series(temp_dict)
    temp_df = temp_df.append(temp_series, ignore_index=True)

temp_df


# %%

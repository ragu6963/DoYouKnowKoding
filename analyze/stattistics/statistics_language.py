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
no_free_df = pd.DataFrame()
free_df = pd.DataFrame()

for language_name in language_list:
    df = pd.read_csv(
        f"../../analyze_data/{language_name}/{language_name}_all.csv"
    )
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

    # 유료강의 무료강의 나누기
    # 기타 강의 제외
    if language_name != "etc":
        temp_free_df = df[df.price == 0]
        free_df = free_df.append(temp_free_df)
        free_df = free_df.append(df[df.price.isnull()])

        temp_no_free_df = df[df.price > 0]
        no_free_df = no_free_df.append(temp_no_free_df)

    python_free_df = free_df[free_df.subject == "파이썬"]
    java_free_df = free_df[free_df.subject == "자바"]
    c_free_df = free_df[free_df.subject == "C언어"]

    python_no_free_df = no_free_df[no_free_df.subject == "파이썬"]
    java_no_free_df = no_free_df[no_free_df.subject == "자바"]
    c_no_free_df = no_free_df[no_free_df.subject == "C언어"]
temp_df
# free_df


# %%
# 무료 유료 평균 조회수 비교
import plotly.graph_objects as go


langauge = ["파이썬", "자바", "C언어"]
free_view_mean_list = [
    free_df[free_df.subject == "파이썬"].view.mean(),
    free_df[free_df.subject == "자바"].view.mean(),
    free_df[free_df.subject == "C언어"].view.mean(),
]
no_free_view_mean_list = [
    no_free_df[no_free_df.subject == "파이썬"].view.mean(),
    no_free_df[no_free_df.subject == "자바"].view.mean(),
    no_free_df[no_free_df.subject == "C언어"].view.mean(),
]

fig = go.Figure(
    data=[
        go.Bar(name="무료", x=langauge, y=free_view_mean_list),
        go.Bar(name="유료", x=langauge, y=no_free_view_mean_list),
    ],
)
fig.update_layout(barmode="group")
fig.show()


# %%
# 무료 유료 강의 수 비교
import plotly.graph_objects as go

langauge = ["파이썬", "자바", "C언어"]
free_lec_sum_list = [
    free_df[free_df.subject == "파이썬"].shape[0],
    free_df[free_df.subject == "자바"].shape[0],
    free_df[free_df.subject == "C언어"].shape[0],
]
no_free_lec_sum_list = [
    no_free_df[no_free_df.subject == "파이썬"].shape[0],
    no_free_df[no_free_df.subject == "자바"].shape[0],
    no_free_df[no_free_df.subject == "C언어"].shape[0],
]

fig = go.Figure(
    data=[
        go.Bar(
            name="무료",
            x=langauge,
            y=free_lec_sum_list,
            text=free_lec_sum_list,
            textposition="auto",
        ),
        go.Bar(
            name="유료",
            x=langauge,
            y=no_free_lec_sum_list,
            text=no_free_lec_sum_list,
            textposition="auto",
        ),
    ],
)
# fig.update_traces(texttemplate="%{text:.2s}", textposition="outside")
# fig.update_layout(uniformtext_minsize=8, uniformtext_mode="hide")
fig.update_layout(barmode="group")
fig.show()
# fig.write_html("../static/images/charts/file.html")
# %%
# 강의 수 비교
import plotly.graph_objects as go

barchart_df = temp_df[temp_df.subject != "etc"]
fig = go.Figure([go.Bar(x=barchart_df.subject, y=barchart_df.lec_sum)])
fig.show()


# %%


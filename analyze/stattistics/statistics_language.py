# 만든이 : 정우영
# %%
import pandas as pd
import numpy as np

# %%
language_list = ["python", "java", "c"]

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
    view_max = df["view"].max()
    temp_dict["view_max"] = view_max

    # view 최솟값
    view_min = df["view"].min()
    temp_dict["view_min"] = view_min

    # view 합계
    view_sum = df["view"].sum()
    temp_dict["view_sum"] = view_sum

    # view 평균
    view_mean = int(df["view"].mean())
    temp_dict["view_mean"] = view_mean

    # view 표준편차
    view_std = df["view"].std()
    temp_dict["view_std"] = view_std

    columns_list = df.columns

    price_df = df[df.price > 0]
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

    temp_series = pd.Series(temp_dict)
    temp_df = temp_df.append(temp_series, ignore_index=True)

    # 유료강의 무료강의 나누기
    # 기타 강의 제외
    # if language_name != "etc":
    #     temp_free_df = df[df.price == 0]
    #     free_df = free_df.append(temp_free_df)
    #     free_df = free_df.append(df[df.price.isnull()])

    #     temp_no_free_df = df[df.price > 0]
    #     no_free_df = no_free_df.append(temp_no_free_df)

    # python_free_df = free_df[free_df.subject == "파이썬"]
    # java_free_df = free_df[free_df.subject == "자바"]
    # c_free_df = free_df[free_df.subject == "C언어"]

    # python_no_free_df = no_free_df[no_free_df.subject == "파이썬"]
    # java_no_free_df = no_free_df[no_free_df.subject == "자바"]
    # c_no_free_df = no_free_df[no_free_df.subject == "C언어"]
temp_df
# %%
import plotly.graph_objects as go

langauge = ["Python", "Java", "C language"]
view_mean_list = temp_df["view_mean"]
view_std_list = temp_df["view_std"]

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=langauge,
        y=view_mean_list,
        name="조회수 평균",
        marker_color="#4C92F5",
        marker_line_color="rgb(8,48,107)",
        marker_line_width=2,
        opacity=0.6,
        showlegend=True,
    )
)

fig.add_trace(
    go.Bar(
        x=langauge,
        y=view_std_list,
        name="조회수 표준편차",
        marker_color="rgb(245, 76, 76)",
        marker_line_color="rgb(107, 8, 8)",
        marker_line_width=2,
        opacity=0.6,
        showlegend=True,
    )
)

fig.update_layout(legend=dict(yanchor="top", xanchor="right", x=0.6, y=0.99))
fig.update_layout(barmode="group")
fig.show()
# %%
# 가격 평균 및 표준편차
import plotly.graph_objects as go

langauge = ["Python", "Java", "C language"]
price_mean_list = temp_df["price_mean"]
price_std_list = temp_df["price_std"]

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=langauge,
        y=price_mean_list,
        name="가격 평균",
        marker_color="#4C92F5",
        marker_line_color="rgb(8,48,107)",
        marker_line_width=2,
        opacity=0.6,
        showlegend=True,
    )
)

fig.add_trace(
    go.Bar(
        x=langauge,
        y=price_std_list,
        name="가격 표준편차",
        marker_color="rgb(245, 76, 76)",
        marker_line_color="rgb(107, 8, 8)",
        marker_line_width=2,
        opacity=0.6,
        showlegend=True,
    )
)

fig.update_layout(legend=dict(yanchor="top", xanchor="right", x=0.6, y=0.99))
fig.update_layout(barmode="group")
fig.show()


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
# 무료 유료 총 강의 수 비교

import plotly.graph_objects as go

langauge = ["Python", "Java", "C language"]

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
lanugage_lec_sum_df = temp_df[temp_df.subject != "etc"]

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=langauge,
        y=lanugage_lec_sum_df.lec_sum,
        name="총 강의수",
        marker_color="#4C92F5",
        marker_line_color="rgb(8,48,107)",
        marker_line_width=2,
        opacity=0.6,
        showlegend=True,
    )
)
fig.add_trace(
    go.Bar(
        x=langauge,
        y=free_lec_sum_list,
        name="무료 강의수",
        marker_color="rgb(76, 245, 118)",
        marker_line_color="rgb(8, 107, 31)",
        marker_line_width=2,
        opacity=0.6,
        showlegend=True,
    )
)

fig.add_trace(
    go.Bar(
        x=langauge,
        y=no_free_lec_sum_list,
        name="유료 강의수",
        marker_color="rgb(245, 76, 76)",
        marker_line_color="rgb(107, 8, 8)",
        marker_line_width=2,
        opacity=0.6,
        showlegend=True,
    )
)
fig.update_layout(legend=dict(yanchor="top", xanchor="right", x=0.99, y=0.99))
fig.update_layout(barmode="group")
fig.show()
# %%
# 강의 수 비교
import plotly.graph_objects as go

langauge = ["Python", "Java", "C language"]
lanugage_lec_sum_df = temp_df[temp_df.subject != "etc"]

fig = go.Figure(data=[go.Bar(x=langauge, y=lanugage_lec_sum_df.lec_sum,)],)
fig.update_traces(
    marker_color="#4C92F5",
    marker_line_color="rgb(8,48,107)",
    marker_line_width=2,
    opacity=0.6,
    name="강의수",
    showlegend=True,
)

fig.update_layout(legend=dict(yanchor="top", xanchor="right", x=0.99, y=0.99))
fig.show()


# %%


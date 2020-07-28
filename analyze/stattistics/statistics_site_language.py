# 만든이 : 정우영
# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


# %%
file_list = [
    "inflearn",
    "edwith",
    "groom",
    "gseek",
    "programmers",
    "sangco",
    "kocw",
]
language_list_df = []
subject_list = ["python", "java", "c"]
for subject in subject_list:
    temp_df = pd.DataFrame(
        {
            "site": [],
            "lec_sum": [],
            "view_max": [],
            "view_sum": [],
            "view_mean": [],
            "subject": [],
        }
    )
    for file_name in file_list:
        df = pd.read_csv(
            f"../../analyze_data/{subject}/{subject}_{file_name}.csv"
        )

        if df["site"].count() == 0:
            continue

        temp_dict = {}

        temp_dict["subject"] = subject
        if (
            file_name == "inflearn"
            or file_name == "groom"
            or file_name == "programmers"
        ):
            temp_dict["site"] = file_name + "<br>유료"
        else:
            temp_dict["site"] = file_name + "<br>무료"

        # 강의 수
        lec_sum = df.shape[0]
        lec_sum
        temp_dict["lec_sum"] = lec_sum

        # 조회수 합계
        view_max = df["view"].max()
        view_max
        temp_dict["view_max"] = view_max

        # 조회수 합계
        view_sum = df["view"].sum()
        view_sum
        temp_dict["view_sum"] = view_sum

        # 평균
        view_mean = int(df["view"].mean())
        view_mean
        temp_dict["view_mean"] = view_mean
        temp_series = pd.Series(temp_dict)
        temp_df = temp_df.append(temp_series, ignore_index=True)

    language_list_df.append(temp_df)
# %%
language_list_df[1]

# %%
# 언어별 사이트마다 총 조회수와 강의 수
# 조회수 line 강의수 bar
for langauge_df in language_list_df:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    langauge = langauge_df["subject"][0]
    temp_df = langauge_df
    view_sum = temp_df["view_sum"]
    lec_sum = temp_df["lec_sum"]

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(
        go.Bar(
            x=temp_df["site"],
            y=lec_sum,
            name="강의수",
            marker_color="#4C92F5",
            marker_line_color="rgb(8,48,107)",
            marker_line_width=2,
            opacity=0.6,
        ),
        secondary_y=True,
    )
    fig.add_trace(
        go.Scatter(
            x=temp_df["site"],
            y=view_sum,
            name="총 조회수",
            marker_color="rgb(245, 76, 76,255)",
            marker_line_color="rgb(107, 8, 8,255)",
            marker_line_width=2,
            opacity=0.6,
        ),
        secondary_y=False,
    )

    fig.update_yaxes(title_text=f"<b>총 조회수</br>", secondary_y=False)
    fig.update_yaxes(title_text="<b>강의수</b>", secondary_y=True)
    fig.update_layout(
        legend=dict(yanchor="top", xanchor="right", x=0.55, y=0.95)
    )
    print(f"{langauge}")
    fig.show()
# %%
# 언어별 각 사이트 최대 조회수
for langauge_df in language_list_df:
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    langauge = langauge_df["subject"][0]
    temp_df = langauge_df

    view_max = temp_df["view_max"]
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=temp_df["site"],
            y=view_max,
            name="최대조회수",
            marker_color="#4C92F5",
            marker_line_color="rgb(8,48,107)",
            marker_line_width=2,
            opacity=0.6,
            showlegend=True,
        ),
    )
    fig.update_layout(
        legend=dict(yanchor="top", xanchor="right", x=0.55, y=0.95)
    )
    print(f"{langauge}")
    fig.show()


# %%

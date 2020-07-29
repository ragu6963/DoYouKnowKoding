# 만든이 : 정우영
# %%
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# %%
file_list = [
    "kocw",
]

# %%
temp_df = pd.DataFrame()
subject = "all"

df = pd.read_csv(f"../../analyze_data/all/all_kocw.csv")
college_count_df = pd.DataFrame()
count_dict = {}
for i, row in df.iterrows():
    if row.college in count_dict:
        count_dict[row.college] += 1
    else:
        count_dict[row.college] = 1

for k, v in count_dict.items():
    temp_dict = {"college": k, "count": v}
    college_count_df = college_count_df.append(temp_dict, ignore_index=True)

sort_count_df = college_count_df.sort_values("count", ascending=False)
# 기준 이하 제거
sort_count_df = sort_count_df[sort_count_df["count"] >= 2]

# %%
# plotly
import chart_studio.plotly
import cufflinks as cf

cf.go_offline(connected=True)

# %%
# 가로 차트
import plotly.graph_objects as go
import plotly.express as px

fig = go.Figure()
fig.add_trace(go.Bar(x=sort_count_df["college"], y=sort_count_df["count"]))
fig.update_layout(barmode="group", xaxis_tickangle=-45)
fig.show()

# %%
import plotly.graph_objects as go

x = sort_count_df["college"]
y = sort_count_df["count"]
fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=x,
        y=y,
        text=y,
        textfont=dict(size=12, color="RGB(255,255,255)"),
        textposition="auto",
        name="강의수",
        marker_color="#4C92F5",
        marker_line_color="rgb(8,48,107)",
        marker_line_width=2,
        opacity=0.6,
        showlegend=True,
    ),
)
fig.update_layout(legend=dict(yanchor="top", xanchor="right", x=0.99, y=0.99))
fig.update_layout(barmode="group", xaxis_tickangle=-45)
fig.show()


# %%

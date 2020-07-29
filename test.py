#%%
# %%
import pandas as pd
import numpy as np

#%%
import plotly.graph_objects as go

langauge_list = ["Python", "Java", "C", "C++", "C#"]
stack_list = [41.7, 41.1, 20.6, 23.5, 31.0]
github_list = [14.2, 10.7, 3.9, 8.8, 3.9]
pypl_list = [31.7, 17.1, 5.9, 5.9, 6.7]

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=langauge_list,
        y=stack_list,
        name="Stack Overflow 2019",
        marker_color="rgb(245, 76, 76,255)",
        marker_line_color="rgb(107, 8, 8,255)",
        marker_line_width=3,
        opacity=0.6,
        showlegend=True,
    ),
)
fig.add_trace(
    go.Scatter(
        x=langauge_list,
        y=github_list,
        name="github push 2020 Q2",
        marker_color="#4C92F5",
        marker_line_color="rgb(8,48,107)",
        marker_line_width=3,
        opacity=0.6,
        showlegend=True,
    ),
)
fig.add_trace(
    go.Scatter(
        x=langauge_list,
        y=pypl_list,
        name="pypl 2020 07",
        marker_color="rgb(76, 245, 118)",
        marker_line_color="rgb(8, 107, 31)",
        marker_line_width=3,
        opacity=0.6,
        showlegend=True,
    ),
)
fig.update_layout(legend=dict(yanchor="top", xanchor="right", x=0.99, y=0.99))
fig.show()  # %%


# %%

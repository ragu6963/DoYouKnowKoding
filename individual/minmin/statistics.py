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
temp_df = pd.DataFrame(
    {
        "site": [],
        "lec_sum": [],
        "view_sum": [],
        "view_mean": [],
        "price_mean": [],
        "like_mean": [],
        "score_mean": [],
    }
)
subject = "c"
for file_name in file_list:
    df = pd.read_csv(f"../../analyze_data/{subject}/{subject}_{file_name}.csv")

    if df["site"].count() == 0:
        continue

    temp_dict = {}

    temp_dict["site"] = file_name

    # 강의 수
    lec_sum = df.shape[0]
    lec_sum
    temp_dict["lec_sum"] = lec_sum

    # 합계
    view_sum = df["view"].sum()
    view_sum
    temp_dict["view_sum"] = view_sum

    # 평균
    view_mean = int(df["view"].mean())
    view_mean
    temp_dict["view_mean"] = view_mean

    columns_list = df.columns

    price_mean = 0

    # price 평균
    if df["price"].isnull().sum() == 0:
        # price가 0이 아닌 것
        price_df = df[df.price != 0]
        price_mean = int(price_df["price"].mean())
        temp_dict["price_mean"] = price_mean
    else:
        temp_dict["price_mean"] = np.nan

    # like 평균
    if df["like"].isnull().sum() == 0:
        like_mean = int(df["like"].mean())
        temp_dict["like_mean"] = like_mean
    else:
        temp_dict["like_mean"] = np.nan

    # score 평균
    if df["score"].isnull().sum() == 0:
        like_df = df[df.score != -1]
        score_mean = like_df["score"].mean()
        temp_dict["score_mean"] = score_mean
    else:
        temp_dict["score_mean"] = np.nan

    temp_series = pd.Series(temp_dict)
    temp_df = temp_df.append(temp_series, ignore_index=True)

temp_df


# %%
# 그래프 강의수
site_view_sum = pd.DataFrame()
site_view_sum["site"] = temp_df["site"]
site_view_sum["view_sum"] = temp_df["view_sum"]
site_view_sum
fig = plt.figure()
plt.bar(site_view_sum["site"], site_view_sum["view_sum"])
plt.show()


# %%
# 사이트별 강의수(pie그래프)
import plotly.graph_objects as go

site_lec_sum = pd.DataFrame()
site_lec_sum["site"] = temp_df["site"]
site_lec_sum["lec_sum"] = temp_df["lec_sum"]

labels = site_lec_sum["site"]
values = site_lec_sum["lec_sum"]


fig = go.Figure(
    data=[
        go.Pie(
            labels=labels,
            values=values,
            textinfo="label+percent",
            insidetextorientation="radial",
        )
    ]
)

fig.show()


# %%
# 사이트별 강의수와 조회수 비교
plt.rcParams["font.family"] = "NanumBarunGothic"
plt.rcParams["font.size"] = 10
plt.rcParams["figure.figsize"] = (10, 4)

site_view_mean = pd.DataFrame()
site_view_mean["site"] = temp_df["site"]
site_view_mean["lec_sum"] = temp_df["lec_sum"]
site_view_mean["view_mean"] = temp_df["view_mean"]


x = site_view_mean["site"]
y1 = site_view_mean["lec_sum"]
y2 = site_view_mean["view_mean"]

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()


line1 = ax1.bar(x, y1, alpha=0.5)
line2 = ax2.plot(x, y2, "go--", color="green")

plt.legend((line1[0], line2[0]), ("강의수", "조회수"), loc="upper center")
plt.grid(True, alpha=0.5)

plt.show()

# %%


# %%

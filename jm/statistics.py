# 만든이 : 정우영
# %%
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.graph_objects as go
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
# %%
temp_df = pd.DataFrame(
    {
        "site": [],
        "lec_sum": [],
        "view_sum": [],
        "view_max": [],
        "view_mean": [],
        "price_mean": [],
        "like_mean": [],
        "score_mean": [],
        "title" : [],
    }
)
subject = "c"
for file_name in file_list:
    df = pd.read_csv(f"../analyze_data/{subject}/{subject}_{file_name}.csv")

    if df["site"].count() == 0:
        continue

    temp_dict = {}

    temp_dict["site"] = file_name

    # 강의 수
    lec_sum = df.shape[0]
    lec_sum
    temp_dict["lec_sum"] = lec_sum

    # 합계
    # view_sum = df["view"].sum()
    # view_sum
    # temp_dict["view_sum"] = view_sum

    # 평균
    view_mean = int(df["view"].mean())
    view_mean
    temp_dict["view_mean"] = view_mean

     # view 최댓값
    view_max = df["view"].max()
    temp_dict["view_max"] = view_max


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

# temp_df

# %%
# 그래프 총 조회수

site_view_sum = pd.DataFrame()
site_view_sum["site"] = temp_df["site"]
site_view_sum["view_sum"] = temp_df["view_sum"]
site_view_sum
fig = plt.figure()
plt.bar(site_view_sum["site"], site_view_sum["view_sum"])
plt.show()

# %%
# 그래프 강의 수
site_lec_sum = pd.DataFrame()
site_lec_sum["site"] = temp_df["site"]
site_lec_sum["lec_sum"] = temp_df["lec_sum"]
site_lec_sum
fig = plt.figure()
plt.bar(site_lec_sum["site"], site_lec_sum["lec_sum"])
plt.show()
# %%
# 그래프 평균 조회수
site_view_mean = pd.DataFrame()
site_view_mean["site"] = temp_df["site"]
site_view_mean["view_mean"] = temp_df["view_mean"]
site_view_mean
fig = plt.figure()
plt.bar(site_view_mean["site"], site_view_mean["view_mean"])
plt.show()

# %%
site_score_mean = pd.DataFrame()
site_score_mean["site"] = temp_df["site"]
site_score_mean["score_mean"] = temp_df["score_mean"]
site_score_mean
fig = plt.figure()
plt.bar(site_score_mean["site"], site_score_mean["score_mean"])
plt.show()

# %%
site_like_mean = pd.DataFrame()
site_like_mean["site"] = temp_df["site"]
site_like_mean["like_mean"] = temp_df["like_mean"]
site_like_mean
fig = plt.figure()
plt.bar(site_like_mean["site"], site_like_mean["like_mean"])
plt.show()


# %%
# site_like_sum_division_view_sum = pd.DataFrame()
# site_like_sum_division_view_sum["site"] = temp_df["site"]
# site_like_sum_division_view_sum["like_sum_division_view_sum"] = temp_df[
#     "like_sum_division_view_sum"
# ]
# site_like_sum_division_view_sum
# fig = plt.figure()
# plt.bar(
#     site_like_sum_division_view_sum["site"],
#     site_like_sum_division_view_sum["like_sum_division_view_sum"],
# )
# plt.show()


# %%
# plotly
import chart_studio.plotly
import cufflinks as cf

cf.go_offline(connected=True)

# %%
# 가로 차트
import plotly.graph_objects as go
import plotly.express as px

site_lec_sum = pd.DataFrame()
site_lec_sum["site"] = temp_df["site"]
site_lec_sum["lec_sum"] = temp_df["lec_sum"]

fig = go.Figure()
config = {"staticPlot": True}
# fig = px.bar(site_lec_sum, x="lec_sum", y="site")
# fig.show()
fig.add_trace(go.Bar(x=site_lec_sum["site"], y=site_lec_sum["lec_sum"]))
fig.show(config=config)
# fig.write_html("file.html")

# %%
# 가로 누적 차트
import plotly.express as px

all_view_mean = pd.DataFrame(
    {
        "조회수평균": ["0", "0", "0", "0", "0", "0", "0"],
        "site": temp_df.sort_values(by=["view_mean"], axis=0)["site"][:],
        "view_mean": temp_df.sort_values(by=["view_mean"], axis=0)["view_mean"][:],
    }
)

fig = px.bar(all_view_mean, x="view_mean", y="조회수평균", color="site", orientation="h", height=500)
fig.show(config=config)
fig.write_html("file.html")

# %%
# 세로 라벨 차트
site_lec_sum = pd.DataFrame()
site_lec_sum["site"] = temp_df["site"]
site_lec_sum["view_max"] = temp_df["view_max"]

x = site_lec_sum["site"]
y = site_lec_sum["view_max"]

# Use textposition='auto' for direct text
fig = go.Figure(data=[go.Bar(x=x, y=y, text=y, textposition="auto",)])

fig.show()


# %%
mpl.rc('font', family='NanumBarunGothic') #한글 폰트 설정
plt.figure(figsize=(10, 5))
plt.bar(temp_df['site'].astype(str),temp_df['lec_sum']) 
plt.xlabel('사이트')
plt.ylabel('강의 수')   
plt.show()


# %%
animals=['giraffes', 'orangutans', 'monkeys']

fig = go.Figure(data=[
    go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
    go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()


# %%
# 과목 별 조회 수 최대 값
# view 최댓값
mpl.rc('font', family='NanumBarunGothic') #한글 폰트 설정
plt.figure(figsize=(10, 5))
plt.bar(temp_df['site'].astype(str),temp_df['view_max']) 
plt.xlabel('사이트')
plt.ylabel('조회 수')
plt.grid(True,axis = 'y',alpha=0.25)
plt.show()


# %%

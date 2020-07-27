# 만든이 : 정우영
# %%
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np
import platform

# %%
file_list = [
    "inflearn",
    "edwith",
    "groom",
    "geek",
    "programmers",
    "sangco",
    "kocw",
]

# %%
temp_df = pd.DataFrame(
    {
        "site": [],
        "view_sum": [],
        "view_mean": [],
        "lec_sum": [],
        "price_mean": [],
        "like_mean": [],
        "score_mean": [],
    }
)
subject = "java"
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
    view_sum = df["view"].sum()
    view_sum
    temp_dict["view_sum"] = view_sum

    # 평균
    view_mean = int(df["view"].mean())
    view_mean
    temp_dict["view_mean"] = view_mean

    columns_list = df.columns

    price_mean = 0
    # 가격 평균
    if "price" in columns_list:
        price_mean = int(df["price"].mean())
        price_mean
        temp_dict["price_mean"] = price_mean
    else:
        price_mean = np.nan

    # 생활코딩용 좋아요 평균
    if "like" in columns_list:
        like_mean = int(df["like"].mean())
        like_mean
        temp_dict["like_mean"] = like_mean
    else:
        like_mean = np.nan

    # 평점 평균
    if "score" in columns_list:
        # condition = df["score"] == -1
        df["score"] = np.where(df["score"] == -1, np.nan, df["score"])
        score_mean = int(df["score"].mean())
        score_mean
        temp_dict["score_mean"] = score_mean
    else:
        score_mean = np.nan

    temp_series = pd.Series(temp_dict)
    temp_df = temp_df.append(temp_series, ignore_index=True)

temp_df

#  (java) site 별 조회 수 평균 그래프 

mpl.rc('font', family='NanumBarunGothic') #한글 폰트 설정
plt.figure(figsize=(10, 5))
plt.bar(temp_df['site'].astype(str),temp_df['view_mean']) 
plt.title('조회')
plt.xlabel('사이트')
plt.ylabel('조회 수')
plt.show()


# %%
#  (java) site 별 가격 평균 그래프 

mpl.rc('font', family='NanumBarunGothic') #한글 폰트 설정
plt.figure(figsize=(10, 5))
plt.bar(temp_df['site'].astype(str),temp_df['price_mean']) 
plt.title('사이트 별 가격평균')
plt.xlabel('사이트')
plt.ylabel('가격')
plt.show()

# 
    
# %%

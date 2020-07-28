# 만든이 김민재
import urllib.request
import urllib.parse
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import quote

gseek_df = pd.DataFrame(
    {"title": [], "view": [], "price": [], "score": [], "like": [], "college": [], "url": []}
)

main_url = "https://www.gseek.kr/learn/"
url_list = [
    "learn.list?SC_SC1_CODE=5e43e5e60905d&SC_SC2_CODE=5e43e62cf3e50",
    "learn.list?SC_SC1_CODE=5e43e5e60905d&SC_SC2_CODE=5e43e62d0bf28",
]

for url in url_list:
    with urllib.request.urlopen(main_url + url) as response:
        html = response.read().decode("utf8")
        soup = BeautifulSoup(html, "html.parser")

    cards = soup.select("div.card-lift--hover")
    for card in cards:
        link = card.select_one("a.web")["href"]

        with urllib.request.urlopen(main_url + link) as response:
            html = response.read().decode("utf8")
            soup = BeautifulSoup(html, "html.parser")

        title = soup.select_one("div > h3.line").get_text()
        print(title)
        trs = soup.select("table.web > tbody > tr")
        trs_len = len(trs)

        # 조회수 평균값
        total = 0
        for tr in trs:
            view = tr.select("td")[2].get_text().replace("회", "")
            total += int(view)

        print(total // trs_len)
        view = total // trs_len

        # 조회수 중간값
        # middle = trs_len//2
        # view = trs[middle].select("td")[2].get_text().replace("회","")
        # print(view)

        # 좋아요 평균값
        total = 0
        for tr in trs:
            like = tr.select("td")[3].get_text()
            total += int(like)

        print(total // trs_len)
        like = total // trs_len
        gseek_dict = {
            "title": title,
            "view": view,
            "price": np.nan,
            "score": np.nan,
            "like": like,
            "college": np.nan,
            "url": main_url + link,
        }
        gseek_series = pd.Series(gseek_dict)
        gseek_df = gseek_df.append(gseek_series, ignore_index=True)

gseek_df.to_csv("crawling_data/gseek.csv", index=False)

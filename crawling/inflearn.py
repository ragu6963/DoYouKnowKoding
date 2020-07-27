# 만든이 : 정우영

import urllib.request
import urllib.parse
import numpy as np
import json
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import quote

main_url = "https://www.inflearn.com"
inflearn_df = pd.DataFrame(
    {"title": [], "view": [], "price": [], "score": [], "like": [], "college": [], "url": []}
)
category_list = [
    ["https://www.inflearn.com/courses/it-programming?order=seq&page=", 25],
    ["https://www.inflearn.com/courses/data-science?order=seq&page=", 5],
]
for category_url, last_page in category_list:
    print(category_url)
    print(last_page)
    for i in range(1, last_page + 1):
        url = category_url + str(i)
        # print(url)
        with urllib.request.urlopen(url) as response:
            html = response.read().decode("utf8")
            soup = BeautifulSoup(html, "html.parser")

        cards = soup.select("div.card")

        for card in cards:
            inflearn_dict = {}
            card_url = card.select_one(".course_card_front")["href"]

            title = card.select_one(".course_title").get_text()

            price = str(json.loads(card["fxd-data"])["reg_price"]).replace(".0", "")

            content_url = main_url + quote(card_url)

            with urllib.request.urlopen(content_url) as response:
                html = response.read().decode("utf8")
                soup = BeautifulSoup(html, "html.parser")

            view = soup.select_one("small.student_cnt").get_text().split("명")[0]

            score = soup.select_one("span.average_num")
            if score is None:
                score = -1
            else:
                score = score.get_text()

            inflearn_dict = {
                "title": title,
                "view": view,
                "price": price,
                "score": score,
                "like": np.nan,
                "college": np.nan,
                "url": content_url,
            }
            inflearn_series = pd.Series(inflearn_dict)

            inflearn_df = inflearn_df.append(inflearn_series, ignore_index=True)
            print(title)

inflearn_df.to_csv("crawling_data/inflearn.csv", index=False)


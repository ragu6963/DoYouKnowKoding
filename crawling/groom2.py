# 정종민
import urllib.request
import urllib.parse
import json
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import quote

main_url = "https://edu.goorm.io/category/programming"
last_page = 17
groom_df = pd.DataFrame({"title": [], "price": [], "view": [], "score": []})

for i in range(1, last_page + 1):
    url = main_url + "?page=" + str(i) + "&sort=newest"

    with urllib.request.urlopen(url) as response:
        html = response.read().decode("utf8")
        soup = BeautifulSoup(html, "html.parser")

    cards = soup.select("div.card")
    for card in cards:

        title = card.select_one("div.kV2LiJ").get_text()
        price = card.select_one("span._3vh60A").get_text()
        if price == "무료":
            price = 0
        else:
            price = price.replace(",", "").replace("₩", "")

        score = card.select_one("span._2KWt9f").get_text()
        view = card.select_one("div._1kTxrO > span").get_text()
        print(title)

        groom_dict = {"title": title, "price": price, "view": view, "score": score}
        groom_series = pd.Series(groom_dict)

        groom_df = groom_df.append(groom_series, ignore_index=True)

groom_df.to_csv("crawling_data/groom.csv", index=False)


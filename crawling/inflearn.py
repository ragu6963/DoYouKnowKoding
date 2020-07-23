import urllib.request
import urllib.parse
import json
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import quote


main_url = "https://www.inflearn.com"
# last_page = 40
last_page = 2
inflearns = pd.DataFrame({"title": [], "price": [], "view": [], "score": []})

for i in range(1, last_page + 1):
    url = main_url + "/courses?order=seq&page=" + str(i)
    with urllib.request.urlopen(url) as response:
        html = response.read().decode("utf8")
        soup = BeautifulSoup(html, "html.parser")
    cards = soup.select("div.card")

    for card in cards[:1]:
        inflearn_dict = {}
        url = card.select_one(".course_card_front")["href"]
        title = card.select_one(".course_title").get_text()

        price = str(json.loads(card["fxd-data"])["reg_price"]).replace(".0", "")
        content_url = main_url + quote(url)

        inflearn_dict["title"] = title
        inflearn_dict["price"] = price

        with urllib.request.urlopen(content_url) as response:
            html = response.read().decode("utf8")
            soup = BeautifulSoup(html, "html.parser")

        view = soup.select_one(" small.student_cnt").get_text().split("명")[0]
        inflearn_dict["view"] = view

        score = soup.select_one("span.average_num")
        if score is None:
            score = -1
        else:
            score = score.get_text()

        inflearn_dict["score"] = score
        inflearn_df = pd.Series(inflearn_dict)

        inflearns = inflearns.append(inflearn_df, ignore_index=True)

inflearns.to_csv("./data/inflearns.csv", index=False)


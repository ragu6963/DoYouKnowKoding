# 만든이 : 정우영

import urllib.request
import urllib.parse
import pandas as pd
import numpy as np
import time
from bs4 import BeautifulSoup
from selenium import webdriver

programmers_dict = {}
programmers_df = pd.DataFrame(
    {"title": [], "view": [], "price": [], "score": [], "like": [], "college": [], "url": []}
)

driver = webdriver.Chrome("crawling/data/chromedriver")
driver.get("https://programmers.co.kr/learn?tag=%EB%AA%A8%EB%93%A0%20%EC%BD%94%EC%8A%A4")
time.sleep(3)
source = driver.page_source
items = driver.find_elements_by_xpath("/html/body/div[3]/div[3]/div[2]/li")
for item in items:
    item_text = item.text
    if not "정원" in item_text:
        title = item.find_element_by_class_name("title").text
        programmers_dict["title"] = title

        price = (
            item.find_element_by_xpath("a/div[3]/h5/span[2]").text.replace("₩", "").replace(",", "")
        )

        if price == "무료":
            price = 0

        price = int(price)
        programmers_dict["price"] = price

        url = item.find_element_by_xpath("a").get_attribute("href")

        with urllib.request.urlopen(url) as response:
            html = response.read().decode("utf8")
            soup = BeautifulSoup(html, "html.parser")
        view = soup.select("#overview-fixed-menu > div > ul > li > h6")[-2].get_text().split("명")[0]

        # print(view)
        print(title)
        programmers_dict = {
            "title": title,
            "view": view,
            "price": price,
            "score": np.nan,
            "like": np.nan,
            "college": np.nan,
            "url": url,
        }

        programmers_series = pd.Series(programmers_dict)
        programmers_df = programmers_df.append(programmers_series, ignore_index=True)

programmers_df.to_csv("crawling_data/programmers.csv", index=False)

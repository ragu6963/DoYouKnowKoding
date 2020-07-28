# 만든이 : 이성철

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from selenium import webdriver
import time
import pandas as pd
import numpy as np

sangco_df = pd.DataFrame(
    {"title": [], "view": [], "price": [], "score": [], "like": [], "college": [], "url": []}
)

url = "https://opentutorials.org/course/1"
driver = webdriver.Chrome("crawling/data/chromedriver")

with urllib.request.urlopen(url) as response:
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

links = soup.select("a.courselink")
index_list = [
    [1, 24],
    [32, 41],
]
for start, end in index_list:
    for index in range(start, end):
        sangco_dict = {}
        url = links[index]["href"]
        with urllib.request.urlopen(url) as response:
            html = response.read()
            soup = BeautifulSoup(html, "html.parser")
        title = soup.select_one("h1.entry-title").get_text()
        view = soup.select_one("span.count").get_text()

        sangco_dict["title"] = title

        driver.get(url)
        time.sleep(1)
        source = driver.page_source
        iframe_url = driver.find_element_by_xpath(
            "//*[@id='facebook_like']/div/span/iframe"
        ).get_attribute("src")

        with urllib.request.urlopen(iframe_url) as response:
            html = response.read()
            fb_soup = BeautifulSoup(html, "html.parser")
        like = fb_soup.select("#u_0_3")[0].text
        if like[-2] == "천":
            like = int(like[0]) * 1000 + int(like[2]) * 100
        else:
            like = like[:-1]
        print(f"{title} - {index} - {like}")

        sangco_dict = {
            "title": title,
            "view": view,
            "price": np.nan,
            "score": np.nan,
            "like": like,
            "college": np.nan,
            "url": url,
        }
        sangco_series = pd.Series(sangco_dict)
        sangco_df = sangco_df.append(sangco_series, ignore_index=True)

sangco_df.to_csv("crawling_data/sangco.csv", index=False)


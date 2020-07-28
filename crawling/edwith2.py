# 만든이 : 정우영

import urllib.request
import urllib.parse
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import quote
from selenium import webdriver

edwith_df = pd.DataFrame({"title": [], "view": [], "like": [], "url": []})

driver = webdriver.Chrome("crawling/data/chromedriver")
categoryId = [298, 299]
for Id in categoryId:
    driver.implicitly_wait(2)
    driver.get(f"https://www.edwith.org/search/index?categoryId={Id}")
    driver.implicitly_wait(2)
    cards = driver.find_elements_by_class_name("lecture_card")
    for card in cards:
        title = card.find_element_by_class_name("lecture_info").find_element_by_tag_name("dt").text
        like = card.find_element_by_class_name("favorite").text.replace("좋아요", "")
        view = card.find_element_by_class_name("student").text.replace("수강생 수", "")
        print(title)
        print(like)
        print(view)
        edwith_dict = {"title": title, "view": view, "like": like,"url":}
        edwith_series = pd.Series(edwith_dict)

        edwith_df = edwith_df.append(edwith_series, ignore_index=True)

edwith_df.to_csv("crawling_data/edwith.csv", index=False)

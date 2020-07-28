# 만든이 : 정우영
import urllib.parse
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from urllib.parse import quote
from selenium import webdriver
import time

edwith_df = pd.DataFrame(
    {"title": [], "view": [], "price": [], "score": [], "like": [], "college": [], "url": []}
)

driver = webdriver.Chrome("crawling/data/chromedriver")
categoryId = [24]
for Id in categoryId:
    driver.get(f"https://www.edwith.org/search/index?categoryId={Id}")
    driver.implicitly_wait(2)
    for i in range(4):
        driver.find_element_by_xpath("//*[@id='_more_area']/button").click()
        time.sleep(1)

    lectures = driver.find_element_by_class_name("lecture_list")
    lectures = lectures.find_elements_by_tag_name("li")
    for lecture in lectures:
        print(lecture.text)
        title = (
            lecture.find_element_by_class_name("lecture_info").find_element_by_tag_name("dt").text
        )
        like = lecture.find_element_by_class_name("favorite").text.replace("좋아요", "")
        view = lecture.find_element_by_class_name("student").text.replace("수강생 수", "")
        url = lecture.find_element_by_class_name("lnk_lecture").get_attribute("href")
        print(title)
        print(like)
        print(view)
        print(url)

        edwith_dict = {
            "title": title,
            "view": view,
            "price": np.nan,
            "score": np.nan,
            "like": like,
            "college": np.nan,
            "url": url,
        }
        edwith_series = pd.Series(edwith_dict)

        edwith_df = edwith_df.append(edwith_series, ignore_index=True)

edwith_df.to_csv("crawling_data/edwith3.csv", index=False)

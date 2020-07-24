# 만든이 : 정우영

import urllib.request
import urllib.parse
import json
import pandas as pd
import time, requests
from bs4 import BeautifulSoup
from urllib.parse import quote
from selenium import webdriver

kocw_df = pd.DataFrame({"title": [], "view": [], "score": []})

driver = webdriver.Chrome("crawling/data/chromedriver")
driver.get("http://www.kocw.net/home/index.do")
driver.implicitly_wait(3)


# 검색어 리스트
search_list = ["파이썬", "python", "java", "자바", "C언어", "프로그래밍"]
for keyword in search_list:
    driver.execute_script(
        f"document.getElementsByName('query')[0].value='{keyword}'"
    )
    driver.find_element_by_xpath(
        '//*[@id="search"]/form/fieldset/input[2]'
    ).click()
    driver.implicitly_wait(1)

    # 추천강의만 출력
    driver.find_element_by_xpath('//*[@id="ct_P"]/a').click()
    driver.implicitly_wait(1)

    # 100개 출력
    driver.find_element_by_xpath('//*[@id="ipageScale^input"]').click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath('//*[@id="ipageScale^input^100"]').click()
    driver.implicitly_wait(1)
    driver.find_element_by_xpath(
        '//*[@id="container"]/div/form/div[3]/div[1]/ul[2]/li[4]/a'
    ).click()
    driver.implicitly_wait(1)

    itmes = driver.find_elements_by_class_name("listCon2")
    for item in itmes:
        link = item.find_element_by_tag_name("a")
        url = link.get_attribute("href")
        with urllib.request.urlopen(url) as response:
            html = response.read().decode("utf8")
            soup = BeautifulSoup(html, "html.parser")

        title = soup.select_one("div.resultDetailTop > h3 > a").get_text()
        print(title)
        view = (
            soup.select("ul.detailViewList > li > dl > dd")[2]
            .get_text()
            .replace(",", "")
        )
        print(view)
        try:
            score = (
                soup.select("ul.detailViewList > li > dl > dd")[3]
                .get_text()
                .split("/")[0]
            )
            print(score)

        except:
            score = -1
            print("평점 X")

        kocw_dict = {"title": title, "view": view, "score": score}
        kocw_series = pd.Series(kocw_dict)

        kocw_df = kocw_df.append(kocw_series, ignore_index=True)

kocw_df.to_csv("data/kocw.csv", index=False)


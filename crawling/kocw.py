# 만든이 : 정우영

import urllib.request
import urllib.parse
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

kocw_df = pd.DataFrame(
    {
        "title": [],
        "view": [],
        "price": [],
        "score": [],
        "like": [],
        "college": [],
        "url": [],
    }
)

driver = webdriver.Chrome("crawling/data/chromedriver")
driver.get("http://www.kocw.net/home/index.do")
driver.implicitly_wait(3)

# 검색어 리스트
keyword_dict = {
    "파이썬": ["파이썬", "python"],
    "자바": ["java", "자바",],
    "c언어": ["C언어", "C프로그래밍"],
}
for subject, keyword_list in keyword_dict.items():
    for keyword in keyword_list:
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
            college = soup.select("ul.detailTitInfo > li ")[0].get_text()
            print(college)

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

            kocw_dict = {
                "title": f"[{subject}]{title}",
                "view": view,
                "price": np.nan,
                "score": score,
                "like": np.nan,
                "college": college,
                "url": url,
            }
            kocw_series = pd.Series(kocw_dict)

            kocw_df = kocw_df.append(kocw_series, ignore_index=True)

kocw_df.to_csv("crawling_data/kocw.csv", index=False)


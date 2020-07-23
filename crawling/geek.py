#만든이 김민재
import urllib.request
import urllib.parse
import json
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import quote

geek_df = pd.DataFrame({"title": [],  "view": [], "score": []})

main_url = "https://www.gseek.kr/learn/"
url_list = ["learn.list?SC_SC1_CODE=5e43e5e60905d&SC_SC2_CODE=5e43e62cf3e50","learn.list?SC_SC1_CODE=5e43e5e60905d&SC_SC2_CODE=5e43e62d0bf28"]

for url in url_list:
    with urllib.request.urlopen(main_url + url) as response:
        html = response.read().decode("utf8")
        soup = BeautifulSoup(html, "html.parser")

    cards = soup.select("div.card-lift--hover")
    for card in cards:
        # title = card.select_one("a.web").get_text()
        # print(title) 
        link = card.select_one("a.web")['href']
        # print(link)
        
        with urllib.request.urlopen(main_url+link) as response:
            html = response.read().decode("utf8")
            soup = BeautifulSoup(html, "html.parser")

        title = soup.select_one("div > h3.line").get_text()
        print(title)
        trs = soup.select("table.web > tbody > tr") 
        trs_len = len(trs)
        # 조회수 평균값
        total = 0
        for tr in trs:
            view = tr.select("td")[2].get_text().replace("회","")
            total += int(view)
        
        print(total//trs_len)
        view = total//trs_len

        # 조회수 중간값
        # middle = trs_len//2
        # view = trs[middle].select("td")[2].get_text().replace("회","")
        # print(view)

        # 좋아요 평균값    
        total = 0
        for tr in trs:
            score = tr.select("td")[3].get_text()
            total += int(score)
        print(total//trs_len)
        score = total//trs_len
        geek_dict={"title": title,  "view": view, "score": score}
        geek_series=pd.Series(geek_dict)
        geek_df=geek_df.append(geek_series,ignore_index=True)

geek_df.to_csv("./data/geek.csv",index=False)
     

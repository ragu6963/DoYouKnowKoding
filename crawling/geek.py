import urllib.request
import urllib.parse
import json
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import quote

main_url = "https://www.gseek.kr/learn/learn.list?SC_SC1_CODE=5e43e5e60905d&SC_SC2_CODE=5e43e62cf3e50"
with urllib.request.urlopen(main_url) as response:
    html = response.read().decode("utf8")
    soup = BeautifulSoup(html, "html.parser")

cards = soup.select("div.card-lift--hover")
title = cards[0].select_one("a.web").get_text()
print(title)

# 만든이 : 정우영

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

url = "https://opentutorials.org/course/1"

with urllib.request.urlopen(url) as response:
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")

links = soup.select("a.courselink")
for link in links:
    url = link["href"]
    with urllib.request.urlopen(url) as response:
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
    title = soup.select_one("h1.entry-title").get_text()
    view = soup.select_one("span.count").get_text()
    print(f"{title}-{view}")

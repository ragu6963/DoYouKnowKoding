# %%
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# %%
language_list = ["python", "java", "c", "etc"]
# %%
from wordcloud import WordCloud
import numpy as np
from os import path
import matplotlib.pyplot as plt
import os
import random

stopwords_kr = [
    "파이썬",
    "프로그래밍",
    "코딩",
    "활용",
    "자바",
    "언어",
    "프로그래밍",
    "이용한",
]


def displayWordCloud(
    data=None, backgroundcolor="white", width=800, height=600,
):
    wordcloud = WordCloud(
        font_path="C:\\Users\\admin\\AppData\\Local\\Microsoft\\Windows\\Fonts\\NanumBarunGothic.ttf",
        background_color=backgroundcolor,
        width=width,
        height=height,
        stopwords=stopwords_kr,
        mask=c_mask,
        min_font_size=4,
        repeat=True,
    ).generate(data)
    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    # wordcloud.to_file("wordCloud.png")


# %%
from PIL import Image

icon = Image.open("python.png")
python_mask = Image.new("RGB", icon.size, (255, 255, 255))
python_mask.paste(icon, icon)
python_mask = np.array(python_mask)

icon = Image.open("java.png")
java_mask = Image.new("RGB", icon.size, (255, 255, 255))
java_mask.paste(icon, icon)
java_mask = np.array(java_mask)

icon = Image.open("c.png")
c_mask = Image.new("RGB", icon.size, (255, 255, 255))
c_mask.paste(icon, icon)
c_mask = np.array(c_mask)
# %%
# Komoran 사용 명사 추출
# 사용자 사전 추가
from konlpy.tag import Komoran

for language_name in language_list[1:2]:
    title_list = []
    title_str = ""
    df = pd.read_csv(f"../analyze_data/{language_name}/{language_name}_all.csv")
    titles = df["title"]
    for title in titles:
        title_list.append(title)
        title_str += title

    # 사용자 사전 옵션 전달
    komoran = Komoran(userdic="./dic.txt")
    noun_list = komoran.nouns(title_str)
    noun_count = {}
    for noun in noun_list:
        if noun in noun_count.keys():
            noun_count[noun] += 1
        else:
            noun_count[noun] = 1
    # noun_list = sorted(noun_count.items(), key=lambda x: x[1], reverse=True)
    # print(noun_list)
    displayWordCloud(" ".join(noun_list))
    # noun_extractor._compounds_components.get(title_list, None)


# %%
# soynlp 사용 명사 추출

from soynlp.utils import DoublespaceLineCorpus
from soynlp.noun import LRNounExtractor_v2


for language_name in language_list[:1]:
    title_list = []
    df = pd.read_csv(f"../analyze_data/{language_name}/{language_name}_all.csv")
    titles = df["title"]
    for title in titles:
        title_list.append(title)

    noun_extractor = LRNounExtractor_v2()
    nouns = noun_extractor.train_extract(title_list)

    if language_name == "python":
        del nouns["Python"]
    # for noun, lank in nouns.items():
    # print(noun, lank)
    displayWordCloud(" ".join(nouns), language_name)
    # noun_extractor._compounds_components.get(title_list, None)


# %%
# konlpy okt 사용 명사 추출
from konlpy.tag import Okt

for language_name in language_list[:1]:
    title_list = []
    title_str = ""
    df = pd.read_csv(f"../analyze_data/{language_name}/{language_name}_all.csv")
    titles = df["title"]
    for title in titles:
        title_list.append(title)
        title_str += title

    okt = Okt()
    noun_list = okt.nouns(title_str)
    noun_count = {}
    for noun in noun_list:
        if noun in noun_count.keys():
            noun_count[noun] += 1
        else:
            noun_count[noun] = 1
    noun_list = sorted(noun_count.items(), key=lambda x: x[1], reverse=True)
    print(noun_list)
    # print(noun_list)
    # displayWordCloud(" ".join(nouns))
    # noun_extractor._compounds_components.get(title_list, None)

# %%
# Mecab 사용 명사 추출
from eunjeon import Mecab

for language_name in language_list[:1]:
    title_list = []
    title_str = ""
    df = pd.read_csv(f"../analyze_data/{language_name}/{language_name}_all.csv")
    titles = df["title"]
    for title in titles:
        title_list.append(title)
        title_str += title

    mecab = Mecab()
    noun_list = mecab.nouns(title_str)
    noun_count = {}
    for noun in noun_list:
        if noun in noun_count.keys():
            noun_count[noun] += 1
        else:
            noun_count[noun] = 1
    noun_list = sorted(noun_count.items(), key=lambda x: x[1], reverse=True)
    print(noun_list)
    # print(noun_list)
    # displayWordCloud(" ".join(nouns))
    # noun_extractor._compounds_components.get(title_list, None)


# %%

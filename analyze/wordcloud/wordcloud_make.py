# %%
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

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

icon = Image.open("etc.png")
etc_mask = Image.new("RGB", icon.size, (255, 255, 255))
etc_mask.paste(icon, icon)
etc_mask = np.array(etc_mask)

icon = Image.open("team.png")
team_mask = Image.new("RGB", icon.size, (255, 255, 255))
team_mask.paste(icon, icon)
team_mask = np.array(team_mask)

icon = Image.open("name.png")
name_mask = Image.new("RGB", icon.size, (255, 255, 255))
name_mask.paste(icon, icon)
name_mask = np.array(name_mask)

# %%
from wordcloud import WordCloud
import numpy as np
import matplotlib.pyplot as plt

stopwords_kr = [
    "파이썬",
    "코딩",
    "자바",
    "언어",
    "프로그래밍",
    "이용한",
    "Python",
    "Java",
]


def displayWordCloud(language_name, data):
    if language_name == "python":
        mask = python_mask
    if language_name == "java":
        mask = java_mask
    if language_name == "c":
        mask = c_mask
    if language_name == "etc":
        mask = etc_mask
    if language_name == "team":
        mask = team_mask
    if language_name == "name":
        mask = name_mask

    wordcloud = WordCloud(
        font_path="C:\\Users\\admin\\AppData\\Local\\Microsoft\\Windows\\Fonts\\NanumBarunGothic.ttf",
        background_color="white",
        width=800,
        height=600,
        stopwords=stopwords_kr,
        mask=mask,
        min_font_size=4,
        repeat=True,
    ).generate(data)
    plt.figure(figsize=(10, 10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    wordcloud.to_file(
        f"../../static/images/wordclouds/{language_name}_white.png"
    )

    # wordcloud.to_file("python_wordcloud.png")


# %%
# soynlp 사용 명사 추출
language_list = ["python", "java", "c", "etc"]
# language_list = ["java", "etc"]

from soynlp.noun import LRNounExtractor_v2

for language_name in language_list:
    title_list = []
    df = pd.read_csv(
        f"../../analyze_data/{language_name}/{language_name}_team.csv"
    )
    titles = df["title"]
    for title in titles:
        title_list.append(title)

    noun_extractor = LRNounExtractor_v2()
    nouns = noun_extractor.train_extract(title_list)
    if language_name == "python":
        del nouns["Python"]
    if language_name == "java":
        del nouns["Java"]

    # for noun, lank in nouns.items():
    #     print(noun, lank)
    displayWordCloud(language_name, " ".join(nouns))
    # noun_extractor._compounds_components.get(title_list, None)


# %%
# language_list = ["java", "etc"]

from soynlp.noun import LRNounExtractor_v2

title_list = []
df = pd.read_csv(f"../../analyze_data/team/team_team.csv")
# displayWordCloud(team, " ".join(nouns))

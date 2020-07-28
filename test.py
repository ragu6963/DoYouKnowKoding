#%%
# from numpy.core.numeric import nan
import pandas as pd
import numpy as np

df = pd.read_csv(f"analyze_data/top_3_lecture.csv", encoding="utf-8")
#%%
python_list = df[df.subject == "파이썬"]
java_list = df[df.subject == "자바"]
list1 = java_list.to_dict("list")
list1
# %%

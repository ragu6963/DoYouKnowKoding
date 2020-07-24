import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm
import platform


df = pd.read_csv('..\analyze_data/java/java_inflearn.csv', index_col = 'point', encoding = 'euc-kr')
df
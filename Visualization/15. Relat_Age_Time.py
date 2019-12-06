# 연령, 성별, 신고시각, 구급처종 상관관계

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from sklearn.cluster import KMeans
import scipy.stats as stats
import seaborn as sns

font_location = 'C:/Windows/Fonts/NanumGothic.ttf'
fm.get_fontconfig_fonts()
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)
data = data[data['긴급구조시'] == '경기도']
data = data[['신고시각', '환자연령', '환자성별', '구급처종명']]
data = data.dropna(axis=0)
data = data[data['환자연령'] <= 100]
data['신고시각'] = pd.to_datetime(data['신고시각'])
data['신고시각'] = data['신고시각'].apply(lambda x: x.hour)
data['환자연령'] = data['환자연령'].apply(lambda x: x/10)
data['환자성별'] = data['환자성별'].apply(lambda x: 0 if x=='남' else 1)

feature = data[['신고시각', '환자연령']]

sns.jointplot(x="신고시각", y="환자연령", data=feature, kind="kde")
plt.suptitle("신고시각과 환자연령의 Joint Plot 과 Kernel Density Plot", y=1.02)
plt.show()

print(feature)
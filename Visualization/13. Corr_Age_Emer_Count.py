# 평균연령, 구조횟수 상관관계

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
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
df = data[['긴급구조구']]
df = df.dropna(axis=0)

df['긴급구조구'] = df.긴급구조구.apply(lambda x: x[:4])
df['긴급구조구'] = df.긴급구조구.apply(lambda x: x.replace(' ', ''))

state_age = '평균연령집계현황.csv'
state_data = pd.read_csv(state_age, sep=',', encoding='ANSI')
state_data['행정구역명'] = state_data.행정구역명.apply(lambda x: x[4:])
state_data['행정구역명'] = state_data.행정구역명.apply(lambda x: x.replace(' ', ''))
state_data = state_data[state_data['행정구역구분명'] == '시군']

datas = []
for name in state_data['행정구역명']:
    noEmbul = len(df[df['긴급구조구'] == name])
    datas.append(noEmbul)

state_data = state_data[['평균연령']]
state_data['구조횟수'] = datas

print(state_data)
corr = state_data.corr(method='pearson')
cor = stats.pearsonr(state_data['구조횟수'], state_data['평균연령'])
sns.heatmap(data=corr, annot=True, fmt='.3f', linewidths=.5, cmap='Blues')
plt.show()

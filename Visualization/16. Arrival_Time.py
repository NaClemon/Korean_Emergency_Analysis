# 현장과의 거리

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

font_location = 'C:/Windows/Fonts/NanumGothic.ttf'
fm.get_fontconfig_fonts()
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)
df = data[['신고시각', '현장도착시각']].dropna(axis=0)
df['신고시각'] = pd.to_datetime(df['신고시각'])
df['현장도착시각'] = pd.to_datetime(df['현장도착시각'])
df['도착시간'] = df['현장도착시각'] - df['신고시각']
df['도착시간'] = df['도착시간'].apply(lambda x: x.seconds/60.0)
df = df[df['도착시간'] <= 25.0]

print(df)

plt.hist(df['도착시간'],
         density=True,
         bins=25)
plt.show()
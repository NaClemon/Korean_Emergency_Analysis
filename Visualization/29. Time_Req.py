# 소요 시간 시각화

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns
import plotly.express as px

font_location = 'C:/Windows/Fonts/NanumGothic.ttf'
fm.get_fontconfig_fonts()
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)
data = data[data['긴급구조시'] == '경기도']
data = data[['신고시각', '현장도착시각', '귀소시각', '긴급구조구']]

data['신고시각'] = pd.to_datetime(data['신고시각'], format='%H:%M')
data['현장도착시각'] = pd.to_datetime(data['현장도착시각'], format='%H:%M')
data['귀소시각'] = pd.to_datetime(data['귀소시각'], format='%H:%M')
data['소요시간'] = data['귀소시각'] - data['신고시각']
data['응급처치시간'] = (data['귀소시각'] - data['현장도착시각']) - \
                 (data['현장도착시각'] - data['신고시각'])
data['신고시각'] = data['신고시각'].dt.time
data['현장도착시각'] = data['현장도착시각'].dt.time
data['귀소시각'] = data['귀소시각'].dt.time

data['소요시간'] = pd.to_datetime(data['소요시간'])
data['소요시간'] = data['소요시간'].dt.hour * 60 + data['소요시간'].dt.minute + data['소요시간'].dt.second/60
data = data[['소요시간', '응급처치시간', '긴급구조구']]

data = data.dropna(axis=0)
print(data)

fig = px.histogram(data, x="소요시간")
fig.show()
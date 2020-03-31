# 월별, 성별 구급 사고 횟수 변화
import pandas as pd
import numpy as np
import plotly_express as px
import datetime

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)

data = data[data['긴급구조시'] == '경기도']
data = data[['신고년월일', '환자성별', '긴급구조구', '환자연령']]

# data['신고년월일'] = pd.to_datetime(data['신고년월일'])
data['환자연령'] = pd.to_numeric(data['환자연령'])
data = data.dropna(axis=0)
data['신고년월일'] = data['신고년월일'].apply(lambda x: x[5:7])
data['신고년월일'] = pd.to_numeric(data['신고년월일'])
# data['신고년월일'] = data['신고년월일'].apply(lambda x: pd.to_datetime(x, format='%Y-%m'))

data['환자연령'] = data['환자연령'].apply(lambda x: int((x/10)) * 10)
data['긴급구조구'] = data.긴급구조구.apply(lambda x: x[:4])
data['긴급구조구'] = data.긴급구조구.apply(lambda x: x.replace(' ', ''))

data = data[data['환자성별'] != '미상']
data['환자성별'].replace(['여','남'], [1,1.02], inplace=True)
data = data.groupby(['신고년월일', '환자성별', '긴급구조구', '환자연령']).size().reset_index(name='횟수')
print(data)

fig = px.scatter(data, x='환자성별', y='환자연령', animation_frame='신고년월일',
                 animation_group='환자연령',
                 size='횟수', color='환자성별',
                 hover_name='환자성별', facet_col='환자성별',
                 log_x=True, size_max=50)
fig.show()
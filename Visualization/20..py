# 미완성
import pandas as pd
import numpy as np
import plotly_express as px

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)

data = data[data['긴급구조시'] == '경기도']
data = data[['출동안전센터', '신고년월일', '환자성별', '긴급구조구']]
data['신고년월일'] = pd.to_datetime(data['신고년월일'])
data = data.dropna(axis=0)

data['긴급구조구'] = data.긴급구조구.apply(lambda x: x[:4])
data['긴급구조구'] = data.긴급구조구.apply(lambda x: x.replace(' ', ''))

data = data.groupby(['출동안전센터', '신고년월일', '환자성별', '긴급구조구']).size().reset_index(name='횟수')
data = data[data['긴급구조구'] == '가평군']

print(data)
fig = px.scatter(data, x='', y='', animation_frame='신고년월일',
                 animation_group='환자성별',
                 size='횟수', color=['환자성별', '출동안전센터'],
                 hover_name='환자성별', facet_col='출동안전센터',
                 log_x=True, size_max=50)
fig.show()
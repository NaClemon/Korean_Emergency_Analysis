# 시간 변화에 대한 접수경로 시각화
import pandas as pd
import plotly_express as px

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)

data = data[['신고시각', '접수경로']]
data['신고시각'] = data.신고시각.apply(lambda x: x[:-3])
data['신고시각'] = pd.to_numeric(data['신고시각'])

data = data.sort_values(['신고시각'], ascending=True)

data = data.groupby(['신고시각', '접수경로']).size().reset_index(name='횟수')

print(data)
fig = px.bar(data,
             x='접수경로', y='횟수',
             color='접수경로',
             animation_frame='신고시각', animation_group='접수경로')
fig.show()
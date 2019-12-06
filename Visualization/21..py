# 국가 비율 Top 7
import pandas as pd
import plotly.graph_objects as go

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)

data = data[data['긴급구조시'] == '경기도']
data = data[data['외국인유무'] == 'Y']
data = data[['국적']]
data = data.dropna(axis=0)

data = data.groupby(['국적']).size().reset_index(name='횟수')
data = data.sort_values(['횟수'], ascending=[False])
data = data[:7]

fig = go.Figure(data=[go.Pie(labels=data['국적'],
                             values=data['횟수'],
                             hole=.3)])
fig.show()
print(data)
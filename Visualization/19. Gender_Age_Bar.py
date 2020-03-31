# 성별, 나이 막대그래프
import numpy as np
import pandas as pd
import plotly.graph_objects as go

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)

data = data[['환자성별', '환자연령']]
data = pd.DataFrame(data)
data = data[(data['환자성별'] == '남') | (data['환자성별'] == '여')]
data['환자연령'] = np.where(data['환자연령'], np.floor(data['환자연령']/10), data['환자연령'])
data['환자연령'] = data['환자연령'].fillna(-1).astype(np.int)
delete_index = data[(data['환자연령'] <= -1) | (data['환자연령'] >= 12)].index
data = data.drop(delete_index)
data = data.groupby(['환자성별', '환자연령']).size().reset_index(name='횟수')
male_data = data[data['환자성별'] == '남']
female_data = data[data['환자성별'] == '여']

print(data)

fig = go.Figure()
fig.add_trace(go.Bar(
    x = male_data['환자연령'],
    y = male_data['횟수'],
    name = '남성',
    marker_color = 'lightslategrey'
))
fig.add_trace(go.Bar(
    x = female_data['환자연령'],
    y = female_data['횟수'],
    name = '여성',
    marker_color = 'crimson'
))
fig.show()
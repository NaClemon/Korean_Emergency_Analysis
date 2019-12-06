# 구급사고종별 원형 그래프(미완성)
import pandas as pd
import plotly.graph_objects as go

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)

data = data[['구급사고종별상위', '구급사고종별하위']]
data = data.dropna(axis=0)

data = data.groupby(['구급사고종별상위', '구급사고종별하위']).size().reset_index(name='횟수')
data['횟수'] = pd.to_numeric(data['횟수'])
data = data[data['횟수'] >= 100]

data['구급사고종별하위'] = data['구급사고종별하위'].apply(lambda x: x.replace(',', ''))

fig = go.Figure(go.Sunburst(
    labels=data['구급사고종별하위'],
    parents=data['구급사고종별상위'],
    values=data['횟수']
))
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
print(data)
fig.show()
# 구급사고종별 원형 그래프
import pandas as pd
import plotly.graph_objects as go

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)

data = data[['구급사고종별상위', '구급사고종별하위']]
data = data.dropna(axis=0)

data = data.groupby(['구급사고종별상위', '구급사고종별하위']).size().reset_index(name='횟수')
data['횟수'] = pd.to_numeric(data['횟수'])

data['구급사고종별하위'] = data['구급사고종별하위'].apply(lambda x: x.replace(',', ''))

df = data['구급사고종별상위'].unique().tolist()

labels = ['구급사고분류'] + df + data['구급사고종별하위'].values.tolist()
parents = [''] + (['구급사고분류'] * len(df)) + data['구급사고종별상위'].values.tolist()

temp = []
for index in df:
    sumlist = data[data['구급사고종별상위'] == index]
    print(len(sumlist))
    sum = sumlist['횟수'].sum()
    temp.append(sum)

values = [data['횟수'].sum()] + temp + data['횟수'].values.tolist()

print(labels)
print(parents)
print(values)

fig = go.Figure()
fig.add_trace(go.Sunburst(
    labels=labels[:47],
    parents=parents[:47],
    values=values[:47],
    domain=dict(column=0, row=0),
    branchvalues="total",
))
fig.add_trace(go.Sunburst(
    labels=labels[47:50],
    parents=parents[47:50],
    values=values[47:50],
    domain=dict(column=0, row=1),
    branchvalues="total",
))
fig.add_trace(go.Sunburst(
    labels=labels[50:],
    parents=parents[50:],
    values=values[50:],
    domain=dict(column=1, row=0),
    branchvalues="total",
))
fig.update_layout(grid= dict(columns=2, rows=2),
                  margin = dict(t=0, l=0, r=0, b=0))
fig.show()
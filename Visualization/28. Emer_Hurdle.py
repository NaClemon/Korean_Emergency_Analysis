# 장애요인 원형 그래프
import pandas as pd
import plotly.graph_objects as go

def build_hierarchical_dataframe(df, levels, value_column, color_columns=None):
    df_all_trees = pd.DataFrame(columns=['id', 'parent', 'value'])
    for i, level in enumerate(levels):
        df_tree = pd.DataFrame(columns=['id', 'parent', 'value'])
        dfg = df.groupby(levels[i:]).sum(numerical_only=True)
        dfg = dfg.reset_index()
        df_tree['id'] = dfg[level].copy()
        if i < len(levels) - 1:
            df_tree['parent'] = dfg[levels[i+1]].copy()
        else:
            df_tree['parent'] = 'total'
        df_tree['value'] = dfg[value_column]
        df_all_trees = df_all_trees.append(df_tree, ignore_index=True)
    total = pd.Series(dict(id='total', parent='',
                              value=df[value_column].sum()))
    df_all_trees = df_all_trees.append(total, ignore_index=True)
    return df_all_trees

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)

data = data[['긴급구조활동장애요인']]
data = data.dropna(axis=0)
new = data['긴급구조활동장애요인'].str.split(',')
data = new.apply(lambda x: pd.Series(x))
data.columns = ['분류1', '분류2', '분류3', '분류4', '분류5', '분류6', '분류7']
data = data[['분류1', '분류2', '분류3']].dropna()
print(data['분류1'].unique())
data = data.groupby(['분류1', '분류2', '분류3']).size().reset_index(name='횟수')
levels = ['분류1', '분류2', '분류3']
value_column = '횟수'

datat = build_hierarchical_dataframe(data, levels, value_column)
dataF = datat[(datat['id'] == 'total') | (datat['parent'] == 'total')]
dataa = datat[(datat['value'] >= 85) & (datat['parent'] == '장거리이송')]
datab = datat[(datat['value'] >= 85) & (datat['parent'] == '교통정체')]
datac = datat[(datat['value'] >= 85) & (datat['parent'] == '원거리 출동')]
print(dataF)
print(dataa)
print(datab)
print(datac)

fig = go.Figure()
fig.add_trace(go.Sunburst(
    labels=dataF['id'],
    parents=dataF['parent'],
    values=dataF['value'],
    domain=dict(column=0, row=0),
    branchvalues="total",
))
fig.add_trace(go.Sunburst(
    labels=dataa['id'] + ['장거리이송'],
    parents=dataa['parent'] + [''],
    values=dataa['value'] + [2138],
    domain=dict(column=1, row=0),
    branchvalues="total",
))
fig.add_trace(go.Sunburst(
    labels=datab['id'] + ['교통정체'],
    parents=datab['parent'] + [''],
    values=datab['value'] + [1758],
    domain=dict(column=0, row=1),
    branchvalues="total",
))
fig.add_trace(go.Sunburst(
    labels=datac['id'] + ['원거리 출동'],
    parents=datac['parent'] + [''],
    values=datac['value'] + [541],
    domain=dict(column=1, row=1),
    branchvalues="total",
))
fig.update_layout(grid= dict(columns=2, rows=2),
                  margin = dict(t=0, l=0, r=0, b=0))
fig.show()
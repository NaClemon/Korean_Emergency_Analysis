# 결정트리

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
import pydot
import graphviz
from IPython.display import display

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data3 = pd.read_csv('Data/2018년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data4 = pd.read_csv('Data/2018년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)
datau = pd.concat([data3, data4], sort=False)
datau['긴급구조시'] = datau['발생장소시도명']
data = pd.concat([data, datau], sort=False)
data = data[data['긴급구조시'] == '경기도']
data = data[['신고시각', '환자연령', '환자성별', '구급처종명', '구급사고종별상위', '의식상태']]
data = data[data['환자성별'] != '미상']
data = data.dropna(axis=0)

numval = []
for i in range(len(data['구급처종명'].unique())):
    numval.append(i)

numval2 = []
for i in range(len(data['의식상태'].unique())):
    numval2.append(i)

data['신고시각'] = pd.to_datetime(data['신고시각'], format='%H:%M')
data['신고시각'] = data['신고시각'].dt.hour * 60 + data['신고시각'].dt.minute + data['신고시각'].dt.second/60
data['환자성별'].replace(['여','남'], [0,1], inplace=True)
data['의식상태'] = data['의식상태'].apply(lambda x: x[:1])
data['구급처종명'].replace(data['구급처종명'].unique(), numval, inplace=True)
data['의식상태'].replace(data['의식상태'].unique(), numval2, inplace=True)

X_train, X_test, y_train, y_test = train_test_split(
    data[['신고시각', '환자연령', '환자성별', '구급처종명']], data[['구급사고종별상위']], stratify=data[['구급사고종별상위']], random_state=42)
print(data)
tree = DecisionTreeClassifier(max_depth=4, random_state=0)
tree.fit(X_train, y_train)

print("훈련 세트 정확도: {:.3f}".format(tree.score(X_train, y_train)))
print("테스트 세트 정확도: {:.3f}".format(tree.score(X_test, y_test)))

export_graphviz(tree, out_file="tree.dot",
                impurity=False, filled=True)
# with open("tree.dot", encoding='UTF8') as f:
#     dot_graph = f.read()
# display(graphviz.Source(dot_graph))
(graph, ) = pydot.graph_from_dot_file('Result/31. Desicion_Tree_Type.dot', encoding='utf-8')
graph.write_png('Result/31. Desicion_Tree_Type.png')
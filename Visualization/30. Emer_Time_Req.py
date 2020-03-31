# 환자 상태에 따른 응급처치 시간

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import seaborn as sns
import plotly_express as px

font_location = 'C:/Windows/Fonts/NanumGothic.ttf'
fm.get_fontconfig_fonts()
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)
data = data[data['긴급구조시'] == '경기도']
data = data[['신고시각', '현장도착시각', '귀소시각', '긴급구조구', '의식상태']]
data = data.dropna(axis=0)
data['의식상태'] = data['의식상태'].apply(lambda x: x[:1])

data['신고시각'] = pd.to_datetime(data['신고시각'], format='%H:%M')
data['현장도착시각'] = pd.to_datetime(data['현장도착시각'], format='%H:%M')
data['귀소시각'] = pd.to_datetime(data['귀소시각'], format='%H:%M')
data['응급처치시간'] = (data['귀소시각'] - data['현장도착시각']) - \
                 (data['현장도착시각'] - data['신고시각'])
data['신고시각'] = data['신고시각'].dt.time
data['현장도착시각'] = data['현장도착시각'].dt.time
data['귀소시각'] = data['귀소시각'].dt.time

data = data[['응급처치시간', '의식상태', '긴급구조구']]
data = data.dropna(axis=0)

data['응급처치시간'] = pd.to_datetime(data['응급처치시간'])
data['응급처치시간'] = data['응급처치시간'].dt.hour * 60 + data['응급처치시간'].dt.minute + data['응급처치시간'].dt.second/60
data = data[data['응급처치시간'] <= 200]

fig = go.Figure()
fig = make_subplots(rows=2, cols=2)
A = go.Histogram(x=data[data['의식상태'] == 'A']['응급처치시간'],
                 name='A',
                      autobinx=False)
P = go.Histogram(x=data[data['의식상태'] == 'P']['응급처치시간'],
                 name='P',
                      autobinx=False)
U = go.Histogram(x=data[data['의식상태'] == 'U']['응급처치시간'],
                 name='U',
                      autobinx=False)
V = go.Histogram(x=data[data['의식상태'] == 'V']['응급처치시간'],
                 name='V',
                      autobinx=False)

fig.append_trace(A, 1, 1)
fig.append_trace(P, 1, 2)
fig.append_trace(U, 2, 1)
fig.append_trace(V, 2, 2)

fig.show()

print(data)
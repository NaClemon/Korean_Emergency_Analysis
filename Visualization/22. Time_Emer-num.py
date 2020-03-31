# 시간별 구급활동

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

font_location = 'C:/Windows/Fonts/NanumGothic.ttf'
fm.get_fontconfig_fonts()
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)

data1 = pd.read_csv('Data/2017년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
data2 = pd.read_csv('Data/2017년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
data = pd.concat([data1, data2], sort=False)
data = data[data['긴급구조시'] == '경기도']
data = data[['신고시각']]

data['신고시각'] = data.신고시각.apply(lambda x: x[:-3])
data['신고시각'] = pd.to_numeric(data['신고시각'])

data = data.sort_values(['신고시각'], ascending=True)

datau1 = pd.read_csv('Data/2018년 상반기 구급활동현황.csv', sep=',', encoding='ANSI')
datau2 = pd.read_csv('Data/2018년 하반기 구급활동현황.csv', sep=',', encoding='ANSI')
datau = pd.concat([datau1, datau2], sort=False)
datau = datau[datau['발생장소시도명'] == '경기도']
datau = datau[['신고시각']]

datau['신고시각'] = datau.신고시각.apply(lambda x: x[:-3])
datau['신고시각'] = pd.to_numeric(datau['신고시각'])

datau = datau.sort_values(['신고시각'], ascending=True)

time = data['신고시각'].unique()

timecount = []
timecountu = []
for i in time:
    temp = len(data[data['신고시각'] == i])
    tempu = len(datau[datau['신고시각'] == i])
    timecount.append(temp)
    timecountu.append(temp)

a = np.array([timecount], dtype=np.int64)
b = np.array([timecountu], dtype=np.int64)
dataab = np.concatenate((a, b)).T

myData = pd.DataFrame(data=dataab,
                      index=time,
                      columns=['2017', '2018']).T

print(myData)
plt.figure(figsize=(10, 1))
sns.heatmap(myData, linewidths=.5,
            cmap='OrRd')
plt.show()